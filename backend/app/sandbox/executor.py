"""Sandbox'ning TASHQI qismi: bola jarayonni boshqaradi.

Himoya qatlamlari (har biri alohida, biri ikkinchisiga tayanmaydi):

  1. `policy.check()` — AST filtri, kodni bajarishdan oldin.
  2. Alohida JARAYON — `python -I` (izolyatsiya rejimi: PYTHON* muhit
     o'zgaruvchilari, foydalanuvchi site-packages va cwd e'tiborsiz).
  3. `runner.py` ichidagi resurs cheklovlari: RLIMIT_CPU, RLIMIT_AS,
     RLIMIT_FSIZE=0 (fayl yozib bo'lmaydi), RLIMIT_NOFILE, RLIMIT_NPROC=0.
  4. Tarmoq yopilgan (socket ishlamaydi).
  5. Bo'sh vaqtinchalik katalog, tozalangan muhit o'zgaruvchilari.
  6. Devor soati bo'yicha timeout va butun JARAYONLAR GURUHINI o'ldirish.
  7. Chiqish hajmi `labkit` tomonidan cheklangan.

Bu arxitektura foydalanuvchi kodini HECH QACHON asosiy jarayonda
`exec()` qilmaydi. Ishlab chiqarishda buning ustiga konteyner
darajasidagi izolyatsiya qo'yilishi kerak — README dagi
"Ishlab chiqarish uchun sandbox" bo'limiga qarang.
"""

from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from app.sandbox.policy import check

_HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class RunLimits:
    """Standart qiymatlar o'lchovga asoslangan.

    150 mavzu + 5 loyihaning hammasi sandbox'da bajarib ko'rilgan:
    o'rtacha 1,1 s, eng sekini (su-16) 7,9 s. Shuning uchun 20 s devor
    soati yetarli zaxira beradi. Xotira: scipy import qilishning o'zi
    ~400 MB virtual adres talab qiladi, 256 MB da u ishlamaydi.
    """

    wall_seconds: float = 20.0
    cpu_seconds: int = 15
    memory_mb: int = 768
    max_output_bytes: int = 4_000_000


@dataclass
class RunResult:
    ok: bool
    values: list[dict[str, Any]] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    series: list[dict[str, Any]] = field(default_factory=list)
    tables: list[dict[str, Any]] = field(default_factory=list)
    stdout: str = ""
    error: str = ""
    error_type: str = ""
    duration_ms: int = 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok, "values": self.values, "notes": self.notes,
            "series": self.series, "tables": self.tables,
            "stdout": self.stdout, "error": self.error,
            "error_type": self.error_type, "duration_ms": self.duration_ms,
        }


def _fail(msg: str, kind: str, ms: int = 0) -> RunResult:
    return RunResult(ok=False, error=msg, error_type=kind, duration_ms=ms)


def run_code(code: str, params: dict[str, float] | None = None,
             limits: RunLimits | None = None) -> RunResult:
    """Foydalanuvchi kodini izolyatsiyalangan jarayonda bajaradi."""
    lim = limits or RunLimits()

    report = check(code)                       # 1-qatlam
    if not report.ok:
        return _fail(report.reason, "PolicyError")

    workdir = tempfile.mkdtemp(prefix="lab-")
    started = time.perf_counter()
    try:
        payload = json.dumps({
            "code": code,
            "params": {str(k): float(v) for k, v in (params or {}).items()},
            "cpu_seconds": lim.cpu_seconds,
            "memory_mb": lim.memory_mb,
            "workdir": workdir,
        })
        env = {
            "PATH": "/usr/bin:/bin",
            "HOME": workdir,
            "TMPDIR": workdir,
            "OPENBLAS_NUM_THREADS": "1",       # cheklovlar ichida barqaror
            "OMP_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1",
            "MPLBACKEND": "Agg",
        }
        proc = subprocess.Popen(
            [sys.executable, "-I", "-B", str(_HERE / "runner.py")],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=env, cwd=workdir,
            start_new_session=True,            # o'z jarayonlar guruhi
            text=True,
        )
        try:
            out, err = proc.communicate(payload, timeout=lim.wall_seconds)
        except subprocess.TimeoutExpired:
            _kill_group(proc)
            proc.communicate()
            ms = int((time.perf_counter() - started) * 1000)
            return _fail(
                f"Vaqt tugadi: kod {lim.wall_seconds:.0f} sekunddan ortiq "
                f"ishladi va to'xtatildi.", "TimeoutError", ms)

        ms = int((time.perf_counter() - started) * 1000)
        if len(out) > lim.max_output_bytes:
            return _fail("Natija juda katta", "OutputTooLarge", ms)
        if proc.returncode != 0 or not out.strip():
            return _fail(_diagnose(proc.returncode, err), _kind(proc.returncode), ms)
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            return _fail("Sandbox natijani o'qib bo'lmadi", "ProtocolError", ms)
        return RunResult(
            ok=bool(data.get("ok")),
            values=data.get("values", []), notes=data.get("notes", []),
            series=data.get("series", []), tables=data.get("tables", []),
            stdout=data.get("stdout", ""), error=data.get("error", ""),
            error_type=data.get("error_type", ""), duration_ms=ms,
        )
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def _kill_group(proc: subprocess.Popen) -> None:
    for sig in (signal.SIGKILL,):
        try:
            os.killpg(os.getpgid(proc.pid), sig)
        except (ProcessLookupError, PermissionError):
            proc.kill()


def _kind(rc: int) -> str:
    if rc == -signal.SIGKILL:
        return "MemoryLimit"
    if rc == -signal.SIGXCPU:
        return "CpuLimit"
    return "SandboxError"


def _diagnose(rc: int, err: str) -> str:
    if rc == -signal.SIGKILL:
        return ("Xotira chegarasi oshib ketdi yoki jarayon to'xtatildi. "
                "Masala o'lchamini kichraytiring.")
    if rc == -signal.SIGXCPU:
        return ("Protsessor vaqti chegarasi oshib ketdi. Iteratsiyalar "
                "sonini yoki to'r o'lchamini kamaytiring.")
    tail = (err or "").strip().splitlines()
    if tail:
        return f"Sandbox xatosi: {tail[-1][:300]}"
    return f"Sandbox kutilmaganda to'xtadi (kod {rc})"

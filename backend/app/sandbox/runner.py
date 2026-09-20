"""Sandbox ICHIDAGI jarayon. Bu fayl ALOHIDA jarayonda ishga tushadi.

Ketma-ketlik ataylab shunday tartibda:
  1. Og'ir modullarni (numpy/scipy/sympy) OLDIN import qilamiz —
     aks holda RLIMIT_AS ularning virtual xotirasini bo'g'ib qo'yadi.
  2. Tarmoqni yopamiz (socket butunlay ishlamaydigan holga keltiriladi).
  3. Resurs cheklovlarini qo'yamiz (CPU, xotira, fayl, jarayon).
  4. Bo'sh vaqtinchalik katalogga o'tamiz va sys.path ni tozalaymiz.
  5. Faqat SHUNDAN KEYIN foydalanuvchi kodini bajaramiz.

Natija stdout'ga bitta qator JSON bo'lib chiqadi. Hech qanday boshqa
narsa stdout'ga yozilmasligi uchun foydalanuvchi kodi davomida
stdout stderr'ga yo'naltiriladi.
"""

from __future__ import annotations

import builtins
import io
import json
import os
import resource
import sys

# `python -I` skript katalogini sys.path ga QO'SHMAYDI (-P nazarda tutilgan)
# va PYTHONPATH ni ham e'tiborsiz qoldiradi (-E). Shuning uchun labkit va
# policy_inline ni topish uchun o'z katalogimizni o'zimiz qo'shamiz.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


def _preimport() -> None:
    for name in ("numpy", "scipy", "scipy.linalg", "scipy.optimize",
                 "scipy.sparse", "scipy.sparse.linalg", "scipy.special",
                 "scipy.integrate", "scipy.interpolate", "scipy.signal",
                 "scipy.sparse.csgraph", "scipy.stats", "sympy"):
        try:
            __import__(name)
        except ImportError:
            pass


def _kill_network() -> None:
    """Tarmoqqa chiqishni imkonsiz qiladi."""
    import socket

    def _blocked(*_a, **_k):
        raise OSError("Tarmoqqa murojaat sandbox'da taqiqlangan")

    for attr in ("socket", "create_connection", "create_server",
                 "socketpair", "getaddrinfo", "gethostbyname"):
        if hasattr(socket, attr):
            setattr(socket, attr, _blocked)
    sys.modules["socket"].socket = _blocked  # type: ignore[attr-defined]


def _limits(cpu_s: int, mem_mb: int, nofile: int) -> None:
    mem = mem_mb * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s + 1))
    resource.setrlimit(resource.RLIMIT_AS, (mem, mem))
    resource.setrlimit(resource.RLIMIT_DATA, (mem, mem))
    resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))       # fayl yozib bo'lmaydi
    resource.setrlimit(resource.RLIMIT_NOFILE, (nofile, nofile))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    try:                                                     # yangi jarayon yo'q
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    except (ValueError, OSError):
        pass


#: Foydalanuvchi kodiga beriladigan builtins — xavflilari olib tashlangan.
_DENY = {
    "eval", "exec", "compile", "open", "input", "breakpoint", "__import__",
    "globals", "locals", "vars", "dir", "getattr", "setattr", "delattr",
    "memoryview", "help", "exit", "quit", "license", "credits", "copyright",
}


def _safe_builtins() -> dict:
    ns = {k: v for k, v in vars(builtins).items() if k not in _DENY}
    # import faqat oq ro'yxatdagi modullar uchun
    from policy_inline import ALLOWED_ROOTS

    real_import = builtins.__import__

    def guarded(name, g=None, l=None, fromlist=(), level=0):
        if level != 0:
            raise ImportError("nisbiy import taqiqlangan")
        if name.split(".", 1)[0] not in ALLOWED_ROOTS:
            raise ImportError(f"'{name}' modulini import qilish taqiqlangan")
        return real_import(name, g, l, fromlist, level)

    ns["__import__"] = guarded
    return ns


def main() -> int:
    payload = json.loads(sys.stdin.read())
    code = payload["code"]
    params = payload.get("params") or {}
    cpu_s = int(payload.get("cpu_seconds", 10))
    mem_mb = int(payload.get("memory_mb", 512))

    _preimport()
    _kill_network()

    workdir = payload.get("workdir") or "."
    os.chdir(workdir)
    # cwd va foydalanuvchi kataloglari sys.path da qolmasin,
    # lekin sandbox katalogi (labkit) qolishi shart
    sys.path[:] = [p for p in sys.path
                   if p and p not in (".", os.getcwd(), workdir)]

    import labkit

    labkit._reset(params)
    _limits(cpu_s, mem_mb, nofile=64)

    real_stdout = sys.stdout
    sys.stdout = io.StringIO()          # print() natijani buzmasin
    ns = {"__name__": "__lab__", "__builtins__": _safe_builtins()}
    try:
        exec(compile(code, "<lab>", "exec"), ns)   # noqa: S102 - izolyatsiyalangan
        out = {"ok": True, **labkit._collect()}
    except BaseException as exc:                    # noqa: BLE001
        out = {
            "ok": False,
            "error_type": type(exc).__name__,
            "error": str(exc)[:2000],
            **labkit._collect(),
        }
    finally:
        captured = sys.stdout.getvalue()[:4000]
        sys.stdout = real_stdout
    out["stdout"] = captured
    sys.stdout.write(json.dumps(out))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

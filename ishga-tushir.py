#!/usr/bin/env python3
"""Docker'siz ishga tushirish — hammasi http://localhost:7070 da.

Bu skript Docker bo'lmagan kompyuterda ham ishlaydi: u backendni
8000-portda ko'taradi va frontendning yig'ilgan nusxasini 7070-portda
beradi, /api so'rovlarini esa backendga uzatadi (nginx o'rniga).

    python ishga-tushir.py

Talablar: Python 3.11+ va (frontendni yig'ish uchun) Node.js 18+.
Agar frontend allaqachon yig'ilgan bo'lsa (frontend/dist), Node kerak emas.
"""

from __future__ import annotations

import argparse
import http.server
import os
import shutil
import socketserver
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "frontend" / "dist"
BACKEND = ROOT / "backend"
API_PREFIXES = ("/api/", "/health", "/docs", "/openapi.json", "/static/", "/redoc")

PORT = int(os.environ.get("MEXANIKA_PORT", "7070"))
API_PORT = int(os.environ.get("MEXANIKA_API_PORT", "8000"))
API = f"http://127.0.0.1:{API_PORT}"


def log(msg: str) -> None:
    print(f"  {msg}", flush=True)


def need(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def step_export() -> None:
    log("1/4  Kurikulum JSON ni yaratish…")
    r = subprocess.run([sys.executable, "-m", "content.curriculum.export"],
                       cwd=str(ROOT), capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr)
        sys.exit("Kurikulum eksporti yiqildi.")
    log("     " + r.stdout.strip().splitlines()[-1])


def step_frontend(force: bool) -> None:
    if DIST.joinpath("index.html").exists() and not force:
        log("2/4  Frontend allaqachon yig'ilgan (frontend/dist) — o'tkazib yuborildi")
        return
    if not need("npm"):
        sys.exit("Node.js/npm topilmadi va frontend/dist yo'q.\n"
                 "Node.js 18+ o'rnating yoki tayyor dist bilan ZIP dan foydalaning.")
    log("2/4  Frontendni yig'ish (bir necha daqiqa)…")
    fe = ROOT / "frontend"
    if not (fe / "node_modules").is_dir():
        subprocess.run(["npm", "install", "--no-audit", "--no-fund"],
                       cwd=str(fe), check=True)
    subprocess.run(["npm", "run", "build"], cwd=str(fe), check=True)


def step_backend() -> subprocess.Popen:
    log(f"3/4  Backend ({API}) ishga tushmoqda…")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(BACKEND)
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app",
         "--host", "127.0.0.1", "--port", str(API_PORT), "--log-level", "warning"],
        cwd=str(BACKEND), env=env)
    for _ in range(90):
        try:
            with urllib.request.urlopen(f"{API}/health", timeout=2) as r:
                if r.status == 200:
                    log("     backend tayyor")
                    return proc
        except Exception:
            time.sleep(1)
    proc.terminate()
    sys.exit("Backend ishga tushmadi. backend/requirements.txt o'rnatilganmi?")


class Handler(http.server.SimpleHTTPRequestHandler):
    """Statik fayllar + /api proksisi + SPA fallback."""

    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(DIST), **k)

    def log_message(self, fmt, *args):  # jim rejim
        pass

    def _is_api(self) -> bool:
        return self.path.startswith(API_PREFIXES)

    def _proxy(self, body: bytes | None) -> None:
        url = API + self.path
        req = urllib.request.Request(url, data=body, method=self.command)
        for h in ("Content-Type", "Accept", "Content-Length"):
            if h in self.headers:
                req.add_header(h, self.headers[h])
        try:
            with urllib.request.urlopen(req, timeout=120) as up:
                data = up.read()
                self.send_response(up.status)
                for k, v in up.headers.items():
                    if k.lower() not in ("transfer-encoding", "connection"):
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(data)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type",
                             e.headers.get("Content-Type", "application/json"))
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as exc:
            msg = f'{{"detail":"Backendga ulanib bo\'lmadi: {exc}"}}'.encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)

    def do_GET(self):
        if self._is_api():
            return self._proxy(None)
        path = (DIST / self.path.lstrip("/")).resolve()
        if not str(path).startswith(str(DIST.resolve())) or not path.is_file():
            self.path = "/index.html"          # SPA marshrutlari
        return super().do_GET()

    def do_POST(self):
        if not self._is_api():
            self.send_error(404)
            return
        n = int(self.headers.get("Content-Length", 0))
        self._proxy(self.rfile.read(n) if n else b"")


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main() -> int:
    ap = argparse.ArgumentParser(description="Mexanika Akademiyasini ishga tushirish")
    ap.add_argument("--rebuild", action="store_true", help="frontendni qayta yig'ish")
    args = ap.parse_args()

    print("\nMexanika Akademiyasi\n" + "-" * 52)
    step_export()
    step_frontend(args.rebuild)
    backend = step_backend()

    log(f"4/4  Sayt: http://localhost:{PORT}")
    print("-" * 52)
    print(f"\n  Saytni oching:  http://localhost:{PORT}")
    print(f"  API hujjati  :  http://localhost:{PORT}/docs")
    print("\n  To'xtatish uchun: Ctrl+C\n")

    try:
        with Server(("0.0.0.0", PORT), Handler) as srv:
            srv.serve_forever()
    except KeyboardInterrupt:
        print("\n  To'xtatilmoqda…")
    finally:
        backend.terminate()
        try:
            backend.wait(timeout=10)
        except subprocess.TimeoutExpired:
            backend.kill()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

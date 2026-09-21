"""Manim sahnalarini render qilish.

Manim og'ir tizim kutubxonalariga (cairo, pango, ffmpeg) tayanadi,
shuning uchun uni alohida konteynerda ishlatish tavsiya etiladi:

    docker compose --profile manim run --rm manim python -m animatsiya.render --all

Mahalliy muhitda manim o'rnatilgan bo'lsa:

    python -m animatsiya.render --all              # hammasi
    python -m animatsiya.render --topic su-30      # bitta mavzuniki
    python -m animatsiya.render --scene FullChain  # nom bo'yicha
    python -m animatsiya.render --list             # ro'yxat
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "animatsiya" / "media"

QUALITY = {"past": "-ql", "orta": "-qm", "yuqori": "-qh", "4k": "-qk"}


def _refs() -> list[tuple[str, str, str, str]]:
    sys.path.insert(0, str(ROOT))
    from content.curriculum.registry import all_topics
    out = []
    for t in all_topics():
        m = t.lesson.manim
        if m:
            out.append((t.id, m.module, m.scene, m.title))
    return out


def render_one(module: str, scene: str, quality: str) -> int:
    path = ROOT / module
    if not path.exists():
        print(f"  YO'Q: {module}")
        return 1
    cmd = [sys.executable, "-m", "manim", QUALITY[quality],
           "--media_dir", str(OUT), str(path), scene]
    print("  $ " + " ".join(cmd[-4:]))
    return subprocess.run(cmd, cwd=str(ROOT / "animatsiya" / "scenes")).returncode


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Manim sahnalarini render qilish")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all", action="store_true", help="barcha sahnalar")
    g.add_argument("--topic", help="bitta mavzu id si, masalan su-30")
    g.add_argument("--scene", help="sahna sinfining nomi")
    g.add_argument("--list", action="store_true", help="sahnalar ro'yxati")
    ap.add_argument("--quality", choices=sorted(QUALITY), default="orta")
    args = ap.parse_args(argv)

    refs = _refs()

    if args.list:
        print(f"{len(refs)} ta sahna:\n")
        for tid, module, scene, title in refs:
            print(f"  {tid:8s} {scene:28s} {Path(module).name:26s} {title[:40]}")
        return 0

    if args.topic:
        refs = [r for r in refs if r[0] == args.topic]
    elif args.scene:
        refs = [r for r in refs if r[2] == args.scene]
    if not refs:
        print("Mos sahna topilmadi")
        return 1

    try:
        import manim  # noqa: F401
    except ImportError:
        print("manim o'rnatilmagan.\n"
              "  pip install manim   (cairo, pango va ffmpeg kerak)\n"
              "  yoki: docker compose --profile manim run --rm manim \\\n"
              "            python -m animatsiya.render --all")
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    failed = []
    for tid, module, scene, _title in refs:
        print(f"[{tid}] {scene}")
        if render_one(module, scene, args.quality):
            failed.append(scene)
    print(f"\nTayyor: {len(refs) - len(failed)} / {len(refs)}")
    if failed:
        print("Yiqilgan sahnalar: " + ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

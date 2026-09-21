"""Har bir ManimRef HAQIQATAN mavjud faylga va sinfga ishora qiladimi?

Bu tekshiruv manim o'rnatilmagan muhitda ham ishlaydi: u sahnalarni
RENDER qilmaydi, faqat modul faylini va Scene sinfini topadi hamda
sinfning `construct` metodi borligini tasdiqlaydi.

Ishlatish:
    python -m animatsiya.verify          # faqat havolalarni tekshirish
    python -m animatsiya.verify --build  # sahnalarni qurib ham ko'rish
                                         # (manim yoki uning stub'i kerak)
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _classes_in(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return {n.name for n in tree.body if isinstance(n, ast.ClassDef)}


def _has_construct(path: Path, name: str) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for n in tree.body:
        if isinstance(n, ast.ClassDef) and n.name == name:
            return any(isinstance(f, ast.FunctionDef) and f.name == "construct"
                       for f in n.body)
    return False


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Manim havolalarini tekshirish")
    ap.add_argument("--build", action="store_true",
                    help="sahnalarni qurib ham ko'rish (manim kerak)")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(ROOT))
    from content.curriculum.registry import all_topics

    refs = [(t.id, t.lesson.manim.module, t.lesson.manim.scene)
            for t in all_topics() if t.lesson.manim]

    problems: list[str] = []
    files: set[Path] = set()
    for tid, module, scene in refs:
        path = ROOT / module
        files.add(path)
        if not path.exists():
            problems.append(f"{tid}: '{module}' fayli YO'Q")
            continue
        classes = _classes_in(path)
        if scene not in classes:
            problems.append(f"{tid}: '{module}' ichida '{scene}' sinfi YO'Q")
        elif not _has_construct(path, scene):
            problems.append(f"{tid}: '{scene}' da construct() metodi YO'Q")

    print(f"ManimRef havolalari : {len(refs)}")
    print(f"Noyob sahna         : {len({s for _, _, s in refs})}")
    print(f"Modul fayllari      : {len(files)}")
    for p in problems:
        print(f"  XATO {p}")
    if problems:
        print(f"\nNATIJA: {len(problems)} ta muammo")
        return 1

    if args.build:
        sys.path.insert(0, str(ROOT / "animatsiya" / "scenes"))
        built = 0
        for _tid, module, scene in refs:
            mod = __import__(Path(module).stem)
            cls = getattr(mod, scene)
            obj = cls()
            obj.setup()
            obj.construct()
            built += 1
        print(f"Qurilgan sahnalar   : {built}")

    print("\nNATIJA: barcha havolalar to'g'ri")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

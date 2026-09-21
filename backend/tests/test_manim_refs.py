"""ManimRef havolalari haqiqiy fayl va sinfga ishora qiladimi?

40-talab: mavjud bo'lmagan faylga havola bo'lmasligi kerak. Manim bu
muhitda o'rnatilmagan, shuning uchun sahnalar RENDER qilinmaydi —
lekin ularning mavjudligi va tuzilishi AST orqali tekshiriladi.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "content" / "generated" / "curriculum.json"


@pytest.fixture(scope="module")
def refs() -> list[tuple[str, str, str]]:
    data = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    out = []
    for t in data["topics"]:
        m = t["lesson"].get("manim")
        if m:
            out.append((t["id"], m["module"], m["scene"]))
    return out


def test_there_are_manim_references(refs) -> None:
    assert len(refs) >= 80, f"juda kam ManimRef: {len(refs)}"


def test_every_module_file_exists(refs) -> None:
    missing = sorted({m for _, m, _ in refs if not (ROOT / m).exists()})
    assert not missing, f"yo'q fayllar: {missing}"


def test_every_scene_class_exists(refs) -> None:
    cache: dict[str, set[str]] = {}
    bad = []
    for tid, module, scene in refs:
        if module not in cache:
            tree = ast.parse((ROOT / module).read_text(encoding="utf-8"))
            cache[module] = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
        if scene not in cache[module]:
            bad.append(f"{tid}: {scene} -> {module}")
    assert not bad, f"yo'q sinflar: {bad}"


def test_every_scene_has_construct(refs) -> None:
    bad = []
    for tid, module, scene in refs:
        tree = ast.parse((ROOT / module).read_text(encoding="utf-8"))
        for n in tree.body:
            if isinstance(n, ast.ClassDef) and n.name == scene:
                if not any(isinstance(f, ast.FunctionDef) and f.name == "construct"
                           for f in n.body):
                    bad.append(f"{tid}: {scene}")
    assert not bad, f"construct() yo'q: {bad}"


def test_scene_files_are_valid_python() -> None:
    for p in sorted((ROOT / "animatsiya" / "scenes").glob("*.py")):
        ast.parse(p.read_text(encoding="utf-8"), filename=str(p))


def test_no_local_package_shadows_manim() -> None:
    """Loyiha ildizida 'manim' nomli katalog bo'lmasligi kerak.

    Aks holda u haqiqiy manim paketini soya qiladi va sahnalarni
    ildizdan ishga tushirib bo'lmaydi.
    """
    assert not (ROOT / "manim").exists(), \
        "ildizdagi 'manim/' katalogi haqiqiy paketni soya qiladi"

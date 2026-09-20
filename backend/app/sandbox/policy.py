"""Foydalanuvchi kodining STATIK tekshiruvi (birinchi himoya qatlami).

Bu modul kodni BAJARMAYDI — faqat AST sifatida tahlil qiladi va xavfli
konstruksiyalarni bajarishdan OLDIN rad etadi. Ikkinchi qatlam —
`executor.py` dagi izolyatsiyalangan jarayon va resurs cheklovlari.

Muhim: bu qatlamning o'zi YETARLI EMAS. AST filtri chetlab o'tilishi
mumkin bo'lgan usullar ma'lum, shuning uchun u hech qachon yagona
himoya sifatida ishlatilmaydi — u faqat oddiy xatolarni erta va
tushunarli xabar bilan qaytarish uchun xizmat qiladi.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

#: Ruxsat etilgan modullar (submodullari bilan).
ALLOWED_ROOTS: frozenset[str] = frozenset({
    "labkit", "math", "cmath", "statistics", "fractions", "decimal",
    "itertools", "functools", "operator", "random", "numpy", "scipy",
    "sympy", "collections", "heapq", "bisect", "copy", "typing",
})

#: Umuman ruxsat etilmaydigan nomlar.
FORBIDDEN_NAMES: frozenset[str] = frozenset({
    "eval", "exec", "compile", "open", "input", "breakpoint",
    "__import__", "globals", "locals", "vars", "dir",
    # hasattr() FAQAT bool qaytaradi va obyektga havola bermaydi,
    # shuning uchun u ruxsat etiladi; getattr/setattr/delattr esa
    # ixtiyoriy nom bo'yicha obyekt olishga imkon bergani uchun yopiq.
    "getattr", "setattr", "delattr",
    "memoryview", "help", "exit", "quit", "license", "credits",
})

#: Kod hajmi va murakkabligi chegaralari.
MAX_CHARS = 60_000
MAX_LINES = 1_500
MAX_NODES = 40_000


class PolicyError(ValueError):
    """Kod siyosatni buzdi. Xabar foydalanuvchiga ko'rsatiladi."""


@dataclass(frozen=True)
class PolicyReport:
    ok: bool
    reason: str = ""
    line: int = 0


def _root(name: str) -> str:
    return name.split(".", 1)[0]


class _Validator(ast.NodeVisitor):
    def __init__(self) -> None:
        self.nodes = 0

    def generic_visit(self, node: ast.AST) -> None:
        self.nodes += 1
        if self.nodes > MAX_NODES:
            raise PolicyError(
                f"Kod juda murakkab: {MAX_NODES} dan ortiq AST tuguni")
        super().generic_visit(node)

    # --- import ---------------------------------------------------------
    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            if _root(alias.name) not in ALLOWED_ROOTS:
                raise PolicyError(
                    f"{node.lineno}-qator: '{alias.name}' modulini import "
                    f"qilish taqiqlangan. Ruxsat etilganlar: "
                    f"{', '.join(sorted(ALLOWED_ROOTS))}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.level:
            raise PolicyError(
                f"{node.lineno}-qator: nisbiy import taqiqlangan")
        if node.module is None or _root(node.module) not in ALLOWED_ROOTS:
            raise PolicyError(
                f"{node.lineno}-qator: '{node.module}' modulidan import "
                f"qilish taqiqlangan")
        self.generic_visit(node)

    # --- xavfli nomlar ---------------------------------------------------
    def visit_Name(self, node: ast.Name) -> None:
        if node.id in FORBIDDEN_NAMES:
            raise PolicyError(
                f"{node.lineno}-qator: '{node.id}' ishlatish taqiqlangan")
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        # dunder atributlar orqali sandbox'dan chiqish urinishlari
        if node.attr.startswith("__") and node.attr.endswith("__"):
            raise PolicyError(
                f"{node.lineno}-qator: '{node.attr}' kabi maxsus "
                f"atributlarga murojaat taqiqlangan")
        if node.attr in FORBIDDEN_NAMES:
            raise PolicyError(
                f"{node.lineno}-qator: '.{node.attr}' taqiqlangan")
        self.generic_visit(node)

    # --- yozishga urinish -------------------------------------------------
    def visit_Global(self, node: ast.Global) -> None:
        raise PolicyError(f"{node.lineno}-qator: 'global' taqiqlangan")

    def visit_Nonlocal(self, node: ast.Nonlocal) -> None:
        raise PolicyError(f"{node.lineno}-qator: 'nonlocal' taqiqlangan")


def check(code: str) -> PolicyReport:
    """Kodni tekshiradi. Bajarmaydi."""
    if not code or not code.strip():
        return PolicyReport(False, "Kod bo'sh")
    if len(code) > MAX_CHARS:
        return PolicyReport(
            False, f"Kod juda uzun: {len(code)} > {MAX_CHARS} belgi")
    n_lines = code.count("\n") + 1
    if n_lines > MAX_LINES:
        return PolicyReport(
            False, f"Kod juda uzun: {n_lines} > {MAX_LINES} qator")
    try:
        tree = ast.parse(code, mode="exec")
    except SyntaxError as exc:
        return PolicyReport(
            False, f"Sintaksis xatosi: {exc.msg}", exc.lineno or 0)
    try:
        _Validator().visit(tree)
    except PolicyError as exc:
        return PolicyReport(False, str(exc))
    return PolicyReport(True)

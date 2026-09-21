"""Chizma spetsifikatsiyalarini yozish uchun ixcham yordamchilar.

Alohida modul: fan fayllari bundan import qiladi, paket `__init__`
esa fan fayllarini yig'adi — shunda aylanma import bo'lmaydi.
"""

from __future__ import annotations

from content.curriculum.schema import Figure, FigureCurve, FigureParam, FigureReadout

__all__ = ["fig", "fp", "fc", "fr"]


def fp(key: str, label: str, lo: float, hi: float, default: float,
       step: float, unit: str = "") -> FigureParam:
    """Surgich."""
    return FigureParam(key=key, label=label, minimum=lo, maximum=hi,
                       default=default, step=step, unit=unit)


def fc(label: str, expr: str, color: str = "tension", *,
       dashed: bool = False, when: str = "") -> FigureCurve:
    """Egri chiziq y = f(x)."""
    return FigureCurve(label=label, expr=expr, color=color,  # type: ignore[arg-type]
                       dashed=dashed, when=when)


def fr(label: str, expr: str, unit: str = "", color: str = "ink",
       text: str = "") -> FigureReadout:
    """Chizma ostidagi hisoblangan qiymat."""
    return FigureReadout(label=label, expr=expr, unit=unit,
                         color=color, text=text)  # type: ignore[arg-type]


def fig(title: str, caption: str, *, params=(), curves=(), readouts=(),
        x=("x", "y"), x_min: str = "0", x_max: str = "1",
        kind: str = "plot", options=None, note: str = "") -> Figure:
    """Chizma spetsifikatsiyasi. `x` — (x o'qi nomi, y o'qi nomi)."""
    return Figure(
        kind=kind,  # type: ignore[arg-type]
        title=title, caption=caption,
        params=list(params), curves=list(curves), readouts=list(readouts),
        x_label=x[0], y_label=x[1], x_min=x_min, x_max=x_max,
        options=dict(options or {}), note=note,
    )

"""`labkit` — sandbox ichidagi kod foydalanadigan YAGONA chiqish kanali.

Foydalanuvchi kodi natijani `print()` bilan emas, shu modul orqali
qaytaradi. Bu ataylab shunday: chiqish tuzilgan (structured) bo'ladi,
turlari tekshiriladi va hajmi cheklanadi, ya'ni frontend har doim
bashorat qilinadigan JSON oladi.

API (mavzu kodlari shunga tayanadi):
    from labkit import PARAMS, note, series, table, value
"""

from __future__ import annotations

import math
from typing import Any

#: Interactive Lab'dan kelgan parametrlar; `executor` to'ldiradi.
PARAMS: dict[str, float] = {}

#: Chiqish hajmi chegaralari — cheksiz natija bilan xotirani to'ldirishga yo'l qo'ymaydi.
MAX_VALUES = 120
MAX_NOTES = 40
MAX_SERIES = 40
MAX_TABLES = 20
MAX_POINTS = 5_000
MAX_ROWS = 400
MAX_COLS = 12
MAX_TEXT = 4_000

_values: list[dict[str, Any]] = []
_notes: list[str] = []
_series: list[dict[str, Any]] = []
_tables: list[dict[str, Any]] = []


class LabError(ValueError):
    """labkit noto'g'ri ishlatildi — xabar foydalanuvchiga ko'rsatiladi."""


def _reset(params: dict[str, float] | None = None) -> None:
    """Faqat executor chaqiradi."""
    global PARAMS
    PARAMS = dict(params or {})
    _values.clear()
    _notes.clear()
    _series.clear()
    _tables.clear()


def _finite(x: Any, where: str) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError) as exc:
        raise LabError(f"{where}: son kutilgan, '{type(x).__name__}' keldi") from exc
    if math.isnan(v) or math.isinf(v):
        raise LabError(f"{where}: chekli son emas ({x!r})")
    return v


def value(label: str, val: Any, unit: str = "") -> None:
    """Bitta skalyar natija."""
    if not isinstance(label, str) or not label.strip():
        raise LabError("value(): label bo'sh bo'lmagan satr bo'lishi kerak")
    if len(_values) >= MAX_VALUES:
        raise LabError(f"value(): {MAX_VALUES} tadan ortiq qiymat berib bo'lmaydi")
    _values.append({
        "label": label[:200],
        "value": _finite(val, f"value({label!r})"),
        "unit": str(unit)[:40],
    })


def note(text: str) -> None:
    """Natijani izohlovchi matn."""
    if not isinstance(text, str) or not text.strip():
        raise LabError("note(): matn bo'sh bo'lmasligi kerak")
    if len(_notes) >= MAX_NOTES:
        raise LabError(f"note(): {MAX_NOTES} tadan ortiq izoh berib bo'lmaydi")
    _notes.append(text[:MAX_TEXT])


def series(label: str, x: Any, y: Any, xlabel: str = "", ylabel: str = "") -> None:
    """Grafik uchun (x, y) juftliklari."""
    if not isinstance(label, str) or not label.strip():
        raise LabError("series(): label bo'sh bo'lmagan satr bo'lishi kerak")
    if len(_series) >= MAX_SERIES:
        raise LabError(f"series(): {MAX_SERIES} tadan ortiq seriya berib bo'lmaydi")
    xs, ys = list(x), list(y)
    if len(xs) != len(ys):
        raise LabError(
            f"series({label!r}): x va y uzunligi mos emas ({len(xs)} va {len(ys)})")
    if not xs:
        raise LabError(f"series({label!r}): kamida bitta nuqta kerak")
    if len(xs) > MAX_POINTS:
        raise LabError(
            f"series({label!r}): {len(xs)} nuqta, ruxsat etilgani {MAX_POINTS}")
    _series.append({
        "label": label[:200],
        "x": [_finite(v, f"series({label!r}).x") for v in xs],
        "y": [_finite(v, f"series({label!r}).y") for v in ys],
        "xlabel": str(xlabel)[:120],
        "ylabel": str(ylabel)[:120],
    })


def table(title: str, headers: Any, rows: Any) -> None:
    """Jadval: sarlavhalar va satrlar."""
    if not isinstance(title, str) or not title.strip():
        raise LabError("table(): sarlavha bo'sh bo'lmasligi kerak")
    if len(_tables) >= MAX_TABLES:
        raise LabError(f"table(): {MAX_TABLES} tadan ortiq jadval berib bo'lmaydi")
    hs = [str(h)[:120] for h in headers]
    if not hs:
        raise LabError(f"table({title!r}): sarlavhalar bo'sh")
    if len(hs) > MAX_COLS:
        raise LabError(f"table({title!r}): {len(hs)} ustun, ruxsat {MAX_COLS}")
    out: list[list[str]] = []
    for i, row in enumerate(rows):
        cells = list(row)
        if len(cells) != len(hs):
            raise LabError(
                f"table({title!r}): {i}-satrda {len(cells)} katak, "
                f"{len(hs)} kutilgan")
        out.append([str(c)[:200] for c in cells])
        if len(out) > MAX_ROWS:
            raise LabError(f"table({title!r}): {MAX_ROWS} dan ortiq satr")
    if not out:
        raise LabError(f"table({title!r}): birorta satr yo'q")
    _tables.append({"title": title[:200], "headers": hs, "rows": out})


def _collect() -> dict[str, Any]:
    """Faqat executor chaqiradi."""
    return {
        "values": list(_values),
        "notes": list(_notes),
        "series": list(_series),
        "tables": list(_tables),
    }

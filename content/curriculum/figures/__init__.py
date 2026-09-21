"""Har bir mavzu uchun interaktiv chizma spetsifikatsiyalari.

Chizmalar dars matnidan ALOHIDA saqlanadi: shunda dars fayllari
o'qilishi oson qoladi va chizmalarni bir joyda ko'rib chiqish mumkin.
`registry.all_topics()` ularni mavzularga biriktiradi.

Qoida: har bir mavzuda KAMIDA IKKITA chizma bo'lishi shart —
buni `audit.py` tekshiradi.
"""

from __future__ import annotations

from content.curriculum.figures.base import fc, fig, fp, fr  # noqa: F401
from content.curriculum.schema import Figure

from content.curriculum.figures import materiallar_qarshiligi as _mq
from content.curriculum.figures import nazariy_mexanika as _nm
from content.curriculum.figures import plastinalar_qobiqlar as _pq
from content.curriculum.figures import sonli_usullar as _su
from content.curriculum.figures import tutash_muhitlar as _tmm

__all__ = ["FIGURES", "fig", "fp", "fc", "fr"]

#: mavzu id → chizmalar ro'yxati
FIGURES: dict[str, list[Figure]] = {}
for _mod in (_nm, _mq, _tmm, _pq, _su):
    FIGURES.update(_mod.FIGURES)

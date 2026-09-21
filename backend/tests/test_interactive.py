"""Interaktiv chizmalar: har bir fanda kamida ikkitadan bo'lishi kerak.

Registry frontend'da (TypeScript) yashaydi, shuning uchun uni matn
sifatida o'qiymiz. Maqsad — mavzu id i o'zgarganda chizma jimgina
yo'qolib qolmasligi.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "frontend" / "src" / "interactive" / "registry.ts"
CURRICULUM = ROOT / "content" / "generated" / "curriculum.json"

PREFIX = {"nazariy-mexanika": "nm-", "materiallar-qarshiligi": "mq-",
          "tutash-muhitlar": "tmm-", "plastinalar-qobiqlar": "pq-",
          "sonli-usullar": "su-"}
MIN_PER_SUBJECT = 2


@pytest.fixture(scope="module")
def keys() -> list[str]:
    src = REGISTRY.read_text(encoding="utf-8")
    body = src.split("export const INTERACTIVE", 1)[1]
    body = body.split("export function", 1)[0]
    return re.findall(r'"([a-z]+-\d{2})"\s*:\s*\{', body)


@pytest.fixture(scope="module")
def topic_ids() -> set[str]:
    data = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    return {t["id"] for t in data["topics"]}


def test_registry_file_exists() -> None:
    assert REGISTRY.exists(), "interactive/registry.ts topilmadi"


def test_keys_are_real_topics(keys, topic_ids) -> None:
    bad = sorted(set(keys) - topic_ids)
    assert not bad, f"mavjud bo'lmagan mavzu id lari: {bad}"


def test_no_duplicate_keys(keys) -> None:
    assert len(keys) == len(set(keys)), "registry'da takroriy kalit bor"


def test_at_least_two_per_subject(keys) -> None:
    counts = {sid: sum(1 for k in keys if k.startswith(pref))
              for sid, pref in PREFIX.items()}
    low = {s: c for s, c in counts.items() if c < MIN_PER_SUBJECT}
    assert not low, f"bu fanlarda {MIN_PER_SUBJECT} tadan kam chizma bor: {low}"


def test_every_component_is_imported() -> None:
    """Registry'dagi har bir komponent haqiqatan import qilinganmi?"""
    src = REGISTRY.read_text(encoding="utf-8")
    imported = set(re.findall(r"import\s*\{([^}]+)\}\s*from\s*\"\./(?:nm|mq|tmm|pq|su)\"", src))
    names: set[str] = set()
    for group in imported:
        names |= {x.strip() for x in group.split(",") if x.strip()}
    # Faqat HAQIQIY yozuvlardagi komponentlar: "nm-01": { ..., Component: X }
    # (tur e'lonidagi `Component: ComponentType` hisobga olinmaydi)
    used = set(re.findall(r'"[a-z]+-\d{2}"\s*:\s*\{[^}]*Component:\s*(\w+)', src))
    missing = sorted(used - names)
    assert not missing, f"import qilinmagan komponentlar: {missing}"


def test_component_files_exist() -> None:
    d = ROOT / "frontend" / "src" / "interactive"
    for name in ("ui.tsx", "nm.tsx", "mq.tsx", "tmm.tsx", "pq.tsx", "su.tsx"):
        assert (d / name).exists(), f"{name} topilmadi"

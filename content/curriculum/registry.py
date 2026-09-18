"""Barcha fanlarni yig'uvchi reyestr va qulay qidiruv funksiyalari."""

from __future__ import annotations

from functools import lru_cache

from content.curriculum.projects import PROJECTS
from content.curriculum.schema import FinalProject, Module, Subject, Topic
from content.curriculum.subjects.materiallar_qarshiligi import SUBJECT as _S2
from content.curriculum.subjects.nazariy_mexanika import SUBJECT as _S1
from content.curriculum.subjects.plastinalar_qobiqlar import SUBJECT as _S4
from content.curriculum.subjects.sonli_usullar import SUBJECT as _S5
from content.curriculum.subjects.tutash_muhitlar import SUBJECT as _S3

#: Fanlar pedagogik zanjir tartibida (2-talab).
SUBJECTS: list[Subject] = [_S1, _S2, _S3, _S4, _S5]


@lru_cache(maxsize=1)
def all_topics() -> tuple[Topic, ...]:
    """Barcha mavzular global tartibda (fan tartibi → mavzu tartibi)."""
    return tuple(t for s in SUBJECTS for t in s.topics)


@lru_cache(maxsize=1)
def topic_index() -> dict[str, Topic]:
    return {t.id: t for t in all_topics()}


@lru_cache(maxsize=1)
def global_order() -> dict[str, int]:
    """Mavzu id → global ketma-ket raqam (prerequisite tekshiruvi uchun)."""
    return {t.id: i for i, t in enumerate(all_topics())}


@lru_cache(maxsize=1)
def module_index() -> dict[str, Module]:
    return {m.id: m for s in SUBJECTS for m in s.modules}


def subject_index() -> dict[str, Subject]:
    return {s.id: s for s in SUBJECTS}


def get_subject(subject_id: str) -> Subject | None:
    return subject_index().get(subject_id)


def get_topic(topic_id: str) -> Topic | None:
    return topic_index().get(topic_id)


def get_project(project_id: str) -> FinalProject | None:
    return {p.id: p for p in PROJECTS}.get(project_id)


def topics_of_module(module_id: str) -> list[Topic]:
    return [t for t in all_topics() if t.module_id == module_id]


def dependency_edges() -> list[tuple[str, str]]:
    """(prerequisite_id, topic_id) juftliklari — dependency graph qirralari."""
    return [(pre, t.id) for t in all_topics() for pre in t.prerequisites]


def search(query: str, limit: int = 30) -> list[Topic]:
    """Mavzu nomi, tavsifi va teglari bo'yicha sodda qidiruv."""
    q = query.casefold().strip()
    if not q:
        return []
    scored: list[tuple[int, Topic]] = []
    for t in all_topics():
        score = 0
        if q in t.title.casefold():
            score += 10
        if q in t.description.casefold():
            score += 4
        if any(q in tag.casefold() for tag in t.tags):
            score += 6
        if q in t.mathematical_core.casefold() or q in t.engineering_application.casefold():
            score += 2
        if q == t.id.casefold():
            score += 20
        if score:
            scored.append((score, t))
    scored.sort(key=lambda pair: (-pair[0], global_order()[pair[1].id]))
    return [t for _, t in scored[:limit]]

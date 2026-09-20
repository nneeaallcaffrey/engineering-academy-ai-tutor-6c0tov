"""Kurikulum JSON'ini bazaga yuklash.

Backend kontentni Python modullaridan EMAS, faqat eksport qilingan
JSON'dan oladi. Bu ataylab: backend'ning ishlashi kurikulum kodiga
bog'liq bo'lmaydi va konteynerga faqat bitta fayl ko'chiriladi.
"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import Base, engine
from app.models import Meta, Module, Project, Resource, Subject, Topic

log = logging.getLogger(__name__)

SEED_KEY = "curriculum_sha256"


class CurriculumMissingError(RuntimeError):
    """Kurikulum JSON topilmadi — backend ishlay olmaydi."""


def load_payload(path: Path | None = None) -> dict[str, Any]:
    settings = get_settings()
    p = Path(path or settings.curriculum_json)
    if not p.exists():
        raise CurriculumMissingError(
            f"Kurikulum fayli topilmadi: {p}\n"
            f"Uni yaratish uchun loyiha ildizida quyidagini bajaring:\n"
            f"    python -m content.curriculum.export")
    return json.loads(p.read_text(encoding="utf-8"))


def _digest(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def seed(db: Session, payload: dict[str, Any], *, force: bool = False) -> bool:
    """Bazani to'ldiradi. O'zgarish bo'lmasa hech narsa qilmaydi."""
    digest = _digest(payload)
    current = db.get(Meta, SEED_KEY)
    if current is not None and current.value == digest and not force:
        log.info("Kurikulum o'zgarmagan (%s), seed o'tkazib yuborildi", digest[:12])
        return False

    for model in (Topic, Module, Resource, Project, Subject):
        db.query(model).delete()

    global_order = 0
    for s in payload["subjects"]:
        db.add(Subject(
            id=s["id"], code=s["code"], order=s["order"], title=s["title"],
            tagline=s.get("tagline", ""), description=s.get("description", ""),
            payload={k: v for k, v in s.items()
                     if k not in ("modules", "resources")},
        ))
        for m in s.get("modules", []):
            db.add(Module(
                id=m["id"], subject_id=s["id"], order=m["order"],
                title=m["title"], summary=m.get("summary", ""),
                outcome=m.get("outcome", ""),
            ))
        seen: set[str] = set()
        for r in s.get("resources", []):
            if r["title"] in seen:            # bir fanda takror manba
                continue
            seen.add(r["title"])
            db.add(Resource(
                subject_id=s["id"], title=r["title"], author=r.get("author", ""),
                year=str(r.get("year", "")), kind=r.get("kind", "asosiy"),
                note=r.get("note", ""),
            ))

    # Mavzular JSON ning ILDIZIDA, fanlar ichida emas: ular global
    # pedagogik tartibda berilgan va shu tartib saqlanadi.
    for t in payload["topics"]:
        db.add(Topic(
            id=t["id"], subject_id=t["subject_id"], module_id=t["module_id"],
            order=t["order"], global_order=global_order, title=t["title"],
            description=t.get("description", ""),
            difficulty=t.get("difficulty", "asosiy"),
            estimated_minutes=t.get("estimated_minutes", 90),
            next_topic=t.get("next_topic"),
            prerequisites=t.get("prerequisites", []),
            tags=t.get("tags", []), payload=t,
        ))
        global_order += 1

    for pr in payload.get("projects", []):
        db.add(Project(id=pr["id"], subject_id=pr["subject_id"],
                       title=pr["title"], payload=pr))

    db.merge(Meta(key=SEED_KEY, value=digest))
    db.merge(Meta(key="counts",
                  value=json.dumps(payload.get("meta", {}).get("counts", {}))))
    db.merge(Meta(key="graph", value=json.dumps(payload.get("graph", {}))))
    db.merge(Meta(key="audit", value=json.dumps(payload.get("audit", {}))))
    db.commit()
    log.info("Kurikulum yuklandi: %d mavzu", global_order)
    return True


def init_db(db: Session, *, force: bool = False) -> bool:
    Base.metadata.create_all(engine)
    return seed(db, load_payload(), force=force)


def is_seeded(db: Session) -> bool:
    return db.scalar(select(Meta).where(Meta.key == SEED_KEY)) is not None

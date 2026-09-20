"""Fanlar."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Module, Subject, Topic
from app.schemas import SubjectBrief, SubjectDetail, TopicBrief

router = APIRouter(prefix="/api/subjects", tags=["Fanlar"])


def _brief(t: Topic) -> TopicBrief:
    return TopicBrief(
        id=t.id, subject_id=t.subject_id, module_id=t.module_id, order=t.order,
        global_order=t.global_order, title=t.title, description=t.description,
        learning_objective=(t.payload or {}).get("learning_objective", ""),
        difficulty=t.difficulty, estimated_minutes=t.estimated_minutes,
        prerequisites=t.prerequisites or [], tags=t.tags or [],
        next_topic=t.next_topic,
        has_lab=bool(t.payload.get("lesson", {})
                     .get("computation", {}).get("parameters")),
    )


@router.get("", response_model=list[SubjectBrief], summary="Barcha fanlar")
def list_subjects(db: Session = Depends(get_db)) -> list[SubjectBrief]:
    rows = db.scalars(select(Subject).order_by(Subject.order)).all()
    counts = {s.id: db.query(Topic).filter(Topic.subject_id == s.id).count()
              for s in rows}
    return [
        SubjectBrief(
            id=s.id, code=s.code, order=s.order, title=s.title,
            tagline=s.tagline, topic_count=counts[s.id],
            accent=(s.payload or {}).get("accent", ""),
        ) for s in rows
    ]


@router.get("/{subject_id}", response_model=SubjectDetail,
            summary="Bitta fan: modullar, mavzular, baholash")
def get_subject(subject_id: str, db: Session = Depends(get_db)) -> SubjectDetail:
    s = db.get(Subject, subject_id)
    if s is None:
        raise HTTPException(404, f"'{subject_id}' fani topilmadi")
    topics = db.scalars(
        select(Topic).where(Topic.subject_id == subject_id)
        .order_by(Topic.order)).all()
    modules = db.scalars(
        select(Module).where(Module.subject_id == subject_id)
        .order_by(Module.order)).all()
    p = s.payload or {}
    return SubjectDetail(
        id=s.id, code=s.code, order=s.order, title=s.title, tagline=s.tagline,
        description=s.description, goal=p.get("goal", ""),
        topic_count=len(topics), accent=p.get("accent", ""),
        modules=[{"id": m.id, "order": m.order, "title": m.title,
                  "summary": m.summary, "outcome": m.outcome} for m in modules],
        assessments=p.get("assessments", []),
        topics=[_brief(t) for t in topics],
    )

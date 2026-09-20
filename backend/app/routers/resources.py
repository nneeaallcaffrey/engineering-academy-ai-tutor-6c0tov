"""Adabiyotlar va manbalar."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Resource

router = APIRouter(prefix="/api/resources", tags=["Manbalar"])


@router.get("", summary="Manbalar ro'yxati")
def list_resources(subject_id: str | None = None, kind: str | None = None,
                   db: Session = Depends(get_db)) -> list[dict[str, Any]]:
    stmt = select(Resource)
    if subject_id:
        stmt = stmt.where(Resource.subject_id == subject_id)
    if kind:
        stmt = stmt.where(Resource.kind == kind)
    rows = db.scalars(stmt.order_by(Resource.subject_id, Resource.title)).all()
    return [
        {"id": r.id, "subject_id": r.subject_id, "title": r.title,
         "author": r.author, "year": r.year, "kind": r.kind, "note": r.note}
        for r in rows
    ]

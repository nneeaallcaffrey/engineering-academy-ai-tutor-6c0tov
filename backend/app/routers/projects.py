"""Yakuniy loyihalar."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project

router = APIRouter(prefix="/api/projects", tags=["Loyihalar"])


@router.get("", summary="Barcha yakuniy loyihalar")
def list_projects(subject_id: str | None = None,
                  db: Session = Depends(get_db)) -> list[dict[str, Any]]:
    stmt = select(Project)
    if subject_id:
        stmt = stmt.where(Project.subject_id == subject_id)
    return [p.payload for p in db.scalars(stmt).all()]


@router.get("/{project_id}", summary="Bitta loyiha")
def get_project(project_id: str, db: Session = Depends(get_db)) -> dict[str, Any]:
    p = db.get(Project, project_id)
    if p is None:
        raise HTTPException(404, f"'{project_id}' loyihasi topilmadi")
    return p.payload

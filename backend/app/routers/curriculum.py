"""Kurikulum: bog'liqlik grafi va akademik audit."""

from __future__ import annotations

import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Meta, Topic
from app.schemas import AuditCheck, AuditResponse, GraphEdge, GraphNode, GraphResponse

router = APIRouter(prefix="/api/curriculum", tags=["Kurikulum"])


@router.get("/graph", response_model=GraphResponse,
            summary="Mavzular bog'liqlik grafi")
def get_graph(subject_id: str | None = None,
              db: Session = Depends(get_db)) -> GraphResponse:
    """Prerequisite havolalaridan yo'naltirilgan graf quradi."""
    topics = db.scalars(select(Topic).order_by(Topic.global_order)).all()
    known = {t.id for t in topics}
    keep = {t.id for t in topics
            if subject_id is None or t.subject_id == subject_id}
    nodes = [
        GraphNode(id=t.id, title=t.title, subject_id=t.subject_id,
                  module_id=t.module_id, order=t.global_order,
                  difficulty=t.difficulty)
        for t in topics if t.id in keep
    ]
    edges: list[GraphEdge] = []
    for t in topics:
        if t.id not in keep:
            continue
        for dep in (t.prerequisites or []):
            # Fan bo'yicha filtrlashda tashqi bog'lanish tushib qolmasligi
            # uchun manba tugunini ham qo'shamiz.
            if dep not in known:
                continue
            if dep not in keep:
                src = next(x for x in topics if x.id == dep)
                nodes.append(GraphNode(
                    id=src.id, title=src.title, subject_id=src.subject_id,
                    module_id=src.module_id, order=src.global_order,
                    difficulty=src.difficulty))
                keep.add(dep)
            edges.append(GraphEdge(source=dep, target=t.id))
    return GraphResponse(nodes=nodes, edges=edges)


@router.get("/audit", response_model=AuditResponse,
            summary="Akademik audit natijasi")
def get_audit(db: Session = Depends(get_db)) -> AuditResponse:
    row = db.get(Meta, "audit")
    if row is None:
        raise HTTPException(503, "Audit natijasi hali yuklanmagan")
    data = json.loads(row.value)
    counts_row = db.get(Meta, "counts")
    checks = [
        AuditCheck(
            key=c.get("key", ""), question=c.get("question", ""),
            passed=bool(c.get("passed")), detail=c.get("detail", ""),
            offenders=c.get("offenders", []) or [],
        ) for c in data.get("checks", [])
    ]
    return AuditResponse(
        passed=bool(data.get("passed", all(c.passed for c in checks))),
        checks=checks,
        counts=json.loads(counts_row.value) if counts_row else {},
    )

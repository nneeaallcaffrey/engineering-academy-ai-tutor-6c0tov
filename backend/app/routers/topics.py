"""Mavzular va Interactive Lab."""

from __future__ import annotations

import hashlib
import time
from collections import defaultdict, deque

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.models import LabRun, Subject, Topic
from app.routers.subjects import _brief
from app.sandbox.executor import RunLimits, run_code
from app.schemas import LabParameterOut, RunRequest, RunResponse, TopicBrief, TopicDetail

router = APIRouter(prefix="/api/topics", tags=["Mavzular"])

#: IP -> so'nggi ishga tushirish vaqtlari (oddiy tezlik chegarasi).
_hits: dict[str, deque[float]] = defaultdict(deque)


def _rate_limit(request: Request) -> None:
    limit = get_settings().lab_rate_per_minute
    ip = (request.client.host if request.client else "?") or "?"
    now = time.monotonic()
    q = _hits[ip]
    while q and now - q[0] > 60.0:
        q.popleft()
    if len(q) >= limit:
        raise HTTPException(
            429, f"Juda ko'p so'rov: daqiqasiga {limit} tadan ko'p kod "
                 f"ishga tushirib bo'lmaydi. Biroz kutib qayta urining.")
    q.append(now)


@router.get("", response_model=list[TopicBrief], summary="Mavzular ro'yxati")
def list_topics(
    subject_id: str | None = None,
    module_id: str | None = None,
    q: str | None = Query(None, description="Sarlavha va tavsif bo'yicha qidiruv"),
    limit: int = Query(200, ge=1, le=300),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[TopicBrief]:
    stmt = select(Topic)
    if subject_id:
        stmt = stmt.where(Topic.subject_id == subject_id)
    if module_id:
        stmt = stmt.where(Topic.module_id == module_id)
    if q:
        like = f"%{q.strip()}%"
        stmt = stmt.where(or_(Topic.title.ilike(like),
                              Topic.description.ilike(like)))
    stmt = stmt.order_by(Topic.global_order).offset(offset).limit(limit)
    return [_brief(t) for t in db.scalars(stmt).all()]


@router.get("/{topic_id}", response_model=TopicDetail, summary="Bitta mavzu")
def get_topic(topic_id: str, db: Session = Depends(get_db)) -> TopicDetail:
    t = db.get(Topic, topic_id)
    if t is None:
        raise HTTPException(404, f"'{topic_id}' mavzusi topilmadi")
    p = t.payload
    subject = db.get(Subject, t.subject_id)
    prev = db.scalar(
        select(Topic.id).where(Topic.global_order == t.global_order - 1))
    base = _brief(t)
    return TopicDetail(
        **base.model_dump(),
        lesson=p.get("lesson", {}),
        mathematical_core=p.get("mathematical_core", ""),
        engineering_application=p.get("engineering_application", ""),
        computational_component=p.get("computational_component", ""),
        visualization_component=p.get("visualization_component", ""),
        research_extension=p.get("research_extension", ""),
        previous_link=p.get("previous_link", ""),
        subject_title=subject.title if subject else "",
        prev_topic=prev,
    )


@router.get("/{topic_id}/lab", response_model=list[LabParameterOut],
            summary="Laboratoriya parametrlari")
def get_lab_params(topic_id: str,
                   db: Session = Depends(get_db)) -> list[LabParameterOut]:
    t = db.get(Topic, topic_id)
    if t is None:
        raise HTTPException(404, f"'{topic_id}' mavzusi topilmadi")
    comp = t.payload.get("lesson", {}).get("computation", {})
    return [LabParameterOut(**p) for p in comp.get("parameters", [])]


@router.post("/{topic_id}/run", response_model=RunResponse,
             summary="Kodni sandbox'da bajarish")
def run_topic_code(topic_id: str, body: RunRequest, request: Request,
                   db: Session = Depends(get_db)) -> RunResponse:
    """Kodni IZOLYATSIYALANGAN jarayonda bajaradi.

    Kod asosiy jarayonda hech qachon `exec()` qilinmaydi — batafsil
    `app/sandbox/executor.py` ga qarang.
    """
    t = db.get(Topic, topic_id)
    if t is None:
        raise HTTPException(404, f"'{topic_id}' mavzusi topilmadi")
    _rate_limit(request)

    comp = t.payload.get("lesson", {}).get("computation", {})
    code = body.code if (body.code and body.code.strip()) else comp.get("code", "")
    if not code.strip():
        raise HTTPException(400, "Bajariladigan kod yo'q")

    allowed = {p["key"] for p in comp.get("parameters", [])}
    params = {k: v for k, v in body.params.items() if k in allowed}

    s = get_settings()
    result = run_code(code, params, RunLimits(
        wall_seconds=s.lab_wall_seconds, cpu_seconds=s.lab_cpu_seconds,
        memory_mb=s.lab_memory_mb))

    # Jurnal: kodning O'ZI saqlanmaydi, faqat xesh va uzunlik.
    db.add(LabRun(
        topic_id=topic_id, ok=result.ok, duration_ms=result.duration_ms,
        error_type=result.error_type,
        code_sha256=hashlib.sha256(code.encode()).hexdigest(),
        code_length=len(code),
    ))
    db.commit()
    return RunResponse(**result.as_dict())

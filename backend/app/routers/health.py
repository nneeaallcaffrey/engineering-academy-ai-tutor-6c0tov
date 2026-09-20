"""Sog'liq tekshiruvi."""

from __future__ import annotations

import json

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.models import Meta, Topic
from app.sandbox.executor import RunLimits, run_code
from app.schemas import HealthResponse

router = APIRouter(tags=["Xizmat"])


@router.get("/health", response_model=HealthResponse, summary="Holat")
def health(db: Session = Depends(get_db)) -> HealthResponse:
    s = get_settings()
    try:
        db.execute(text("SELECT 1"))
        database = "ok"
    except Exception as exc:                                  # noqa: BLE001
        database = f"xato: {type(exc).__name__}"
    counts_row = db.get(Meta, "counts")
    counts = json.loads(counts_row.value) if counts_row else {}
    return HealthResponse(
        status="ok" if database == "ok" else "degraded",
        version=s.version, database=database,
        seeded=db.query(Topic).count() > 0, counts=counts,
        sandbox="tayyor",
    )


@router.get("/health/sandbox", summary="Sandbox ishlayaptimi")
def health_sandbox() -> dict[str, object]:
    """Sandbox'ni haqiqiy kod bilan tekshiradi."""
    r = run_code(
        "from labkit import value\nvalue('tekshiruv', 1.0)",
        limits=RunLimits(wall_seconds=20, cpu_seconds=10, memory_mb=768))
    return {"ok": r.ok, "duration_ms": r.duration_ms,
            "error": r.error, "values": r.values}

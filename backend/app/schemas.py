"""API javob va so'rov modellari."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class SubjectBrief(BaseModel):
    id: str
    code: str
    order: int
    title: str
    tagline: str = ""
    topic_count: int = 0
    accent: str = ""


class SubjectDetail(SubjectBrief):
    description: str = ""
    goal: str = ""
    modules: list[dict[str, Any]] = Field(default_factory=list)
    assessments: list[dict[str, Any]] = Field(default_factory=list)
    topics: list["TopicBrief"] = Field(default_factory=list)


class TopicBrief(BaseModel):
    id: str
    subject_id: str
    module_id: str
    order: int
    global_order: int
    title: str
    description: str = ""
    learning_objective: str = ""
    difficulty: str = "asosiy"
    estimated_minutes: int = 90
    prerequisites: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    next_topic: str | None = None
    has_lab: bool = False


class TopicDetail(TopicBrief):
    #: 18 bo'limli darsning to'liq mazmuni (schema.Lesson).
    lesson: dict[str, Any]
    mathematical_core: str = ""
    engineering_application: str = ""
    computational_component: str = ""
    visualization_component: str = ""
    research_extension: str = ""
    previous_link: str = ""
    subject_title: str = ""
    prev_topic: str | None = None


class LabParameterOut(BaseModel):
    key: str
    label: str
    minimum: float
    maximum: float
    default: float
    step: float
    unit: str = ""


class RunRequest(BaseModel):
    """Interactive Lab'dan keladigan so'rov."""

    code: str | None = Field(
        default=None,
        description="Foydalanuvchi tahrirlagan kod. Bo'sh bo'lsa, "
                    "mavzuning original kodi ishlatiladi.",
        max_length=60_000,
    )
    params: dict[str, float] = Field(default_factory=dict)


class RunResponse(BaseModel):
    ok: bool
    values: list[dict[str, Any]] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    series: list[dict[str, Any]] = Field(default_factory=list)
    tables: list[dict[str, Any]] = Field(default_factory=list)
    stdout: str = ""
    error: str = ""
    error_type: str = ""
    duration_ms: int = 0


class GraphNode(BaseModel):
    id: str
    title: str
    subject_id: str
    module_id: str = ""
    order: int = 0
    difficulty: str = "asosiy"


class GraphEdge(BaseModel):
    source: str
    target: str
    kind: str = "prerequisite"


class GraphResponse(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]


class AuditCheck(BaseModel):
    key: str = ""
    question: str = ""
    passed: bool = False
    detail: str = ""
    offenders: list[str] = Field(default_factory=list)


class AuditResponse(BaseModel):
    passed: bool
    checks: list[AuditCheck]
    counts: dict[str, int] = Field(default_factory=dict)


class HealthResponse(BaseModel):
    status: str
    version: str
    database: str
    seeded: bool
    counts: dict[str, int] = Field(default_factory=dict)
    sandbox: str


SubjectDetail.model_rebuild()

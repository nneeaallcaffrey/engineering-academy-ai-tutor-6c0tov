"""ORM modellari.

Kurikulum kontenti — Python dataclass'lardan JSON'ga eksport qilinadi va
shu yerdan bazaga yuklanadi. Dars mazmuni butunligicha `payload` (JSON)
ustunida saqlanadi: u faqat o'qiladi va uning ichki tuzilishi
`content/curriculum/schema.py` da qat'iy belgilangan, shuning uchun uni
o'nlab jadvalga yoyishdan foyda yo'q. Qidiriladigan va bog'lanadigan
maydonlar esa alohida ustunlarda — indekslanadi.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import (
    JSON, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def _now() -> datetime:
    return datetime.now(timezone.utc)


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    code: Mapped[str] = mapped_column(String(16), nullable=False)
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    tagline: Mapped[str] = mapped_column(String(500), default="")
    description: Mapped[str] = mapped_column(Text, default="")
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)

    modules: Mapped[list["Module"]] = relationship(
        back_populates="subject", cascade="all, delete-orphan")
    topics: Mapped[list["Topic"]] = relationship(
        back_populates="subject", cascade="all, delete-orphan")


class Module(Base):
    __tablename__ = "modules"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    subject_id: Mapped[str] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE"), index=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    summary: Mapped[str] = mapped_column(Text, default="")
    outcome: Mapped[str] = mapped_column(Text, default="")

    subject: Mapped[Subject] = relationship(back_populates="modules")


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    subject_id: Mapped[str] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE"), index=True)
    module_id: Mapped[str] = mapped_column(String(64), index=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    global_order: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(400), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")
    difficulty: Mapped[str] = mapped_column(String(32), default="asosiy")
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=90)
    next_topic: Mapped[str | None] = mapped_column(String(64), nullable=True)
    prerequisites: Mapped[list] = mapped_column(JSON, default=list)
    tags: Mapped[list] = mapped_column(JSON, default=list)
    #: To'liq dars (18 bo'lim) — schema.Lesson ning JSON ko'rinishi.
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)

    subject: Mapped[Subject] = relationship(back_populates="topics")

    __table_args__ = (Index("ix_topic_subject_order", "subject_id", "order"),)


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    subject_id: Mapped[str] = mapped_column(String(64), index=True)
    title: Mapped[str] = mapped_column(String(400), nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject_id: Mapped[str] = mapped_column(String(64), index=True)
    title: Mapped[str] = mapped_column(String(400), nullable=False)
    author: Mapped[str] = mapped_column(String(300), default="")
    year: Mapped[str] = mapped_column(String(32), default="")
    kind: Mapped[str] = mapped_column(String(32), default="asosiy")
    note: Mapped[str] = mapped_column(Text, default="")

    __table_args__ = (
        UniqueConstraint("subject_id", "title", name="uq_resource_subject_title"),
    )


class LabRun(Base):
    """Laboratoriya ishga tushirilishining jurnali (diagnostika uchun)."""

    __tablename__ = "lab_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[str | None] = mapped_column(String(64), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now, index=True)
    ok: Mapped[bool] = mapped_column(default=False)
    duration_ms: Mapped[int] = mapped_column(Integer, default=0)
    error_type: Mapped[str] = mapped_column(String(64), default="")
    #: Kodning o'zi SAQLANMAYDI — faqat uzunligi va xesh.
    code_sha256: Mapped[str] = mapped_column(String(64), default="")
    code_length: Mapped[int] = mapped_column(Integer, default=0)


class Meta(Base):
    """Yagona satrli jadval: seed holati va kurikulum versiyasi."""

    __tablename__ = "meta"

    key: Mapped[str] = mapped_column(String(64), primary_key=True)
    value: Mapped[str] = mapped_column(Text, default="")

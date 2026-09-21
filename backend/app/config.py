"""Backend sozlamalari — muhit o'zgaruvchilaridan o'qiladi."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MEXANIKA_", env_file=".env",
                                      extra="ignore")

    app_name: str = "Mexanika Akademiyasi API"
    version: str = "1.0.0"

    #: Kurikulum JSON — content/curriculum/export.py yaratadi.
    curriculum_json: Path = _ROOT / "content" / "generated" / "curriculum.json"
    database_url: str = f"sqlite:///{_ROOT / 'backend' / 'data' / 'mexanika.db'}"

    #: CORS: dev rejimda Vite, Docker'da nginx.
    cors_origins: list[str] = [
        "http://localhost:5173", "http://127.0.0.1:5173",   # Vite dev
        "http://localhost:7070", "http://127.0.0.1:7070",   # Docker / nginx
        "http://localhost:8080", "http://127.0.0.1:8080",
    ]

    #: Sandbox cheklovlari (executor.RunLimits bilan mos).
    lab_wall_seconds: float = 20.0
    lab_cpu_seconds: int = 15
    lab_memory_mb: int = 768

    #: Bitta IP uchun daqiqasiga nechta kod ishga tushirish mumkin.
    lab_rate_per_minute: int = 20

    seed_on_startup: bool = True


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

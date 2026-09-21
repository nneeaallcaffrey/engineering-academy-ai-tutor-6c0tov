# Backend: FastAPI + sandbox
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Ilmiy paketlar uchun minimal tizim kutubxonalari
RUN apt-get update \
 && apt-get install -y --no-install-recommends libgomp1 curl \
 && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Kurikulum manbasi va backend
COPY content /app/content
COPY backend /app/backend

# JSON ni TASVIR ICHIDA yaratamiz — ishga tushishda tashqi narsa kerak emas
RUN python -m content.curriculum.export

# Sandbox root'dan TASHQARI foydalanuvchida ishlaydi
RUN useradd --create-home --uid 10001 mexanika \
 && mkdir -p /app/backend/data \
 && chown -R mexanika:mexanika /app/backend/data
USER mexanika

ENV PYTHONPATH=/app/backend \
    MEXANIKA_CURRICULUM_JSON=/app/content/generated/curriculum.json \
    MEXANIKA_DATABASE_URL=sqlite:////app/backend/data/mexanika.db

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/health || exit 1

WORKDIR /app/backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

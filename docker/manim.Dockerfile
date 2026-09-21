# Manim: faqat animatsiyalarni render qilish uchun (ixtiyoriy profil).
# Bu tasvir katta, shuning uchun u asosiy stek bilan birga ishga tushmaydi.
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential pkg-config \
      libcairo2-dev libpango1.0-dev ffmpeg \
      texlive texlive-latex-extra texlive-fonts-extra dvisvgm \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir manim==0.18.1 numpy scipy

WORKDIR /app
COPY content /app/content
COPY animatsiya /app/animatsiya

ENV PYTHONPATH=/app
CMD ["python", "-m", "animatsiya.render", "--all", "--quality", "orta"]

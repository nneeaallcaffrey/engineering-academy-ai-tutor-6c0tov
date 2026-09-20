# Backend — Mexanika Akademiyasi API

FastAPI + SQLAlchemy. Kontent manbai — `content/generated/curriculum.json`
(uni `python -m content.curriculum.export` yaratadi).

## Ishga tushirish (dev)

```bash
pip install -r requirements.txt
cd ..  &&  python -m content.curriculum.export   # JSON ni yangilash
cd backend
uvicorn app.main:app --reload --port 8000
```

Swagger: http://localhost:8000/docs

## Testlar

```bash
python -m pytest              # tez testlar
python -m pytest --runslow    # + 150 laboratoriyaning hammasini bajarish
```

## Xavfsizlik

Foydalanuvchi Python kodi asosiy jarayonda **hech qachon** `exec()`
qilinmaydi. `app/sandbox/` ning docstring'lariga va loyiha ildizidagi
`README.md` ning "Ishlab chiqarish uchun sandbox" bo'limiga qarang.

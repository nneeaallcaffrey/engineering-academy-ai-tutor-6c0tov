"""FastAPI ilovasi."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.database import SessionLocal
from app.routers import curriculum, health, projects, resources, subjects, topics
from app.seed import CurriculumMissingError, init_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s: %(message)s")
log = logging.getLogger("mexanika")


@asynccontextmanager
async def lifespan(app: FastAPI):
    s = get_settings()
    if s.seed_on_startup:
        db = SessionLocal()
        try:
            changed = init_db(db)
            log.info("Baza tayyor (yangilandi: %s)", changed)
        except CurriculumMissingError as exc:
            log.error("%s", exc)
        finally:
            db.close()
    yield


app = FastAPI(
    title=get_settings().app_name,
    version=get_settings().version,
    description=(
        "Mexanika ta'lim platformasi: 5 fan, 150 mavzu, har bir mavzuda "
        "18 bo'limli dars va sandbox'da bajariladigan Python hisobi.\n\n"
        "**Xavfsizlik.** `/api/topics/{id}/run` foydalanuvchi kodini "
        "asosiy jarayonda HECH QACHON `exec()` qilmaydi: kod avval AST "
        "darajasida tekshiriladi, so'ngra alohida, tarmoqsiz, resurs "
        "chegaralari qo'yilgan jarayonda bajariladi."
    ),
    lifespan=lifespan,
    docs_url=None,          # quyida mahalliy aktivlar bilan qayta quriladi
    redoc_url=None,
    openapi_tags=[
        {"name": "Fanlar", "description": "Beshta fan va ularning modullari"},
        {"name": "Mavzular", "description": "150 mavzu va Interactive Lab"},
        {"name": "Loyihalar", "description": "Har bir fan uchun yakuniy loyiha"},
        {"name": "Manbalar", "description": "Adabiyotlar"},
        {"name": "Kurikulum", "description": "Bog'liqlik grafi va audit"},
        {"name": "Xizmat", "description": "Holat tekshiruvi"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def unhandled(request: Request, exc: Exception) -> JSONResponse:
    """Ichki xatolik tafsilotlari mijozga CHIQMAYDI."""
    log.exception("Kutilmagan xatolik: %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "Serverda ichki xatolik yuz berdi."},
    )


# Swagger UI aktivlari PAKET ICHIDA — CDN'ga chiqmaydi, shuning uchun
# /docs internetsiz muhitda ham ochiladi.
_STATIC = Path(__file__).resolve().parent / "static"
if _STATIC.is_dir():
    app.mount("/static", StaticFiles(directory=str(_STATIC)), name="static")


@app.get("/docs", include_in_schema=False)
def swagger_ui() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "/openapi.json",
        title=f"{app.title} — Swagger",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="/static/swagger-ui.css",
    )


for r in (health.router, subjects.router, topics.router, projects.router,
          resources.router, curriculum.router):
    app.include_router(r)


@app.get("/", include_in_schema=False)
def root() -> dict[str, str]:
    return {"name": get_settings().app_name, "docs": "/docs", "health": "/health"}

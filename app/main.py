from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import analytics
from app.core.config import settings

app = FastAPI(title="readme-analytics", version="0.1.0")

origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",") if o.strip()] or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(analytics.router)

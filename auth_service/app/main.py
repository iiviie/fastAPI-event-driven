from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth_router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "auth-microservice",
        "environment": settings.environment.value,
        "version": settings.app_version,
    }
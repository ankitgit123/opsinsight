

from fastapi import FastAPI
from app.core.config import settings

app=FastAPI(
    title=settings.app_name,
    description="Enterprise AI-powered business data analyst agent",
    version="0.1.0",
    debug=settings.debug,
)

@app.get("/health",tags=["Health"])
async def health_check()-> dict:
    return {"status": "healthy", "application": settings.app_name, "environment": settings.app_env}


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to OpsInsight API",
        "version": "0.1.0",
    }

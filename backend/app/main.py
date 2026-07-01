from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from app.config import settings
from app.database import init_database
from app.routes import auth, user, questions

# Initialize database
init_database()

# Create app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="SkillsPrint Backend API - Placement Preparation Platform",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ============ CORS CONFIGURATION ============
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "*"  # For development only
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(questions.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to SkillsPrint API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "healthy"
    }

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy", "environment": settings.ENVIRONMENT}
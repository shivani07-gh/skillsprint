# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.config import settings
from app.database import init_database
from app.routes import auth, user

# Initialize database
init_database()

# Create app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="SkillsPrint Backend API - Authentication & Authorization",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS middleware
# app/main.py - Alternative CORS configuration

# Get allowed origins from settings
allowed_origins = settings.ALLOWED_ORIGINS.split(",") if settings.ALLOWED_ORIGINS else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if settings.ENVIRONMENT == "production" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(user.router)

# ========== FRONTEND SERVING ==========
# The frontend is at /app/frontend in Docker
FRONTEND_DIR = "/app/frontend"

# Also check other possible locations
if not os.path.exists(FRONTEND_DIR):
    # For local development
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

print(f"📁 Looking for frontend at: {FRONTEND_DIR}")

if os.path.exists(FRONTEND_DIR):
    # Mount static files
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
    
    # Serve HTML pages
    @app.get("/")
    async def serve_login():
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
    
    @app.get("/signup")
    async def serve_signup():
        return FileResponse(os.path.join(FRONTEND_DIR, "signup.html"))
    
    @app.get("/dashboard")
    async def serve_dashboard():
        return FileResponse(os.path.join(FRONTEND_DIR, "dashboard.html"))
    
    print("✅ Frontend served successfully!")
else:
    # Fallback API response
    @app.get("/")
    def root():
        return {
            "message": f"Welcome to {settings.APP_NAME} API",
            "version": settings.APP_VERSION,
            "status": "healthy"
        }
    print("❌ Frontend not found!")

@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy", "environment": settings.ENVIRONMENT}
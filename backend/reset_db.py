# backend/reset_db.py
"""
Reset the database and reload data
Run: python reset_db.py
"""

import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from app.database import engine, Base
from app.models.question import Question

def reset_database():
    """Drop and recreate all tables"""
    print("=" * 50)
    print("🔄 Resetting Database")
    print("=" * 50)
    
    # Drop all tables
    print("🗑️ Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("✅ Tables dropped")
    
    # Create all tables
    print("📊 Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created")
    
    print("=" * 50)
    print("✅ Database reset complete!")
    print("=" * 50)

if __name__ == "__main__":
    reset_database()
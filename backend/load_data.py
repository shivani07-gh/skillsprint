"""
Load CSV data into database
Run: python load_data.py
"""

import sys
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from app.database import SessionLocal, engine, Base
from app.models.question import Question
from app.services.question_service import QuestionService
from app.utils.csv_loader import csv_loader

def load_data():
    print("=" * 60)
    print("📊 Loading CSV Data into Database")
    print("=" * 60)
    
    # Ensure tables exist
    print("\n📊 Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables ready")
    
    db = SessionLocal()
    try:
        # Check existing data
        existing_count = db.query(Question).count()
        if existing_count > 0:
            print(f"⚠️ Database already has {existing_count} questions")
            confirm = input("❓ Overwrite existing data? (y/N): ")
            if confirm.lower() != 'y':
                print("❌ Operation cancelled")
                return
            print("🗑️ Clearing existing questions...")
            db.query(Question).delete()
            db.commit()
            print("✅ Existing data cleared")
        
        # Load data
        print("\n🔄 Loading CSV data...")
        result = QuestionService.load_csv_data_to_db(db)
        
        print("\n" + "=" * 60)
        print(f"✅ Successfully loaded {result['total_loaded']} questions")
        print("=" * 60)
        
        # Show summary
        from sqlalchemy import func
        subjects = db.query(Question.subject, func.count(Question.id)).group_by(Question.subject).all()
        if subjects:
            print("\n📊 Subject Summary:")
            for subject, count in subjects:
                print(f"  • {subject}: {count} questions")
        else:
            print("\n⚠️ No data loaded. Check CSV files.")
        
        # Show difficulty distribution
        difficulties = db.query(Question.difficulty, func.count(Question.id)).group_by(Question.difficulty).all()
        if difficulties:
            print("\n📊 Difficulty Distribution:")
            for diff, count in difficulties:
                diff_name = diff.value if hasattr(diff, 'value') else str(diff)
                print(f"  • {diff_name}: {count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    load_data()
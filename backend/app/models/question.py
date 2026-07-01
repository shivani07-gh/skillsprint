from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, Enum as SQLEnum
from sqlalchemy.sql import func
import enum

from app.database import Base

class Difficulty(str, enum.Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    
    @classmethod
    def _missing_(cls, value):
        """Handle case-insensitive matching"""
        if isinstance(value, str):
            value_lower = value.lower()
            for member in cls:
                if member.value.lower() == value_lower:
                    return member
        return None

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(String(50), unique=True, index=True, nullable=True)
    
    # Subject categorization
    subject = Column(String(50), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=False, index=True)
    difficulty = Column(SQLEnum(Difficulty, values_callable=lambda obj: [e.value for e in obj]), default=Difficulty.MEDIUM)
    
    # Question content
    question = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # List of 4 options
    correct_option = Column(Integer, nullable=False)  # 0-3
    explanation = Column(Text, nullable=True)
    hint = Column(Text, nullable=True)
    formula = Column(Text, nullable=True)
    shortcut = Column(Text, nullable=True)
    
    # Metadata
    estimated_time = Column(Integer, default=60)  # seconds
    company = Column(String(100), nullable=True)
    exam = Column(String(100), nullable=True)
    tags = Column(JSON, nullable=True)  # List of tags
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'subject': self.subject,
            'topic': self.topic,
            'subtopic': self.subtopic,
            'difficulty': self.difficulty.value if self.difficulty else None,
            'question': self.question,
            'options': self.options,
            'correct_option': self.correct_option,
            'explanation': self.explanation,
            'hint': self.hint,
            'formula': self.formula,
            'shortcut': self.shortcut,
            'estimated_time': self.estimated_time
        }
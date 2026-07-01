from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

class QuestionBase(BaseModel):
    subject: str = Field(..., description="Subject name")
    topic: str = Field(..., description="Topic name")
    subtopic: str = Field(..., description="Subtopic name")
    difficulty: str = Field(..., description="Easy, Medium, or Hard")
    question: str = Field(..., description="Question text")
    options: List[str] = Field(..., min_length=4, max_length=4, description="4 options")
    correct_option: int = Field(..., ge=0, le=3, description="Index of correct option (0-3)")
    explanation: Optional[str] = Field(None, description="Explanation")
    hint: Optional[str] = Field(None, description="Hint for the question")
    formula: Optional[str] = Field(None, description="Formula used")
    shortcut: Optional[str] = Field(None, description="Shortcut trick")

class QuestionCreate(QuestionBase):
    question_id: Optional[str] = None
    estimated_time: Optional[int] = 60
    tags: Optional[List[str]] = None

class QuestionResponse(QuestionBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    question_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SubjectSummary(BaseModel):
    name: str
    icon: str
    description: str
    color: str
    total_questions: int
    topics_count: int
    progress: float = 0.0

class TopicSummary(BaseModel):
    name: str
    total_questions: int
    subtopics: List[str]
    progress: float = 0.0

class SubtopicSummary(BaseModel):
    name: str
    total_questions: int
    difficulty: str
    progress: float = 0.0

class SubjectDetail(BaseModel):
    subject: str
    topics: List[TopicSummary]

class QuestionFilter(BaseModel):
    subject: Optional[str] = None
    topic: Optional[str] = None
    subtopic: Optional[str] = None
    difficulty: Optional[str] = None
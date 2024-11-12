from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = "subjects"
    
    subject_code = Column(String, primary_key=True, index=True)  # Código único da matéria
    name = Column(String(), nullable=False)
    study_load = Column(Integer, nullable=False)
    
    

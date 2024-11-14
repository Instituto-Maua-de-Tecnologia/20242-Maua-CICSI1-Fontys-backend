from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = "subjects"
    
    subject_code = Column(String, primary_key=True, index=True)  # Código único da matéria
    name = Column(String(), nullable=False)
    study_load = Column(Integer, nullable=False)
    
    user_subject = relationship("UserSubject", back_populates="subject")
    semester = relationship("Semester", back_populates="subject")
    
    


    

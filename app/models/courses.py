from uuid import uuid4
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = "courses"
    
    course_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    
    semester = relationship("Semester", back_populates="course")  
    coordination = relationship("Coordination", back_populates="course")
    schedule = relationship("Schedule", back_populates="course")
      
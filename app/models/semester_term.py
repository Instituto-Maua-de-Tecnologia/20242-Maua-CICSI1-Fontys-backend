

from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class SemesterTerm(BaseModel): 
    __table__ = 'semester_term'
    
    semester_id = Column(String, primary_key=True, index=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    subject_code = Column(String, ForeignKey("subject_codes.subject_code"), nullable=False)
    number = Column(Integer, nullable=False)
    
    courses = relationship("Course", back_populates="semester_term")
    subject_codes = relationship("Subject", back_populates="semester_term")
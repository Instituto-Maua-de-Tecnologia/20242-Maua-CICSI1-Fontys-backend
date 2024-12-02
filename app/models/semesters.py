from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

class Semester(Base):
    __tablename__ = "semesters"

    semester_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    semester_number = Column(Integer, nullable=False, index=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    subject_code = Column(String, ForeignKey("subjects.subject_code"), nullable=False)

    subject = relationship("Subject", back_populates="semester")
    course = relationship("Course", back_populates="semester")
    schedule = relationship("Schedule", back_populates="semester")
    coordination = relationship("Coordination", back_populates="semester")
from uuid import uuid4
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    schedule_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    course_id = Column(String, ForeignKey('courses.course_id'), nullable=False)
    slot_id = Column(Integer, ForeignKey('slots.slot_id'), nullable=False)
    subject_code = Column(String, ForeignKey('subjects.subject_code'), nullable=False)
    semester_number = Column(Integer, ForeignKey('semesters.semester_number'), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="schedule")
    course = relationship("Course", back_populates="schedule")
    subject = relationship("Subject", back_populates="schedule")
    slot = relationship("Slot", back_populates="schedule")
    semester = relationship("Semester", back_populates="schedule")
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base

class Schedule(Base):
    __tablename__ = "schedule"
    
    schedule_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    course_id = Column(String, ForeignKey('courses.course_id'), nullable=False)
    slot_id = Column(String, ForeignKey('slots.slot_id'), nullable=False)
    subject_code = Column(String, ForeignKey('subject_codes.subject_code'), nullable=False)
    number_semester = Column(Integer, nullable=False)
    
    users = relationship("User", back_populates="schedules")
    courses = relationship("Course", back_populates="schedules")
    subject_codes = relationship("Subject", back_populates="schedules")
    slots = relationship("Slot", back_populates="schedules")

from sqlalchemy import Column, Integer, String, ForeignKey, Time, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.enum.days_of_week import DayOfWeek
from app.enum.time_slot import TimeSlot
from app.models.subject import Subject
from app.models.user import User

class Calendar(Base):
    __tablename__ = "calendar"
    
    calendar_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('professors.id'), nullable=False)
    subject_id = Column(String, ForeignKey('subjects.id'), nullable=False)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)
    time_slot = Column(Enum(TimeSlot), nullable=False)
    
    user = relationship("User", back_populates="schedules")
    subject = relationship("Subject", back_populates="schedules")

User.schedules = relationship("Schedule", back_populates="professor")
Subject.schedules = relationship("Schedule", back_populates="subject")
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.enum.days_of_week import DayOfWeek
from app.models.subject import Subject
from app.models.user import User

class Schedule(Base):
    __tablename__ = "schedules"
    schedule_id = Column(String, primary_key=True, index=True)
    professor_id = Column(String, ForeignKey('professors.id'), nullable=False)
    subject_id = Column(String, ForeignKey('subjects.id'), nullable=False)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)
    time_slot = Column(String, nullable=False)
    # Relacionamentos
    professor = relationship("Professor", back_populates="schedules")
    subject = relationship("Subject", back_populates="schedules")

User.schedules = relationship("Schedule", back_populates="professor")
Subject.schedules = relationship("Schedule", back_populates="subject")
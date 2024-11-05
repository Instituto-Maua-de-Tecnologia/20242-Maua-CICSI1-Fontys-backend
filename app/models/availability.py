from sqlalchemy import Boolean, Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.enum.days_of_week import DayOfWeek
from app.enum.time_slot import TimeSlot

class Availability(Base):
    __tablename__ = "availability"

    availability_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)
    time_slot = Column(Enum(TimeSlot), nullable=False)
    status = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="availabilities")

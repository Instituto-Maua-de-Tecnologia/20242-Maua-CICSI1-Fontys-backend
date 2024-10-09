from sqlalchemy import Boolean, Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.enum import DaysOfWeek, TimeSlots

class Availability(Base):
    __tablename__ = "availability"

    availability_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    day_of_week = Column(Enum(DaysOfWeek), nullable=False)
    time_slot = Column(Enum(TimeSlots), nullable=False)
    status = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="availabilities")

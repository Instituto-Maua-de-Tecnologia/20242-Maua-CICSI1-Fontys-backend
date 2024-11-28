from app.core.database import Base
from sqlalchemy import Column, DateTime, Enum as SqlEnum, Integer

from app.enums.days_of_week_enum import DayOfWeekEnum
from sqlalchemy.orm import relationship


class Slot(Base): 
    __tablename__ = "slots"
    
    slot_id = Column(Integer, primary_key=True, index=True)
    day_of_week = Column(SqlEnum(DayOfWeekEnum), nullable=False)
    time = Column(DateTime, nullable=False)
    
    availability = relationship("Availability", back_populates="slot")
    schedule = relationship("Schedule", back_populates="slot")
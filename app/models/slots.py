from app.core.database import Base
from sqlalchemy import Column, Enum, String, Time

from app.enum.days_of_week import DayOfWeek


class Slots(Base): 
    __tablename__ = "slots"
    
    slot_id = Column(String, primary_key=True, index=True)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)
    time = Column(Time, nullable=False)
    
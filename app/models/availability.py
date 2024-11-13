from sqlalchemy import  Column, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.enum import Values

class Availability(Base):
    __tablename__ = "availability"
    
    availability_id = Column(String, primary_key=True, index=True)
    slot_id = Column(String, ForeignKey("slots.slot_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    value = Column(Enum(Values), nullable=False)

    users = relationship("User", back_populates="availabilities")
    slots = relationship("Slot", back_populates="availabilities")

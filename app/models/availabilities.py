from sqlalchemy import  Column, Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.enums.availability_values_enum import AvailabilityValuesEnum

class Availability(Base):
    __tablename__ = "availabilitys"
    
    availability_id = Column(String, primary_key=True, index=True)
    slot_id = Column(Integer, ForeignKey("slots.slot_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    availability_value = Column(SqlEnum(AvailabilityValuesEnum), nullable=False)

    user = relationship("User", back_populates="availability")
    slot = relationship("Slot", back_populates="availability")

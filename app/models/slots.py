from app.db.base import Base
from sqlalchemy import Column, String


class Slots(Base): 
    __tablename__ = "slot"
    
    slot_id = Column(String, primary_key=True, index=True)
    day_time = Column(String, nullable=False)
    
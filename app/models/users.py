import os

from sqlalchemy import Column, String
from app.core.database import Base, engine
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    user_id = Column(String(), primary_key=True, index=True)
    microsoft_id = Column(String(), nullable=False)
    photo = Column(String(), nullable=True)
    name = Column(String(), nullable=False)
    notes = Column(String(500), nullable=True)

    user_type = relationship("UserType", back_populates="user")
    user_subject = relationship("UserSubject", back_populates="user")
    availability = relationship("Availability", back_populates="user")
    user_shipping = relationship("UserShipping", back_populates="user")
    schedule = relationship("Schedule", back_populates="user")

    

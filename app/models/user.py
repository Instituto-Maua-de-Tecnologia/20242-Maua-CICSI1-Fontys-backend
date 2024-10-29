from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
from sqlalchemy.orm import relationship

from app.enum.status_type import StatusType
from app.enum.user_type import UserType


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(), primary_key=True, index=True)
    microsoft_id = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    status = Column(Enum(StatusType), default="Active", nullable=False)
    name = Column(String(), nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    notes = Column(String(500), nullable=True)

    subjects = relationship("UserSubject", back_populates="user")
    availabilities = relationship("Availability", back_populates="user")

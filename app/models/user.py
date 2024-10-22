from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(200), primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(Enum("Active", "Inactive"), default="Active")
    name = Column(String(255), nullable=False)
    user_type = Column(Enum("Secretary", "Professor", "Coordinator"), nullable=False)
    notes = Column(String(500), nullable=True)

    subjects = relationship("UserSubject", back_populates="user")
    availabilities = relationship("Availability", back_populates="user")

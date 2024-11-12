from sqlalchemy import Column, String, Enum
from app.db.base import Base
from sqlalchemy.orm import relationship

from app.enum.user_type import UserType


class User(Base):
    __tablename__ = "user"

    user_id = Column(String(), primary_key=True, index=True)
    microsoft_id = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    notes = Column(String(500), nullable=True)


from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class UserSubject(Base):
    __tablename__ = "user_subject"

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    subject_code = Column(String, ForeignKey("subject_codes.id"), nullable=False)

    users = relationship("User", back_populates="subjects")
    subject_codes = relationship("Subject", back_populates="users")

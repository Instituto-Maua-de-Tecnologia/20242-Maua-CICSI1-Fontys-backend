from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class UserSubject(Base):
    __tablename__ = "user_subjects"

    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    subject_code = Column(String, ForeignKey("subject_codes.id"), nullable=False)

    users = relationship("User", back_populates="subjects")
    subject_codes = relationship("Subject", back_populates="users")

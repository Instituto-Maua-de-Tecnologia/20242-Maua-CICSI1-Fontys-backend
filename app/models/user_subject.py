from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class UserSubject(Base):
    __tablename__ = "user_subjects"

    subject_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    subject_code = Column(String, ForeignKey("subjects.code"), nullable=False)

    user = relationship("User", back_populates="subjects")
    subject = relationship("Subject", back_populates="users")

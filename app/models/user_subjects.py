from uuid import uuid4
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base, engine

class UserSubject(Base):
    __tablename__ = "user_subjects"
    
    user_subject_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    subject_code = Column(String, ForeignKey("subjects.subject_code"), nullable=False)

    user = relationship("User", back_populates="user_subject")
    subject = relationship("Subject", back_populates="user_subject")



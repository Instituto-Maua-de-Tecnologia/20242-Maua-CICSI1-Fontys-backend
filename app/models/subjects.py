from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    subject_code = Column(String, primary_key=True, index=True)
    subject_name = Column(String, nullable=False)

   
    schedule = relationship("Schedule", back_populates="subject")

  
    user_subject = relationship("UserSubject", back_populates="subject")
    semester = relationship("Semester", back_populates="subject")
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

class Semester(Base):
    __tablename__ = "semesters"

    semester_number = Column(Integer, primary_key=True, index=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)

    course = relationship("Course", back_populates="semester")
    schedule = relationship("Schedule", back_populates="semester")
    coordination = relationship("Coordination", back_populates="semester")
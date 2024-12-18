from uuid import uuid4
from sqlalchemy import  Column, ForeignKey, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship


class Coordination(Base):
    __tablename__ = "coordinations"

    coordination_id = Column(String, primary_key=True, index=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    semester_id = Column(Integer, ForeignKey("semesters.semester_id"), nullable=False)
    year = Column(String, nullable=False)

    course = relationship("Course", back_populates="coordination")
    user = relationship("User", back_populates="coordination")
    semester = relationship("Semester", back_populates="coordination")
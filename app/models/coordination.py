from sqlalchemy import  Column, ForeignKey, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Coordination(Base): 
    __tablename__ = "coordination"
    
    coordination_id = Column(String, primary_key=True, index=True)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    user_id = Column(String, ForeignKey("user.user_id"), nullable=False)
    semester = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)   
    
    courses = relationship("Course", back_populates="coordination")
    users = relationship("User", back_populates="coordination")
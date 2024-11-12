from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Course(Base):
    __tablename__ = "course"
    
    course_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    
      
      
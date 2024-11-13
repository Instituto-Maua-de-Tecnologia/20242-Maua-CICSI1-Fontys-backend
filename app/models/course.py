from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Course(Base):
    __tablename__ = "courses"
    
    course_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    
      
      
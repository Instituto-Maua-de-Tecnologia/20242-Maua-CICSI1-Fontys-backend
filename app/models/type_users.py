from sqlalchemy import Column, String
from app.core.database import Base, engine
from sqlalchemy.orm import relationship

class TypeUser(Base):
    __tablename__ = "type_users"
    
    type_id = Column(String, primary_key=True, index=True)
    type_name = Column(String, nullable=False)

    user_type = relationship("UserType", back_populates="type_user")


    
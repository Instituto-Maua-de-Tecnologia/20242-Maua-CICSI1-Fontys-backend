from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base, engine

class UserType(Base):
    __tablename__ = "user_types"
    
    user_type_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    type_id = Column(String, ForeignKey("type_users.type_id"), nullable=False)
    
    user = relationship("User", back_populates="user_type")
    type_user = relationship("TypeUser", back_populates="user_type")


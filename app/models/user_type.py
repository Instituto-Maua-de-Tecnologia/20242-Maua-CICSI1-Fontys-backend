from sqlalchemy import Column, ForeignKey, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class UserType(Base):
    __tablename__ = "user_types"
    
    user_type_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    type_id = Column(String, ForeignKey("types.type_id"), nullable=False)
    
    
    users = relationship("User", back_populates="types")
    types = relationship("Type", back_populates="users")
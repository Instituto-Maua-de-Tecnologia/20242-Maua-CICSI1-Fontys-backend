from sqlalchemy import Column, String, Enum as SqlEnum
from app.core.database import Base, engine
from sqlalchemy.orm import relationship
from app.enums.type_user_enum import TypeUserEnum

class TypeUser(Base):
    __tablename__ = "type_users"
    
    type_id = Column(String, primary_key=True, index=True)
    type_name = Column(SqlEnum(TypeUserEnum), nullable=False)

    user_type = relationship("UserType", back_populates="type_user")


    
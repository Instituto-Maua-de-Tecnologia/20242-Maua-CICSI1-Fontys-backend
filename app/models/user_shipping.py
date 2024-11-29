
from uuid import uuid4
from app.core.database import Base
from sqlalchemy import Column, DateTime, Enum as SqlEnum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.enums.status_type_enum import StatusTypeEnum



class UserShipping(Base):
    __tablename__ = 'user_shippings'

    shipping_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    shipping_date = Column(DateTime, nullable=False)
    status = Column(SqlEnum(StatusTypeEnum), nullable=False)
    
    user = relationship("User", back_populates="user_shipping")
    
    

from app.core.database import Base
from sqlalchemy import Column, Date, Enum as SqlEnum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.enums.status_type import StatusType



class UserShipping(Base):
    __tablename__ = 'user_shippings'

    shipping_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    shipping_date = Column(Date, nullable=False)
    status = Column(SqlEnum(StatusType), nullable=False)
    
    user = relationship("User", back_populates="user_shipping")
    
    

from app.core.database import Base
from sqlalchemy import Column, Date, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.enum.status_type import StatusType



class UserShipping(Base):
    __tablename__ = 'user_shippings'

    shipping_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    shipping_date = Column(Date, nullable=False)
    status = Column(Enum(StatusType), nullable=False)
    
    users = relationship("User", back_populates="user_shipping")
    
    
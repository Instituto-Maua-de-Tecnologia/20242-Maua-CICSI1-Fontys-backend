


from pydantic import BaseModel
from sqlalchemy import Column, Date, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.enum.status_type import StatusType



class UserShipping(BaseModel):
    __tablename__ = 'user_shipping'

    shipping_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    shipping_date = Column(Date, nullable=False)
    status = Column(Enum(StatusType), nullable=False)
    
    users = relationship("User", back_populates="user_shipping")
    
    

from pydantic import BaseModel
from sqlalchemy import Date

from app.enums.status_type import StatusType

class UserShippingBase(BaseModel):
    shipping_id: str
    user_id: str
    shipping_date: Date
    status: StatusType
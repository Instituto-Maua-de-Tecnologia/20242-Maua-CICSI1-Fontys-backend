
from pydantic import BaseModel
from datetime import date

from app.enums.status_type import StatusType

class UserShippingBase(BaseModel):
    shipping_id: str
    user_id: str
    shipping_date: date
    status: StatusType
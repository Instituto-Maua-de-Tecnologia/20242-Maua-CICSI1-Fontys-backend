
from pydantic import BaseModel
from sqlalchemy import Date

from app.enum.status_type import StatusType

class UserShipping(BaseModel):
    shipping_id: str
    user_id: str
    shipping_date: Date
    status: StatusType
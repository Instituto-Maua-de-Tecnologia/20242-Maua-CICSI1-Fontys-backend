from pydantic import BaseModel

from app.enum.time_slot import TimeSlot
from app.enum.values import Values


class Availability(BaseModel):
    availability_id: str
    user_id: str
    slot_id: str
    value: Values
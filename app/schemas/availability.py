from pydantic import BaseModel

from app.enum.time_slot import TimeSlot


class Availability(BaseModel):
    availability_id: str
    user_id: str
    day_of_week: str
    time_slot: TimeSlot
    status: bool
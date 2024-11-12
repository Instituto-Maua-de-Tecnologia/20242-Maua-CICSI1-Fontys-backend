

from pydantic import BaseModel


class Slot(BaseModel):
    slot_id: str
    day_time: str
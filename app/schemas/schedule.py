from pydantic import BaseModel
from sqlalchemy import DateTime

class CreateScheduleIASchema(BaseModel):
    schedule_id: str
    name: str
    slot_id: int
    subject_code: str
    number_semester: int

class ScheduleResponseSchema(BaseModel):
    schedule_id: str
    message: str

from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

from app.enums.availability_values_enum import AvailabilityValuesEnum
from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum

class CreateScheduleIASchema(BaseModel):
    schedule_id: str
    name: str
    slot_id: int
    subject_code: str
    number_semester: int

class CreateScheduleSchema(BaseModel):
    course_id: str
    user_id: str
    slot_id: str
    subject_code: str
    semester_number: int
    created_at: str


class ScheduleResponseSchema(BaseModel):
    schedule_id: str
    message: str


class GenerateScheduleSchema(BaseModel):
    user_id: Optional[str]
    name : Optional[str]
    subject_code: Optional[str]
    slot_id: Optional[int]
    day_of_week: Optional[str]
    time: Optional[str]
    availability_value: Optional[str]
    subject_name: Optional[str]
    course_id: Optional[str]
    semester_number: Optional[int]
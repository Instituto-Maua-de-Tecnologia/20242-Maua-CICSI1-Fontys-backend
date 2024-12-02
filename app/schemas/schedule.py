from pydantic import BaseModel
from sqlalchemy import DateTime

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
    
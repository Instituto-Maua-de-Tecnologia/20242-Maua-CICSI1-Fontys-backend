

from pydantic import BaseModel


class CoordinationBase(BaseModel):
    coordination_id: str
    user_id: str
    course_id: str
    semester_number: int
    year: str
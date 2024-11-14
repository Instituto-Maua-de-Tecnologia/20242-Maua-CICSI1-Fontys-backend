
from pydantic import BaseModel


class CourseBase(BaseModel):
    course_id: str
    name: str
    duration: int
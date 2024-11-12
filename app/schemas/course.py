
from pydantic import BaseModel


class Course(BaseModel):
    course_id: str
    name: str
    duration: int
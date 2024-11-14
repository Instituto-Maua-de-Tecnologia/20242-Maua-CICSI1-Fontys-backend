

from pydantic import BaseModel


class SemesterBase(BaseModel):
    semester_number: int
    course_id: str
    subject_code: str
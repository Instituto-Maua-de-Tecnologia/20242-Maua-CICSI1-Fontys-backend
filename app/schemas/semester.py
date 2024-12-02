from pydantic import BaseModel


class SemesterBase(BaseModel):
    semester_id: int
    semester_number: int
    course_id: str
    subject_code: str


from pydantic import BaseModel


class SemesterTerm(BaseModel):
    semester_id: str
    course_id: str
    subject_code: str
    number: int
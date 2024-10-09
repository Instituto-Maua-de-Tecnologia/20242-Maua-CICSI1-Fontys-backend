from pydantic import BaseModel
from app.enum.subject_type import SubjectType
from app.models.user_subject import UserSubject


class Subject(BaseModel):
    name: str
    subject_code: str
    subject_type: SubjectType
    user: UserSubject 
    
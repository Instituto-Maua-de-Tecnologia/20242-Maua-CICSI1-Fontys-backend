from pydantic import BaseModel
from app.models.user_subject import UserSubject


class Subject(BaseModel):
    name: str
    subject_code: str
    user: UserSubject 
    
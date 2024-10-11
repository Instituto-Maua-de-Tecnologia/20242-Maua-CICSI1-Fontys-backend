from pydantic import BaseModel
from app.models.user_subject import UserSubject


class Subject(BaseModel):
    subject_id: str
    name: str
    subject_code: str
    study_load: int
    user: UserSubject 
    
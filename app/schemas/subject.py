from pydantic import BaseModel
from app.models.user_subject import UserSubject


class Subject(BaseModel):
    subject_code: str
    name: str
    study_load: int
    
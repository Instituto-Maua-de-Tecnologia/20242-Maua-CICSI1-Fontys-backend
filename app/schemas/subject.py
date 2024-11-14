from pydantic import BaseModel
from app.models.user_subjects import UserSubject


class SubjectBase(BaseModel):
    subject_code: str
    name: str
    study_load: int
    
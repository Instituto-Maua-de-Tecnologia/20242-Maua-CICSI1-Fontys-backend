from pydantic import BaseModel
from app.models.subject import Subject
from app.models.user import User


class UserSubject(BaseModel):
    user_id: str
    subject_id: str
    subject_code: str
    user: User
    subject: Subject
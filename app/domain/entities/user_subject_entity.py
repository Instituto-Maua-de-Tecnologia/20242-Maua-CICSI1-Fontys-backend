import string
from typing import Optional
from pydantic import BaseModel

from app.models import UserSubject


class UserSubjectEntity(BaseModel):
    user_subject_id: Optional[string] = None
    user_id: string
    subject_code: string

    def to_orm(self) -> UserSubject:
        return UserSubject(
            user_subject_id=self.user_subject_id,
            user_id=self.user_id,
            subject_code=self.subject_code,
        )

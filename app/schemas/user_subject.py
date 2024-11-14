from pydantic import BaseModel



class UserSubjectBase(BaseModel):
    user_subject_id: str
    user_id: str
    subject_code: str

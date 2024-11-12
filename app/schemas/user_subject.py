from pydantic import BaseModel



class UserSubject(BaseModel):
    user_id: str
    subject_code: str

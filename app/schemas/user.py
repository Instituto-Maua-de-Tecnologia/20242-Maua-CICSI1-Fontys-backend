from pydantic import BaseModel
from app.enums.user_type import UserType

class UserBase(BaseModel):
    user_id: str
    microsoft_id: str
    photo: str
    name: str
    notes: str
    

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int

    class Config:
        from_atributtes = True
from pydantic import BaseModel
from app.enum.user_type import UserType

class UserBase(BaseModel):
    user_id: str
    microsoft_id: str
    name: str
    notes: str
    

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
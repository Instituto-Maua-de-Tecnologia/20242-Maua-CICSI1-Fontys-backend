from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: str
    microsoft_id: str
    photo: str
    name: str
    notes: str
    
class UserInDB(UserBase):
    id: str

    class Config:
        from_atributtes = True
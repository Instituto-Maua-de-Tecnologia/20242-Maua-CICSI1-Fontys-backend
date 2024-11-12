from pydantic import BaseModel
from app.enum.user_type import UserType

class User(BaseModel):
    user_id: str
    microsoft_id: str
    name: str
    user_type: UserType
    notes: str
    

class CreateUserRequest(BaseModel):
    email: str
    name: str
    password: str

class CreateUserResponse(BaseModel):
    message: str
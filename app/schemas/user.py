from pydantic import BaseModel, Field
from typing import Optional

class CreateUserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    microsoft_id: str 
    photo: Optional[str] = None
    notes: Optional[str] = Field(None, max_length=500)

class UserResponseSchema(BaseModel):
    user_id: str
    message: str
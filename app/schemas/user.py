from pydantic import BaseModel, Field
from typing import Optional

from app.enums.status_type_enum import StatusTypeEnum

class CreateUserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    microsoft_id: Optional[str] = None 
    photo: Optional[str] = None
    notes: Optional[str] = Field(None, max_length=500)

class UserResponseSchema(BaseModel):
    user_id: str
    message: str
    
class GetAllProfessorsResponseSchema(BaseModel):
    user_id: str
    microsoft_id: str
    name: str
    photo: Optional[str] = None
    status: StatusTypeEnum
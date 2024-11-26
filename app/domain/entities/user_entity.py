
from typing import Optional
from pydantic import BaseModel

class UserEntity(BaseModel):
    user_id: Optional[str] = None
    microsoft_id: Optional[str] = True
    name: str
    photo: Optional[str] = True
    notes: Optional[str] = True
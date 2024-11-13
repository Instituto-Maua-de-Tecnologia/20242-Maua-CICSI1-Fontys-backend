
from typing import Optional
from pydantic import BaseModel

class UserEntity(BaseModel):
    user_id: str
    microsoft_id: Optional[str] = None
    name: str
    user_type: Optional[str] = None
    notes: Optional[str] = True
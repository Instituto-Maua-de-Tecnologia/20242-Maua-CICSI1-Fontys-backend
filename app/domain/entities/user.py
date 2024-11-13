
from typing import Optional
from pydantic import BaseModel

class UserEntity(BaseModel):
    user_id: str
    microsoft_id: Optional[str] = None
    name: str
    notes: Optional[str] = True

from typing import Optional
from pydantic import BaseModel

from app.models.users import User

class UserEntity(BaseModel):
    user_id: str
    microsoft_id: Optional[str] = None
    name: str
    photo: Optional[str] = None
    notes: Optional[str] = None
    
    def to_orm(self) -> User:
        return User(
            user_id=self.user_id,
            microsoft_id=self.microsoft_id if self.microsoft_id else None,
            name=self.name,
            photo=self.photo if self.photo else None,
            notes=self.notes if self.notes else None
        )
        
    @classmethod
    
    def from_orm(cls, user: User) -> "UserEntity":
        return cls(
            user_id=user.user_id,
            microsoft_id=user.microsoft_id,
            name=user.name,
            photo=user.photo,
            notes=user.notes
        )
        
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "microsoft_id": self.microsoft_id if self.microsoft_id else None,
            "name": self.name,
            "photo": self.photo if self.photo else None,
            "notes": self.notes if self.notes else None
        }
    
    
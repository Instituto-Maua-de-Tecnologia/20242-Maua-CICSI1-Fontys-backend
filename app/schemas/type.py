

from pydantic import BaseModel

from app.enum.user_type import UserType


class TypeBase(BaseModel):
    type_id: str
    type_name: UserType
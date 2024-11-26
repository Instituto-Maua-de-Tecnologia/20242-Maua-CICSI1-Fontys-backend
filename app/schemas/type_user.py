

from pydantic import BaseModel

from app.enums.user_type import UserType


class TypeUserBase(BaseModel):
    type_id: str
    type_name: UserType
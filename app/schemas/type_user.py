

from pydantic import BaseModel

from app.enums.type_user_enum import TypeUserEnum


class TypeUserBase(BaseModel):
    type_id: str
    type_name: TypeUserEnum
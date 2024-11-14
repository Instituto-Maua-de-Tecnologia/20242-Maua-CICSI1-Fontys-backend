
from pydantic import BaseModel


class UserTypeBase(BaseModel):
    user_type_id: str
    type_id: str
    user_id: str

from pydantic import BaseModel


class UserType(BaseModel):
    user_type_id: str
    type_id: str
    user_id: str

from pydantic import BaseModel


class UserType(BaseModel):
    type_id: str
    user_id: str
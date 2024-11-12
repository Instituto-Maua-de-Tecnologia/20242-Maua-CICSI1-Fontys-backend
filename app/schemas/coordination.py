

from pydantic import BaseModel


class Coordination(BaseModel):
    coordination_id: str
    user_id: str
    course_id: str
    semester: int
    year: int   
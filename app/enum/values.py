from sqlalchemy import Enum


class Values(Enum):
    POSSIBLE = "Possible",
    IMPOSITIVE = "Impossible",
    NEGOCIATED= "Negociated",
    DONE = "Done",
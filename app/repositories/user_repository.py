from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
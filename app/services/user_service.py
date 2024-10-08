from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        return UserRepository.create(self.db, user)
    
    def get_user(self, user_id: int):
        return UserRepository.get(self.db, user_id)

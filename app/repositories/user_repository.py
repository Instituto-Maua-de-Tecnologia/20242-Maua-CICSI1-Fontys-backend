from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    @staticmethod
    def create(db: Session, user: UserCreate):
        db_user = User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
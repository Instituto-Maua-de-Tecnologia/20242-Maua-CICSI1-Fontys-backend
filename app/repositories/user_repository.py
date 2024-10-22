from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        new_user = User(
            user_id=user.user_id,
            email=user.email,
            name=user.name,
            password=user.password,  # Aqui você deve garantir que o password seja criptografado
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

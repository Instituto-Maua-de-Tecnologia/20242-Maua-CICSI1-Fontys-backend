from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import User

class UserRepository:
    def create_user(user: User, db: Session) -> User:
        new_user = User(
            user_id=user.user_id,
            email=user.email,
            name=user.name,
            password=user.password,  # Aqui você deve garantir que o password seja criptografado
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

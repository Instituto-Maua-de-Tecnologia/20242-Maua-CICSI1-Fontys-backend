from sqlalchemy.orm import Session
from app.models.user import User  # Modelo do banco de dados
from app.domain.interfaces.repositories.user_repository_interface import IUserRepository
from app.domain.entities.user import UserEntity  # Entidade de domínio

class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> UserEntity:
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user:
            return UserEntity(
                id=db_user.id,
                name=db_user.name,
                email=db_user.email,
                password=db_user.hashed_password
            )
        return None

    def create_user(self, user: UserEntity) -> UserEntity:
        db_user = User(
            name=user.name,
            email=user.email,
            hashed_password=user.password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserEntity(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            password=db_user.hashed_password
        )
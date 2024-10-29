from app.repositories.user_repository import UserRepository
from app.schemas.user import User
from sqlalchemy.orm import Session
import bcrypt

class UserService:
    def __init__(self, user_repository: UserRepository, db: Session):
        self.user_repository = user_repository
        self.db = db

    def _hash_password(self, password: str) -> str:
        """Função para hash de senha"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def _validate_user(self, user: User):
        """Validações de usuário"""
        if not user.email or '@' not in user.email:
            raise ValueError("Email inválido.")
        if not user.name or len(user.name) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")

    def sign_up(self, user: User) -> User:
        """Método para registrar o usuário"""
        self._validate_user(user)
        user.password = self._hash_password(user.password)
        return self.user_repository.create_user(user, self.db)

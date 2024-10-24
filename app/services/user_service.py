from app.repositories.user_repository import UserRepository
from app.schemas.user import User
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user: User):
        # Aqui você pode adicionar lógica adicional, como validação ou criptografia de senha
        # Exemplo: criptografar senha
        self._validate_user(user)
        user.password = self._hash_password(user.password)
        return self.user_repository.create_user(user, db)

    def _hash_password(self, password: str) -> str:
        # Função para hash de senha, utilize uma lib como bcrypt
        import bcrypt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def _validate_user(self, user: User):
        # Adicione lógica de validação, como verificar se o e-mail já está em uso
        if not user.email or '@' not in user.email:
            raise ValueError("Email inválido.")
        if not user.name or len(user.name) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        
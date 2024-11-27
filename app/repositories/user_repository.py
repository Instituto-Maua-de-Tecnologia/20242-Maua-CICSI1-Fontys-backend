from sqlalchemy.orm import aliased
from sqlalchemy.orm import Session
from app.models.user_shipping import UserShipping
from app.models.users import User  # Modelo do banco de dados
from app.domain.interfaces.repositories.user_repository_interface import IUserRepository
from app.domain.entities.user_entity import UserEntity
from app.schemas.user import GetAllUsersResponseSchema  # Entidade de domínio

class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserEntity) -> UserEntity:
            db_user = User(
                name=user.name,
                photo=user.photo,
                notes=user.notes,
                microsoft_id=user.microsoft_id
            )
            try:
                self.db.add(db_user)
                self.db.commit()
                self.db.refresh(db_user)
            except Exception:
                self.db.rollback()
                raise
            return UserEntity(
                user_id=db_user.user_id,
                microsoft_id=db_user.microsoft_id,
                name=db_user.name,
                photo=db_user.photo,
                notes=db_user.notes
            )
            


    def get_all_users(self) -> list[GetAllUsersResponseSchema]:
        # Criar um alias para a tabela UserShipping, caso seja necessário
        user_shipping_alias = aliased(UserShipping)

        # Realizar a junção entre as tabelas User e UserShipping
        db_users = (
            self.db.query(User, user_shipping_alias.status)
            .join(user_shipping_alias, User.user_id == user_shipping_alias.user_id)
            .all()
        )
        
        # Mapeando os resultados para a estrutura de UserResponseSchema com status
        return [
            GetAllUsersResponseSchema(
                user_id=user.user_id,
                microsoft_id=user.microsoft_id,
                name=user.name,
                photo=user.photo,
                notes=user.notes,
                image_url=user.photo if user.photo else None,
                status=user_shipping_alias.status  # Pega o status da tabela UserShipping
            )
            for user, status in db_users
        ]

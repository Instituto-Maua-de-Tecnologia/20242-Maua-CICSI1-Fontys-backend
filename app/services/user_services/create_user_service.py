from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.domain.entities.user_entity import UserEntity

class CreateUserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def execute(self,
                    name: str,
                    microsoft_id: str = None,
                    photo: str = None,
                    notes: str = None
                    ) -> UserEntity:

        user = UserEntity(
            name=name,
            microsoft_id=microsoft_id or None,
            photo=photo,
            notes=notes
        )

        return self.repository.create_user(user)
        
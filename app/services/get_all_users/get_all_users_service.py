from app.repositories.user_repository import UserRepository


class GetAllUsersService:
    def __init__(self):
        self.user_repository = UserRepository()

    def execute(self):
        return self.user_repository.get_all_users()
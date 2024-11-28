from fastapi import HTTPException
from app.services.user_services.get_all_users_service import GetAllUsersService
from app.schemas.user import GetAllUsersResponseSchema


class GetAllUsersController:
    def __init__(self, service: GetAllUsersService):
        self.service = service

    def handle(self) -> list[GetAllUsersResponseSchema]:
        try:
            # Executa o serviço para buscar todos os usuários
            users = self.service.execute()
            
            # Mapeia os usuários para o schema de resposta
            return [
                GetAllUsersResponseSchema(
                    user_id=user.user_id,
                    microsoft_id=user.microsoft_id,
                    name=user.name,
                    photo=user.photo,
                    notes=user.notes,
                    status=user.status
                )
                for user in users
            ]

        except Exception as e:
            # Lança uma exceção HTTP em caso de erro inesperado
            raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")

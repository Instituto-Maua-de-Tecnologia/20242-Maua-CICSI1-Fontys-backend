from fastapi import HTTPException
from app.services.user_services.get_all_users_service import GetAllUsersService
from app.schemas.user import GetAllUsersResponseSchema


class GetAllUsersController:
    def __init__(self, service: GetAllUsersService):
        self.service = service

    def handle(self) -> list[GetAllUsersResponseSchema]:
        try:
            
            users = self.service.execute()
            
            
            return [
                GetAllUsersResponseSchema(
                    user_id=user.user_id,
                    microsoft_id=user.microsoft_id,
                    name=user.name,
                    photo=user.photo,
                    status=user.status
                )
                for user in users
            ]

        except Exception as e:
           
            raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")

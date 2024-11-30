from fastapi import HTTPException
from app.services.user_services.get_all_professors_service import GetAllProfessorsService
from app.schemas.user import GetAllProfessorsResponseSchema

class GetAllProfessorsController:
    def __init__(self, service: GetAllProfessorsService):
        self.service = service

    def handle(self) -> list[GetAllProfessorsResponseSchema]:
        try:
            
            users = self.service.execute()
            
            
            return [
                GetAllProfessorsResponseSchema(
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

from fastapi import HTTPException
from app.schemas.user import CreateUserSchema
from app.services.user_service import UserService

class CreateUserController:
    
    def __init__(self, service: UserService):
        self.service = service
        
    def handle(self, data: CreateUserSchema) -> dict:
        try:
            user = self.service.execute(
                name=data.name,
                microsoft_id=data.microsoft_id,
                photo=data.photo,
                notes=data.notes
            )
            return {"user_id": user.user_id, "message": "User created successfully"}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")
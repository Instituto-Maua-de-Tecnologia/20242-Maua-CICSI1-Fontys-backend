from app.models.user import User
from app.schemas.user import CreateUserRequest, CreateUserResponse
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

def create_user_controller(request: CreateUserRequest) -> CreateUserResponse:
    # Validações de campo
    if not request.email:
        raise HTTPException(status_code=400, detail="Email is required")
    if not request.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not request.password:
        raise HTTPException(status_code=400, detail="Password is required")
    if request.password != request.password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    try:
        # Instancia UserService e chama sign_up
        user_service = UserService(UserRepository())
        user = user_service.sign_up(User(email=request.email, name=request.name, password=request.password))
        return JSONResponse(status_code=201, content={
            "message": "Criado com sucesso",
            "User": user     
        })
    
    except Exception as e:
        # Exemplo de um erro genérico para caso de falha no serviço
        raise HTTPException(status_code=500, detail=str(e))

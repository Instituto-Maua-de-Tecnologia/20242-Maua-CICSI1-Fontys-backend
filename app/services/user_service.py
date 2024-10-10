import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def login():
        return {
            "login_url": f"{settings.AUTH_URL}?client_id={settings.CLIENT_ID}&response_type=code&redirect_uri={settings.REDIRECT_URI}&response_mode=query&scope={settings.SCOPE}"
        }

    async def auth_callback(self, code: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(settings.TOKEN_URL, data={
                "client_id": settings.CLIENT_ID,
                "client_secret": settings.CLIENT_SECRET,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": settings.REDIRECT_URI,
                "scope": settings.SCOPE
            })
            token_data = response.json()
            access_token = token_data.get("access_token")

            if not access_token:
                raise HTTPException(status_code=400, detail="Failed to retrieve access token")

            user_info = await self.get_user_info(access_token)
            return await UserRepository.create_or_update_user(user_info, self.db)

    async def get_user_info(self, access_token: str):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://graph.microsoft.com/v1.0/me", headers={
                "Authorization": f"Bearer {access_token}"
            })
            return response.json()

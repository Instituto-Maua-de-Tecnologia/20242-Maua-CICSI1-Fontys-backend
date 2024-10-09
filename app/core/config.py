from pydantic import BaseSettings

class Settings(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URI: str = "http://localhost:8000/auth/callback"
    AUTH_URL: str = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    TOKEN_URL: str = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    SCOPE: str = "openid profile email"
    DATABASE_URL: str = "postgresql://postgres:postgres@db/postgres"

    class Config:
        env_file = ".env"

settings = Settings()
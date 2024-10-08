from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@db/postgres"

    class Config:
        env_file = ".env"

settings = Settings()
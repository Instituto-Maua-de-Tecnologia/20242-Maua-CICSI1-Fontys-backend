from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://fontys:fontys@db/fontys"

    class Config:
        env_file = ".env"

settings = Settings()
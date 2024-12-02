import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL_AIVEN: str
    API_KEY: str
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings(
    DATABASE_URL_AIVEN=os.environ.get('DATABASE_URL_AIVEN'),
    API_KEY=os.environ.get('API_KEY'),
    PORT=os.environ.get('PORT')
)

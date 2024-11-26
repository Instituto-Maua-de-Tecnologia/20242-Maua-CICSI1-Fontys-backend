import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL_AIVEN: str

    class Config:
        env_file = ".env"

settings = Settings(
    DATABASE_URL_AIVEN=os.environ.get('DATABASE_URL_AIVEN')
)
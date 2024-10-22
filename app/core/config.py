from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_URL_AIVEN: str

    class Config:
        env_file = ".env"  # Carrega variáveis do arquivo .env

# Instância global de configurações
settings = Settings()

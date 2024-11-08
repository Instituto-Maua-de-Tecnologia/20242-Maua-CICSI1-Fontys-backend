
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL do banco de dados com base no ambiente
environment = os.getenv("ENVIRONMENT", "development")  # Default para 'development'
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") if environment == "development" else os.getenv("DATABASE_URL_AIVEN")

# Verifica se a URL do banco de dados está configurada
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("A URL do banco de dados não foi encontrada. Verifique suas variáveis de ambiente.")

# Criação da engine do SQLAlchemy usando a URL escolhida
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)

# Criando a sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos do SQLAlchemy
Base = declarative_base()

def get_db():
    db = SessionLocal()
    print("Conexão com o banco de dados estabelecida.", db)
    return db
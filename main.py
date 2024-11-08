import logging
import os
from fastapi import FastAPI
from app.api.v1.routes import user
import psycopg2
import uvicorn
from dotenv import load_dotenv
from urllib.parse import urlparse

from app.db.session import get_db

# Carregar o arquivo .env
load_dotenv()

# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializando o aplicativo FastAPI
app = FastAPI()

# Incluindo o router do usuário
app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    logger.info("Acessando a raiz")
    get_db()
    return {"API OK!"}

def check_db_version():
    try:
        # Carregar a URL do banco de dados
        db_aiven_url = os.getenv('DATABASE_URL_AIVEN')
        if not db_aiven_url:
            raise ValueError("A variável DATABASE_URL_AIVEN não foi definida.")

        # Verificar se a URL está em um formato válido
        if not db_aiven_url.startswith("postgres://") and not db_aiven_url.startswith("postgresql://"):
            raise ValueError("A URL do banco de dados não está no formato correto.")

        # Parse da URL
        result = urlparse(db_aiven_url)

        # Conectar ao banco com parâmetros separados
        with psycopg2.connect(
            dbname=result.path[1:],  # Remove a barra inicial do caminho
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port,
            sslmode="require"
        ) as conn:
            with conn.cursor() as cur:
                query_sql = 'SELECT VERSION()'
                cur.execute(query_sql)
                version = cur.fetchone()[0]
                logger.info(f"Versão do banco de dados: {version}")

    except ValueError as ve:
        logger.error(ve)
    except psycopg2.Error as e:
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}", exc_info=True)

if __name__ == "__main__":
    check_db_version()
    uvicorn.run(app, host="127.0.0.1", port=8000)

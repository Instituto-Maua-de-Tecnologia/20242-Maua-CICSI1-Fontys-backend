
import logging
from fastapi import FastAPI
from app.api.v1 import user

# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def read_root():
    logger.info("Acessando a raiz")
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
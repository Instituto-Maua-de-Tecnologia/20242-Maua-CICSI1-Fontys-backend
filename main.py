from fastapi import FastAPI
from app.api.v1.routes import user  


# Inicializando o aplicativo FastAPI
app = FastAPI()

# Incluindo o router do usuário
app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    return {"API OK!"}



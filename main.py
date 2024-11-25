from fastapi import FastAPI
from app.api.v1.routes import user
import uvicorn

# Inicializando o aplicativo FastAPI
app = FastAPI()

# Incluindo o router do usuário
app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    return {"API OK!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)
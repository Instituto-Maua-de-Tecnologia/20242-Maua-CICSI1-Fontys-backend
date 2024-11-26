from fastapi import FastAPI
from app.api.v1.routes import user  

app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="API for managing users."
)

app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

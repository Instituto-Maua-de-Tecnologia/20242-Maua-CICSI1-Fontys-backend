from fastapi import FastAPI
from app.api.v1.routes import user
from app.core.database import Base, engine
from app.models import users, user_types, type_users  


def init_models():
    Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="API for managing users."
)


init_models()


app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}
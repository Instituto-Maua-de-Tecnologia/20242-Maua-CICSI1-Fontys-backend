from fastapi import FastAPI
from app.api.v1.routes import user
from app.api.v1.routes import availability
from app.api.v1.routes import schedule
from app.api.v1.routes import slots
import uvicorn
from app.core.database import Base, engine

def init_models():
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="API for managing users."
)

init_models()

app.include_router(user.router, prefix="/api", tags=["users"])
app.include_router(availability.router, prefix="/api", tags=["availability"])
app.include_router(schedule.router, prefix="/api", tags=["schedule"])
app.include_router(slots.router, prefix="/api", tags=["slots"])

@app.get("/")
async def read_root():
    return {"message": "API is running successfully!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.0", port=8000)

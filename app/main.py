from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def root():
    return {"message": "User Management Service is running"}

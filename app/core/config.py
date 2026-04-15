from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Les Marinettes User Management"
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()

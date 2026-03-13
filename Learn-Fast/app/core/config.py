# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These must match the names in your .env file or Docker environment
    DATABASE_URL: str = "postgresql://postgres:password123@localhost:5432/learning_db"
    
    # Automatically load from a .env file if it exists
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

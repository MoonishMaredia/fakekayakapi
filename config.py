from pydantic import BaseSettings

class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "https://localhost:3000", "https://fakekayaksite.onrender.com", "http://fakekayaksite.onrender.com"]

    class Config:
        env_file = ".env"

settings = Settings()
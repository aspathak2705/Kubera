import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Kubera")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
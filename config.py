import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_USERNAME: str = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_DATABASE: str = os.getenv("DB_DATABASE")

    SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"


settings = Settings()
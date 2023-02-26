from os import environ

from dotenv import load_dotenv
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

load_dotenv()

class DefaultSettings(BaseSettings):
    
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PRFIX", "")
    APP_HOST: str = environ.get("APP_HOST", "http://localhost")
    APP_PORT: int = int(environ.get("APP_PORT", "80"))
    
    POSTGRES_DB: str = environ.get("POSTGRES_DB", "db")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432"))
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "postgres")
    
    @property
    def database_settings(self) -> dict:
        return {
            "database": self.POSTGRES_DB,
            "host" : self.POSTGRES_HOST,
            "port" : self.POSTGRES_PORT,
            "user" : self.POSTGRES_USER,
            "password" : self.POSTGRES_PASSWORD,
        }
        
    @property
    def database_uri_async(self) -> str:
        return (
            "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
            .format(**self.database_settings)
        )
        
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
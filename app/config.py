from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: Literal["local", "dev", "staging", "prod"] = "local"
    DEBUG: bool = False
    TESTING: bool = False
    DATABASE_URL: PostgresDsn
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()

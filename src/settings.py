from functools import lru_cache
from typing import Literal

from dotenv import load_dotenv
from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file="./.env", env_ignore_empty=True, extra="ignore"
    )
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    SECRET_KEY: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    SUPERUSER_EMAIL: EmailStr
    SUPERUSER_USERNAME: str
    SUPERUSER_PASSWORD: str

    YANDEX_CLIENT_ID: str
    YANDEX_SECRET_KEY: str
    YANDEX_TOKEN_URL: str
    YANDEX_REDIRECT_URI: str

    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def yandex_redirect_url(self) -> str:
        return f"https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&force_confirm=yes"  # noqa E3051

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


@lru_cache
def get_settings():
    """Returns cached settings instance."""
    return Settings()


settings = get_settings()

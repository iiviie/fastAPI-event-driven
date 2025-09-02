from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Environment
    environment: Environment = Field(default=Environment.DEV, description="Environment")

    # Application
    app_name: str = Field(default="Auth Microservice", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    debug: bool = Field(default=True, description="Debug mode")
    
    # Server
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    
    # Database
    database_url: str = Field(
        default="postgresql+asyncpg://auth_user:auth_password@localhost:5432/auth_db",
        description="Database URL"
    )
    
    # Redis
    redis_url: str = Field(
        default="redis://localhost:6379/0",
        description="Redis URL"
    )
    
    # Security
    secret_key: str = Field(
        default="babysharkdoodoo",
        description="Secret key for JWT tokens"
    )
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration in minutes"
    )
    
    # CORS
    allowed_origins: list[str] = Field(
        default=["http://localhost:3000"], description="Allowed CORS origins"
    )
    
    # Logging
    log_level: str = Field(default="INFO", description="Log level")

    @property
    def is_dev(self) -> bool:
        return self.environment == Environment.DEV

    @property
    def is_prod(self) -> bool:
        return self.environment == Environment.PROD


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
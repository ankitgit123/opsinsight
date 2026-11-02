

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "OpsInsight"
    app_env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    # Database
    database_url: str

    # LLM
    llm_provider: str = "ollama"
    llm_model: str = "qwen3:4b"
    llm_base_url: str = "http://host.docker.internal:11434/v1"
    llm_api_key: str = "ollama"

    # Agent
    agent_framework: str = "native"
    agent_max_steps: int = 5
    agent_timeout_seconds: int = 60

    # Upload
    max_upload_size_mb: int = 20

    # Observability
    langfuse_enabled: bool = False
    langfuse_secret_key: str = ""
    langfuse_public_key: str = ""
    langfuse_host: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings()-> Settings:
    return Settings()


settings = get_settings()
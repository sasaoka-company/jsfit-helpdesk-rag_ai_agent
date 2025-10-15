from pydantic_settings import BaseSettings, SettingsConfigDict
from src.config import LLM_MODEL


class Settings(BaseSettings):
    openai_api_key: str
    openai_api_base: str
    openai_model: str = LLM_MODEL

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

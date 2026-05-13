"""
Application configuration using pydantic-settings
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    deepseek_api_key: str
    deepseek_api_url: str = "https://api.deepseek.com"

    model_flash: str = "deepseek-v4-flash"
    model_pro: str = "deepseek-v4-pro"


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str
    SPARK_URL: str
    SPARK_DB_DRIVER: str

    model_config = SettingsConfigDict(".env")

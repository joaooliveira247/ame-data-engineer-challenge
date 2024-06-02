from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SPARK_URL: str
    SPARK_DB_DRIVER: str
    APP_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

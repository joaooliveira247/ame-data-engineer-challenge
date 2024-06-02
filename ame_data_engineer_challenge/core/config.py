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

    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()

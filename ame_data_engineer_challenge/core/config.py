from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    SPARK_URL: str
    SPARK_DB_DRIVER: str
    APP_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    BASE_DIR: Path = Path(__file__).parent.parent
    DOLLAR_EXCHANGE: float = 3.81
    YEAR_MONTHS: int = 12

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def db_conn_info(self) -> str:
        return (
            f"dbname={self.DB_NAME} user={self.DB_USER} password="
            f"{self.DB_PASS} host={self.DB_HOST} port={self.DB_PORT}"
        )


settings = Settings()

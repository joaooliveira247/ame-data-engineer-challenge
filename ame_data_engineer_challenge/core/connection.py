from pyspark.sql import SparkSession, DataFrame
from core.config import settings


def get_session() -> SparkSession:
    return (
        SparkSession.builder.master(settings.SPARK_URL)
        .appName("AmeChallenge")
        .config(
            "spark.jars",
            f"{settings.BASE_DIR / 'drivers' / 'postgresql-42.7.3.jar'}",
        )
        .getOrCreate()
    )


def save_on_database(df: DataFrame, table_name: str) -> None:
    properties: dict[str, str] = {
        "user": f"{settings.DB_USER}",
        "password": f"{settings.DB_PASS}",
        "driver": settings.SPARK_DB_DRIVER,
    }

    df.write.jdbc(
        url=f"jdbc:postgresql://{settings.DB_HOST}:{settings.DB_PORT}/"
        f"{settings.DB_NAME}",
        table=table_name,
        mode="append",
        properties=properties,
    )

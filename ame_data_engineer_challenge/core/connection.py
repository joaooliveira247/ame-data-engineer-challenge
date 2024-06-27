from core.config import settings
from pyspark.sql import DataFrame, SparkSession

PROPERTIES: dict[str, str] = {
    "user": f"{settings.DB_USER}",
    "password": f"{settings.DB_PASS}",
    "driver": settings.SPARK_DB_DRIVER,
}


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
    df.write.jdbc(
        url=f"jdbc:postgresql://{settings.DB_HOST}:{settings.DB_PORT}/"
        f"{settings.DB_NAME}",
        table=table_name,
        mode="append",
        properties=PROPERTIES,
    )


def get_from_database(
    spark_session: SparkSession, table_name: str
) -> DataFrame:
    return spark_session.read.jdbc(
        url=f"jdbc:postgresql://{settings.DB_HOST}:{settings.DB_PORT}/"
        f"{settings.DB_NAME}",
        table=table_name,
        properties=PROPERTIES,
    )

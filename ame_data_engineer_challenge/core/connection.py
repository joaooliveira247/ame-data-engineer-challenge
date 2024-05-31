from pyspark.sql import SparkSession
from core.config import settings


def get_session() -> SparkSession:
    return (
        SparkSession.builder.master(settings.SPARK_URL)
        .appName("AmeChallenge")
        .getOrCreate()
    )

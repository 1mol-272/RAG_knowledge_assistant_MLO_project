"""SparkSession helper.

Usage:
    from utils_spark_session import get_spark
    spark = get_spark("my-app")
"""

from pyspark.sql import SparkSession


def get_spark(app_name: str = "app") -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)
        .getOrCreate()
    )

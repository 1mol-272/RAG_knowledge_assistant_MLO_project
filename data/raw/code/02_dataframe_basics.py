from pyspark.sql.functions import col
from utils_spark_session import get_spark


def main():
    spark = get_spark("df-basics")

    df = (spark.read
          .option("header", True)
          .option("inferSchema", True)
          .csv("data.csv"))

    df.printSchema()

    out = (df.select("id", "name", "age")
             .filter(col("age") > 30)
             .orderBy(col("age").desc()))

    out.show(20, truncate=False)


if __name__ == "__main__":
    main()

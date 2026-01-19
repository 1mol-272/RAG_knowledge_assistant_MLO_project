from pyspark.sql.functions import col, count, avg
from utils_spark_session import get_spark


def main():
    spark = get_spark("joins-aggs")

    movies = (spark.read.option("header", True).option("inferSchema", True)
              .csv("movies.csv"))
    ratings = (spark.read.option("header", True).option("inferSchema", True)
               .csv("ratings.csv"))

    # Example: average rating per movie
    stats = (ratings.groupBy("movieId")
             .agg(count("rating").alias("n"), avg("rating").alias("mean")))

    # Join back to movie titles
    res = (movies.join(stats, on="movieId", how="left")
           .orderBy(col("n").desc_nulls_last()))

    res.show(20, truncate=False)


if __name__ == "__main__":
    main()

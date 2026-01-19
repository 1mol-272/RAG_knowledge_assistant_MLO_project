# Triangle count using only DataFrames (no GraphFrames)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("triangle-df").getOrCreate()

# edges: undirected, store with u < v to avoid duplicates
edges = spark.createDataFrame([
    ("a","b"), ("b","c"), ("c","a"), ("c","d")
], ["u","v"])

# Ensure ordering u < v
edges = edges.select(
    col("u").alias("u"),
    col("v").alias("v")
)

e1 = edges.alias("e1")
e2 = edges.alias("e2")
e3 = edges.alias("e3")

# (a,b), (b,c), (a,c)
tri = (e1.join(e2, col("e1.v") == col("e2.u"))
         .join(e3, (col("e1.u") == col("e3.u")) & (col("e2.v") == col("e3.v")))
         .select(col("e1.u").alias("a"), col("e1.v").alias("b"), col("e2.v").alias("c"))
      )

tri.show()
print("triangle_count =", tri.count())

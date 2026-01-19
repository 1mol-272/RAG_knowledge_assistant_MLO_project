# GraphFrames PageRank template (PySpark)
# Requires: from graphframes import GraphFrame

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from graphframes import GraphFrame

spark = SparkSession.builder.appName("graphframes-pagerank").getOrCreate()

# Example vertices and edges
v = spark.createDataFrame([
    ("a",), ("b",), ("c",), ("d",)
], ["id"])

e = spark.createDataFrame([
    ("a","b"), ("b","c"), ("c","a"), ("c","d")
], ["src","dst"])

g = GraphFrame(v, e)

pr = g.pageRank(resetProbability=0.15, maxIter=10)

pr.vertices.select("id", col("pagerank").alias("pr")).orderBy(col("pr").desc()).show()

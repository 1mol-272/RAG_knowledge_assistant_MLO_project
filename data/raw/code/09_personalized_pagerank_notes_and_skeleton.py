"""Personalized PageRank (PPR) skeleton.

GraphFrames doesn't expose built-in PPR in all versions.
Common exam approach:
- implement power iteration with teleport vector focusing on a seed node(s)
- use DataFrame operations: join edges with current rank, aggregate, apply damping

This file provides a DataFrame-style skeleton.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ppr").getOrCreate()

# edges: (src, dst)
edges = spark.createDataFrame([
    ("u1", "u2"),
    ("u2", "u3"),
    ("u3", "u1"),
], ["src", "dst"])

seed = "u1"
d = 0.85  # damping factor
max_iter = 10

# out-degree
outdeg = edges.groupBy("src").agg(F.count("dst").alias("outdeg"))

# initialize ranks
verts = edges.select(F.col("src").alias("id")).union(edges.select(F.col("dst").alias("id"))).distinct()
ranks = verts.withColumn("rank", F.when(F.col("id") == seed, F.lit(1.0)).otherwise(F.lit(0.0)))

for _ in range(max_iter):
    # distribute rank along outgoing edges
    contrib = (edges.join(outdeg, on="src", how="left")
                    .join(ranks.select(F.col("id").alias("src"), "rank"), on="src", how="left")
                    .withColumn("contrib", F.col("rank") / F.col("outdeg"))
                    .groupBy("dst").agg(F.sum("contrib").alias("sum_contrib"))
              )

    # new rank = d * incoming + (1-d) * personalization
    ranks = (verts.join(contrib, verts.id == contrib.dst, how="left")
                  .drop("dst")
                  .fillna({"sum_contrib": 0.0})
                  .withColumn(
                      "rank",
                      F.lit(d) * F.col("sum_contrib") + F.lit(1.0 - d) * F.when(F.col("id") == seed, F.lit(1.0)).otherwise(F.lit(0.0))
                  )
                  .select("id", "rank")
            )

ranks.orderBy(F.desc("rank")).show()

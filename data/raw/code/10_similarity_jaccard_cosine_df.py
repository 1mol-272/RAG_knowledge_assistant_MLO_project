"""Similarity computations in DataFrames.

Exam patterns:
- build user-item interactions
- compute co-occurrence counts via self-join
- Jaccard(u,v) = |Iu ∩ Iv| / |Iu ∪ Iv|

This shows Jaccard for item-item similarity.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("similarity").getOrCreate()

# interactions: (user, item)
ui = spark.createDataFrame([
    ("u1", "i1"), ("u1", "i2"),
    ("u2", "i1"), ("u2", "i3"),
    ("u3", "i2"), ("u3", "i3"),
], ["user", "item"])

# item -> users set size
item_deg = ui.groupBy("item").agg(F.countDistinct("user").alias("deg"))

# co-occurrence between items: users who interacted with both
pairs = (ui.alias("a")
         .join(ui.alias("b"), on=F.col("a.user") == F.col("b.user"))
         .where(F.col("a.item") < F.col("b.item"))
         .groupBy(F.col("a.item").alias("i"), F.col("b.item").alias("j"))
         .agg(F.countDistinct(F.col("a.user")).alias("inter"))
)

pairs = (pairs
         .join(item_deg.withColumnRenamed("item","i").withColumnRenamed("deg","deg_i"), on="i")
         .join(item_deg.withColumnRenamed("item","j").withColumnRenamed("deg","deg_j"), on="j")
         .withColumn("union", F.col("deg_i") + F.col("deg_j") - F.col("inter"))
         .withColumn("jaccard", F.col("inter") / F.col("union"))
)

pairs.orderBy(F.desc("jaccard")).show(truncate=False)

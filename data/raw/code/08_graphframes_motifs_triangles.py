# Motif finding: triangles (GraphFrames)

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from graphframes import GraphFrame

spark = SparkSession.builder.appName("graphframes-motifs").getOrCreate()

v = spark.createDataFrame([("a",), ("b",), ("c",)], ["id"])
e = spark.createDataFrame([("a","b"),("b","c"),("c","a")], ["src","dst"])
g = GraphFrame(v, e)

motifs = g.find("(a)-[e1]->(b); (b)-[e2]->(c); (c)-[e3]->(a)")
# Optional: avoid duplicates by ordering ids
motifs = motifs.where(expr("a.id < b.id AND b.id < c.id"))

motifs.selectExpr("a.id as a", "b.id as b", "c.id as c").show()

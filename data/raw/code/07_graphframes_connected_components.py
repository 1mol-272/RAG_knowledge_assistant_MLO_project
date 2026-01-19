# Connected Components template (GraphFrames)

from pyspark.sql import SparkSession
from graphframes import GraphFrame

spark = SparkSession.builder.appName("graphframes-cc").getOrCreate()

v = spark.createDataFrame([(1,), (2,), (3,), (4,), (5,)], ["id"])
e = spark.createDataFrame([(1,2),(2,3),(4,5)], ["src","dst"])

g = GraphFrame(v, e)

cc = g.connectedComponents()  # returns (id, component)
cc.orderBy("component", "id").show()

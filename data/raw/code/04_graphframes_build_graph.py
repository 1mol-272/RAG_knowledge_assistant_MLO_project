"""Build a GraphFrame from vertices/edges DataFrames.

Requires graphframes installed in the environment.
"""

from utils_spark_session import get_spark
from pyspark.sql import functions as F


def main():
    spark = get_spark("graphframes-build")

    # Minimal example graph
    v = spark.createDataFrame(
        [("a", "Alice", 34), ("b", "Bob", 36), ("c", "Charlie", 30)],
        ["id", "name", "age"],
    )

    e = spark.createDataFrame(
        [("a", "b", "friend"), ("b", "c", "follow"), ("a", "c", "follow")],
        ["src", "dst", "relationship"],
    )

    from graphframes import GraphFrame
    g = GraphFrame(v, e)

    g.vertices.show()
    g.edges.show()
    g.triplets.show(truncate=False)


if __name__ == "__main__":
    main()

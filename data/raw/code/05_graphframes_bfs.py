from utils_spark_session import get_spark


def main():
    spark = get_spark("graphframes-bfs")

    from graphframes import GraphFrame

    v = spark.createDataFrame(
        [("a", "Alice", 34), ("b", "Bob", 36), ("c", "Charlie", 30), ("d", "David", 29)],
        ["id", "name", "age"],
    )
    e = spark.createDataFrame(
        [("a", "b", "friend"), ("b", "c", "follow"), ("c", "d", "follow"), ("a", "d", "follow")],
        ["src", "dst", "relationship"],
    )

    g = GraphFrame(v, e)

    # Find shortest paths from Alice to nodes with age < 32
    paths = g.bfs("name = 'Alice'", "age < 32", edgeFilter="relationship != 'friend'", maxPathLength=3)
    paths.show(truncate=False)


if __name__ == "__main__":n    main()

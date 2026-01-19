# Exam Syllabus (Spark DataFrames + Graphs)

> This is a consolidated syllabus built from the provided course materials.

## A. Spark fundamentals
- Big Data context (6Vs), Spark ecosystem.
- Spark architecture: driver, executors, cluster manager; basic execution model.
- RDD: transformations vs actions, lineage/DAG, fault tolerance.

## B. Spark SQL & DataFrames (PySpark)
- SparkSession and reading files (CSV/JSON/Parquet).
- Schema: inferSchema vs explicit schema; `printSchema`.
- Core operations:
  - `select`, `withColumn`, `filter/where`, `orderBy`, `drop`, `distinct`.
  - Aggregations: `groupBy().agg(...)`, `count`, `collect_list`.
  - Joins: inner/left/right/full; cross join; join keys.
  - Exploding arrays (`explode`), splitting strings (`split`), string funcs.
- UDFs: when to use, performance caveats.

## C. Graph theory basics (needed for algorithms)
- Directed vs undirected graphs, simple vs multigraph vs pseudograph.
- Degree, in-degree/out-degree, adjacency, paths.
- Types of networks: random, small-world, scale-free.

## D. Graph algorithms (concept + implementation patterns)
- Centrality: degree, closeness, betweenness, eigenvector.
- PageRank (standard + personalized): definition, damping, convergence.
- Connected components (undirected) and strongly connected components (directed).
- Triangle counting and clustering coefficient.
- BFS/shortest paths (unweighted vs weighted intuition).

## E. GraphFrames (Spark package)
- Property graph model: vertices DataFrame + edges DataFrame.
- Graph algorithms: BFS, connected components, SCC, LPA, PageRank, shortestPaths, triangleCount.
- Graph queries/pattern matching with `find()` (motifs).
- Advanced: `aggregateMessages`, Pregel-like API.

## F. Recommendation mini-case (TME)
- Construct a heterogeneous graph (users, artists, songs) with weighted edges.
- Personalized PageRank (PPR) to rank songs for a user.

## What to be able to do in the exam
- Explain the concept (what/why), then write short correct PySpark/GraphFrames code.
- Given a small graph, do 1–2 PageRank/PPR iterations by hand.
- Interpret outputs (e.g., components, pagerank weights, BFS paths).

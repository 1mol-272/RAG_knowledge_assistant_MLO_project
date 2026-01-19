# Knowledge Map / Syllabus Outline (Spark DataFrames + Graphs + GraphFrames)

This file is designed for **high-level / abstract questions**:
- "How should I revise?" / "What's the outline?" / "What are the key topics?"
- "What might be on the exam?" / "Give me a study plan"

It is written as a **tree of topics**. Each node includes bilingual keywords to improve retrieval.

---

## A) Spark Fundamentals (基础)
### A1) Spark architecture & execution
Keywords: Driver, Executor, Job, Stage, Task, DAG, lazy evaluation, shuffle, partition
- What runs on driver vs executors
- Lazy evaluation and the execution plan (logical/physical)
- Narrow vs wide transformations, shuffles, stages
- Partitions and parallelism; how repartition/coalesce changes partitions

### A2) RDD basics (if covered)
Keywords: RDD, map, flatMap, reduceByKey, groupByKey, actions, transformations
- When RDD is needed vs DataFrame
- Key-value operations and common pitfalls (groupByKey vs reduceByKey)

### A3) Data sources & I/O
Keywords: read, write, parquet, csv, json, schema, inferSchema
- Explicit schema vs inferred schema
- Partitioned datasets, save modes

---

## B) Spark DataFrames & SQL
### B1) DataFrame API fundamentals
Keywords: select, withColumn, filter/where, explode, when, cast, UDF
- Column expressions (no Python loops in distributed operations)
- Common patterns: parsing, normalization, explode arrays

### B2) Aggregations & Window functions
Keywords: groupBy, agg, count, sum, avg, distinct, window, over, partitionBy, orderBy
- Aggregation semantics and null behavior
- Window functions for ranking, moving averages, sessionization (if seen)

### B3) Joins
Keywords: join, inner, left, right, full, semi, anti, broadcast join
- Join keys, duplicates, skew
- When/why to broadcast; join order; common mistakes

### B4) Performance / Optimization (closed-book exam often tests intuition)
Keywords: cache/persist, checkpoint, explain, catalyst, tungsten, shuffle partitions
- What triggers a shuffle
- cache vs persist, when caching helps
- How to read an `explain()` plan at a high level

---

## C) Graphs with DataFrames (Graphs-as-DataFrames)
### C1) Graph modelling
Keywords: vertices, edges, directed, undirected, weighted, adjacency list, incidence
- Vertex table: id + attributes
- Edge table: src, dst + attributes
- Building a graph from interaction logs

### C2) Typical tasks
Keywords: degree, indegree, outdegree, path, triangle, motifs
- Degree computation using aggregations
- Motifs / patterns as joins

---

## D) GraphFrames (Spark)
### D1) GraphFrames basics
Keywords: GraphFrame, vertices, edges, caching, motif finding
- Constructing a GraphFrame from two DataFrames
- Persisting vertices/edges and graph

### D2) Built-in algorithms
Keywords: PageRank, ConnectedComponents, BFS, ShortestPaths, TriangleCount
- Inputs/outputs of each algorithm (what columns appear)
- Parameters to remember (maxIter, resetProbability, etc.)

### D3) Motif finding
Keywords: motifs, pattern language, g.find("(a)-[e]->(b)")
- How motif patterns map to returned DataFrames

---

## E) Recommendation / Similarity (if in materials)
### E1) Similarity via DataFrames
Keywords: Jaccard, cosine, co-occurrence, pairwise similarity
- Build user-item sets, compute intersections/unions with joins

### E2) Personalized PageRank (PPR)
Keywords: random walk, restart probability, personalized pagerank
- Intuition: bias walks from a seed node
- Implementation idea: iterative propagation + normalization

---

## F) Exam-oriented outputs (what you should be able to do)
### F1) Explain (简答题)
- Define concepts precisely (e.g., shuffle, broadcast join)
- Compare alternatives (RDD vs DF; cache vs persist)

### F2) Coding (编程题)
- Write DataFrame code for join/agg/window
- Build GraphFrame and run BFS/PageRank/CC
- Write motifs/triangle-style queries

### F3) MCQ (选择题)
- Recognize which operation causes shuffle
- Identify correct API usage and output schema

---

## Cross-reference hints
- For Spark DF details: see `data/raw/notes/03_spark_dataframes.md`
- For GraphFrames algorithms: see `data/raw/notes/06_graphframes_api_motifs.md` and `data/raw/notes/05_graph_algorithms_pagerank_bfs_cc.md`

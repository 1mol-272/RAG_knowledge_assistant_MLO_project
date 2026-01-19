# Common Exam Pitfalls (Spark + Graph)

## Spark
- Confusing **transformations** vs **actions**.
- Forgetting that `cache()` is lazy.
- Misunderstanding join output columns (duplicate names, need `alias`).
- Not handling nulls after joins.
- Using `collect()` on large datasets.
- Skew in groupBy/join -> timeouts.

## DataFrames vs RDD
- DataFrames are optimized by Catalyst; prefer them for SQL-like tasks.
- RDD is lower-level; you manage schema and optimization manually.

## Graph
- Directed vs undirected: PageRank uses direction; CC usually undirected.
- BFS/shortest path: BFS works only for unweighted; for weighted use Dijkstra.
- Triangle counting: must avoid double-counting by ordering constraints.

## GraphFrames
- Vertex column name must be `id` (default) unless configured.
- Edge columns must include `src`, `dst`.
- Motif `find()` returns columns with nested structs; you often need `.selectExpr`.

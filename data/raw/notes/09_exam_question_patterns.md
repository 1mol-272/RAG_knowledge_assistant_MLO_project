# Typical Exam Question Patterns (and what they test)

## Spark DataFrames
- “Write a query that…”: projection/filter/orderBy/groupBy/joins.
- “Explain why collect() is dangerous.”
- “Difference between RDD and DataFrame, and why Catalyst helps.”

## Graph algorithms
- Define degree/in-degree/out-degree/path.
- Distinguish: connected vs strongly connected components.
- Explain PageRank and damping; write the iterative equation.
- BFS vs Dijkstra; unweighted vs weighted shortest paths.
- Triangle counting: why ordering avoids double counting.

## GraphFrames
- Build vertices/edges DataFrames and create a GraphFrame.
- Use `find()` motif to express a pattern.
- Run `bfs` or `pageRank` and interpret results.

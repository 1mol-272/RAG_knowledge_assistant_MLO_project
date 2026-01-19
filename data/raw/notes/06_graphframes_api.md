# GraphFrames (Spark) — API & Mental Model

## Why GraphFrames
- Graphs are hard for pure data-parallel models (irregular structure, shuffles per iteration).
- GraphFrames gives a **DataFrame API** for graph queries + algorithms.

## Data model
- `vertices` DataFrame: **one vertex per row**, must have `id` column.
- `edges` DataFrame: **one edge per row**, must have `src`, `dst` columns.
- `triplets`: joined view (src vertex + edge + dst vertex).

## Common API calls
- Graph queries / patterns (motifs): `g.find("(a)-[e]->(b); (b)-[e2]->(c)")`
- Degrees: `g.inDegrees`, `g.outDegrees`, `g.degrees`
- BFS: `g.bfs(fromExpr, toExpr, edgeFilter=None, maxPathLength=10)`

## Algorithms (often asked)
- `pageRank(...)`, `connectedComponents()`, `stronglyConnectedComponents(maxIter)`,
  `shortestPaths(landmarks)`, `triangleCount()`, `labelPropagation(maxIter)`

## Building your own algorithm
- `aggregateMessages(...)` (message passing)
- DataFrame-based `Pregel` API (`graphframes.lib.Pregel`)

## Motif constraints
- You cannot have completely anonymous edges like `()-[]->()` with no named element.
- Negated edges cannot be named.

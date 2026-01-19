# Graph Algorithms Cheat Sheet (Definitions + What to memorize)

## Core definitions
- Graph: G=(V,E), directed/undirected, weighted/unweighted.
- Degree: in-degree/out-degree for directed.
- Path, walk, cycle, simple path.

## BFS / shortest path
- BFS gives shortest path in **unweighted** graphs.
- Complexity: O(|V|+|E|) with adjacency list.

## Connected components
- Undirected CC: nodes connected by some path.
- Algorithm idea (distributed): label propagation / union-find style iterations.

## PageRank
- Random surfer model: PR(v) = (1-d)/|V| + d * sum_{u->v} PR(u)/outdeg(u)
- d (damping) typically 0.85
- Convergence: iterate until delta < eps or maxIter.

## Triangle count
- Triangle: 3-cycle (undirected).
- DataFrame approach: self-joins on edges with ordering constraints.

## Motifs (GraphFrames)
- Use pattern matching to find subgraphs, e.g. triangles: `(a)-[e1]->(b); (b)-[e2]->(c); (c)-[e3]->(a)`

## Personalized PageRank (PPR)
- Similar to PageRank but teleport to a **seed set** S.
- Use for recommendations: “items close to my seed nodes”.

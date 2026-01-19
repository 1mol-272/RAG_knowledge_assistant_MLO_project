# Graph Algorithms & Math You Should Be Comfortable With

## Centralities (conceptual)
- Degree centrality: number of neighbors
- Closeness: inverse of sum of shortest-path distances to others
- Betweenness: fraction of shortest paths that pass through a node
- Eigenvector centrality: importance influenced by important neighbors

## PageRank (core formula)
Let `M` be the transition matrix (column-stochastic for outgoing links).

Iterative update:
- Standard: `PR_{k+1} = d * M * PR_k + (1-d) * v`
- `d` (damping) often ~0.85
- `v` is the personalization vector (uniform for standard PR, or focused on a set of nodes for PPR).

Key points:
- Large systems → use **iterative** methods (power iteration), not direct solvers.
- Handle dangling nodes (no out links) carefully (redistribute mass).

## BFS / Shortest paths
- Unweighted shortest path: BFS layers (distance +1)
- Weighted shortest path: Dijkstra (but distributed variants approximate or use iterated relaxations)

## Triangle counting (idea)
- Count triangles by checking neighbor pairs.
- In distributed settings, use ordering constraints (e.g., `v < u < w`) so each triangle counted once.

## Components
- Connected components (undirected): maximal set where every pair is connected by a path.
- Strongly connected components (directed): mutual reachability (path both ways).

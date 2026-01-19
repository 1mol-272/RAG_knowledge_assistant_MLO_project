# Implementing Graph Algorithms with DataFrames (Map/Reduce view)

This section focuses on the *DataFrame style* (join + groupBy) implementations.

## PageRank as DataFrame operations (sketch)
1. Keep `edges(src, dst, weight)` where weight distributes rank (`1/outDegree` or custom).
2. At each iteration:
   - join edges with ranks on `src`
   - contribution = `d * rank(src) * weight`
   - aggregate by `dst` with `sum(contribution)`
   - new_rank(dst) = aggregated + (1-d) * personalization(dst)

## Triangle counting (sketch)
- Generate neighbor pairs per node (potential triangles) and then join with real edges to validate.
- Use ordering constraints to avoid duplicates.

## BFS style (iterative relaxations)
- Maintain `distances(id, d)` and an `active` set.
- Expand from active nodes by joining with edges and updating tentative distances.
- Stop when there is no update.

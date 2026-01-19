# Glossary (Key terms)

- **Transformation**: Lazy operation that defines a new RDD/DF; executed only when an action is called.
- **Action**: Triggers computation (collect, count, show, write, ...).
- **Shuffle**: Data movement across partitions, typically caused by wide transformations (join, groupBy, repartition).
- **Partition**: A chunk of distributed data processed in parallel.
- **Broadcast join**: Send small table to all executors to avoid large shuffle.
- **Catalyst**: Spark SQL optimizer that rewrites logical plans.
- **Graph**: (V, E) with vertices and edges; often represented by two tables.
- **GraphFrame**: Graph abstraction over Spark DataFrames (vertices DF + edges DF).
- **PageRank**: Importance score based on random walk with teleport.
- **PPR**: Personalized PageRank biased to a seed node with restart.
- **BFS**: Breadth-first search; finds paths under constraints.
- **Connected components**: Groups of vertices connected in an undirected sense.
- **Motif finding**: Pattern matching of subgraphs using a declarative syntax.

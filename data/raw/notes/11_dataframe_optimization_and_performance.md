# DataFrames: Optimization & Performance (Exam-ready)

## Execution model
- Transformations build a **logical plan**; actions trigger execution.
- Spark SQL uses **Catalyst optimizer** to rewrite the plan; physical plan chooses join strategy, partitioning, etc.

## Partitions & shuffles
- Wide transformations (join, groupBy, distinct, repartition) often trigger **shuffle**.
- Use `explain()` to check if there is `Exchange` (shuffle) in the physical plan.

## Join strategies (common questions)
- Broadcast hash join: one side small -> `broadcast(df_small)`.
- Sort-merge join: large-large, requires sorting/shuffle.
- Tips:
  - Filter early, select needed columns.
  - Avoid skew (salting, AQE if available).

## Cache/Persist
- `df.cache()` stores computed partitions in memory (lazy until action).
- Use when the same expensive subplan is reused.

## UDF vs built-in functions
- Prefer built-in SQL functions: optimized + codegen.
- UDF can be slower; also limits optimization.

## Window functions
- Pattern: ranking, moving average, top-k per group.
- Typical: `Window.partitionBy(...).orderBy(...)`.

## Debugging performance
- `df.explain(True)`
- Spark UI: stages, tasks, shuffle read/write, skew.

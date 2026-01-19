# Spark Core & RDD Essentials

## Spark architecture (mental model)
- **Driver**: runs your main program, builds the DAG, schedules jobs.
- **Executors**: run tasks on worker nodes and store cached data.
- **SparkSession / SparkContext**: entry point to Spark. The `master` configuration chooses local vs cluster.

## RDD vs DataFrame (why both exist)
- **RDD**: distributed collection without schema (low-level, functional transformations + actions).
- **DataFrame**: distributed table with schema, optimized by **Catalyst** (query optimizer).

## RDD operations
### Transformations (lazy)
- `map`, `flatMap`, `filter`, `union`, `distinct`...
- Pair-RDD ops: `reduceByKey`, `aggregateByKey`, `join`, `groupByKey`...

### Actions (trigger computation)
- `collect` (only if small), `take`, `count`, `reduce`, `saveAsTextFile`...

## Execution: DAG, Jobs, Stages
- Transformations build a **lineage graph** (DAG).
- An **action** triggers a job; Spark splits it into stages separated by shuffles.

## Common exam traps
- `collect()` on large data can crash the driver.
- `groupByKey()` often worse than `reduceByKey()` due to shuffle volume.
- Not understanding laziness → “why didn’t my code run?”

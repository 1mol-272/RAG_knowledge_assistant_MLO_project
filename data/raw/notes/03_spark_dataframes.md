# Spark DataFrames Cheat Notes

## Create a SparkSession
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("app").getOrCreate()
```

## Read data
```python
df = spark.read.option("header", True).csv("path/to/file.csv")
```

## Inspect & debug
- `df.printSchema()`
- `df.show(n)`
- `df.columns`, `df.count()`

## Core transformations
### Projection / selection
```python
from pyspark.sql.functions import col
(df.select(col("id"), col("name"))
   .filter(col("age") > 30)
   .orderBy(col("age").desc()))
```

### Joins
```python
res = a.join(b, on="id", how="inner")
```
Join types: `inner`, `left`, `right`, `full`, `left_semi`, `left_anti`.

### GroupBy / aggregation
```python
from pyspark.sql.functions import count, avg
(df.groupBy("userId")
   .agg(count("movieId").alias("n"), avg("rating").alias("mean")))
```

### Useful SQL functions (typical)
- `lower`, `split`, `explode`, `max`, `collect_list`, `when`...

## User-defined functions (UDF)
Prefer built-in SQL functions when possible.
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

@udf(IntegerType())
def f(x):
    return 0 if x is None else x

out = df.withColumn("x2", f(col("x")))
```

## Practice checklist
- Can you: read CSV, clean columns, explode arrays, join, groupBy, build features?

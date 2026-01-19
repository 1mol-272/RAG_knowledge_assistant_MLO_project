# Closed-book Exam Strategy (闭卷应对)

## 1) How to answer short questions (简答题)
Use this template:
- Definition (1 sentence)
- Why it matters / when it happens (1–2 sentences)
- Example (mini Spark/graph example)
- Pitfalls (1–2 bullet points)

Examples of common short-answer prompts:
- What is a shuffle? Why is it expensive? How to reduce it?
- DataFrame vs RDD: differences and use cases
- Broadcast join: when to use, limitations
- What does PageRank measure? What are its parameters?

## 2) Coding questions (编程题)
### Recommended closed-book structure
1) Create SparkSession
2) Load data + schema
3) Transformations (select/filter/withColumn)
4) Join / aggregation
5) Output / show

### GraphFrames coding structure
1) Build vertices/edges DataFrames
2) GraphFrame(v, e)
3) Run algorithm (bfs/pagerank/cc)
4) Interpret + show

## 3) MCQ (选择题)
High-frequency MCQ areas:
- API names (select vs withColumn)
- join types semantics
- caching/persist
- GraphFrames required column names

## 4) “If stuck” fallback during exam
- Write the skeleton first (imports + session + dataframe pipeline)
- Then fill details (columns, conditions)
- For graphs: always define vertices(id), edges(src,dst)


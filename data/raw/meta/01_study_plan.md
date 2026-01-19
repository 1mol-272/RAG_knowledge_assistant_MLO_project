# Study Plan (Closed-book) - 10 days / 14 days

Choose the plan based on your remaining time. Goal: be able to **write** code from memory and explain key concepts.

## 10-day plan (2-3h/day)
Day 1: Spark execution model + partition/shuffle mental model
- Make a 1-page memory sheet: Job/Stage/Task, narrow vs wide, shuffle triggers

Day 2: DataFrame core API
- select/withColumn/filter, explode, when/cast
- 5 mini-exercises (transform columns, parse strings, handle nulls)

Day 3: Aggregations
- groupBy + agg patterns, distinct, pivot (if relevant)
- Build 10 query snippets you can rewrite from memory

Day 4: Joins
- inner/left, semi/anti, broadcast join idea
- 5 join exercises (dedup, skew awareness, matching semantics)

Day 5: Window functions (if in course)
- row_number, dense_rank, lag/lead, partitionBy/orderBy

Day 6: Graph modelling with DataFrames
- Build vertices/edges from logs; degree computations
- Do one motif/triangle via joins

Day 7: GraphFrames basics
- Construct GraphFrame; caching
- Understand algorithm outputs (columns) and parameters

Day 8: Graph algorithms
- PageRank, BFS, ConnectedComponents, ShortestPaths, TriangleCount
- For each: what it returns and a minimal code template

Day 9: Recommendation & similarity
- Jaccard/co-occurrence; PPR intuition and pseudo-code

Day 10: Mock exam
- 30-min MCQ + 30-min short answers + 60-min coding
- Review mistakes and update memory sheet

## 14-day plan
- Same ordering but add 4 buffer days:
  - extra coding drills, revisiting weak topics, and one additional mock exam.

## Daily method (闭卷最有效)
1) 20 min: rewrite key templates from memory (no notes)
2) 60-90 min: solve 2-3 problems
3) 20 min: check solutions + write "common mistakes" bullets

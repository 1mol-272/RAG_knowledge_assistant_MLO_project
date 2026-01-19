# Revision Strategy (how to practice efficiently)

## 1) Fast recall loop (15–20 min)
- Re-write from memory:
  - PageRank equation
  - join + groupBy patterns
  - GraphFrame schema requirements (id/src/dst)

## 2) Hands-on drills (60–90 min)
- DataFrames: load CSV → clean → join → aggregate → export.
- GraphFrames: build tiny graph → BFS → connected components → PageRank.

## 3) Error-focused review
Common issues to force yourself to debug:
- type mismatches (string vs int)
- missing columns (`id`, `src`, `dst`)
- duplicates / multiple edges
- exploding arrays leads to row explosion

## 4) If the exam has coding
- Keep a personal “starter template” (SparkSession, imports, helpers)
- Time yourself on 2–3 end-to-end problems.

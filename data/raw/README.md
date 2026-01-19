# Exam RAG Dataset (Spark DataFrames + Graphs + GraphFrames)

This dataset reorganizes the provided course materials into **RAG-friendly files**: concise notes, runnable code templates, and a question bank (MCQ / short answers / coding tasks / math).

It is designed for a **closed-book written exam**, where questions may include:
- Multiple choice (MCQ)
- Short-answer / conceptual questions
- Coding tasks (PySpark DataFrames, graph-as-dataframe, GraphFrames)

## Folder structure

- `data/raw/sources/`
  Original materials (PDF + notebooks) you uploaded.

- `data/raw/notes/`
  Core notes and summaries (concepts, APIs, typical pitfalls, exam patterns).
- `data/raw/meta/`
  High-level meta documents for abstract queries (syllabus outline, study plan, closed-book strategy, glossary, modes/output contract, fallback policy).


- `data/raw/notes/extras/`
  Additional sheets: performance/optimization, algorithm cheat-sheet, common mistakes.

- `data/raw/code/`
  Minimal, runnable code templates that cover common exam-style tasks.

- `data/raw/qbank/`
  Question bank in JSON: MCQ, short answers, coding tasks, and math exercises.

## Suggested usage (RAG)

1. Ingest all files under `data/raw/` into your RAG pipeline.
2. Chunk primarily the Markdown notes and optionally code and JSON.
3. For answering exam questions, retrieve relevant notes + code templates + similar questions.
4. Return answers with citations (file + section/chunk id).

## Quick sanity check

- Notes: `data/raw/notes/*.md` and `data/raw/notes/extras/*.md`
- Code: `data/raw/code/*.py`
- QBank: `data/raw/qbank/*.json`


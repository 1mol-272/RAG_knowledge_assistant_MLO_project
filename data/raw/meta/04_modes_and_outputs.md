# Modes & Structured Output Contract

We support 4 modes in responses:

## 1) explain
- Explain concept and show minimal code skeleton if relevant.

## 2) quiz
- Generate questions (MCQ / short answer) with answers and explanations.

## 3) practice
- Provide a problem statement + hints, but do NOT reveal full solution immediately.

## 4) grade
- User provides an answer/code. Return:
  - score rubric
  - mistakes
  - corrected version
  - key points to review

## Output must always include
- `mode`
- `answer`
- `key_points` with `importance` (1–5)
- `sources` (citations)
- `retrieval` stats (top score, threshold, hit/miss)
- if retrieval miss: `likely_topics` suggestions

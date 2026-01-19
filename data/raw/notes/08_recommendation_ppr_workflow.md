# Recommendation with Personalized PageRank (PPR) — Workflow

## Graph construction idea (music example)
You build a heterogeneous graph:
- user → song edges (weights sum to 1 per user)
- user → artist edges (weights sum to 1 per user)
- artist → song edges (weights sum to 1 per artist)
- song ↔ song edges (similarity links; graph of songs is undirected)

Then you run **Personalized PageRank** from a given user node to rank songs.

## PPR iteration (concept)
Let `x` be the current importance vector.
- Initialize: `x[user] = (1-d)`, others 0.
- Update rule (high-level): propagate mass along outgoing edges with damping `d`,
  and inject teleport mass `(1-d)` back to the personalization source.

## Output
- Sort songs by score and filter out songs already listened by the user.
- Return top-N recommendations.

## Exam angle
- Be able to explain: (1) why weights must be normalized, (2) how personalization changes PR.

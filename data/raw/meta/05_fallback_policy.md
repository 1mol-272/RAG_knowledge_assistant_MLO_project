# Fallback behavior when retrieval is weak

If the top retrieval similarity is below a threshold, treat the question as "not found in corpus".

Then respond with:
1) A transparent note: "I cannot find strong evidence in the provided materials."
2) A *best guess* of where the question fits in the outline (topic suggestions).
3) Ask 1 clarification question OR suggest what material to add.

Topic suggestion logic:
- Match keywords in the question to `topic_map.json` keyword lists
- Return top 3-5 candidate topics with short reasoning

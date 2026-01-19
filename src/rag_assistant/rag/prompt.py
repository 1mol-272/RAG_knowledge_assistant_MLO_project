import json
from rag_assistant.schemas import QueryResponse

def build_prompt(question: str, contexts: list[dict]) -> str:
    ctx = []
    for c in contexts:
        ctx.append(f"[{c['id']}] (doc={c['doc_id']}, page={c.get('page')})\n{c['text']}")
    context_block = "\n\n---\n\n".join(ctx)

    schema_hint = {
        "answer": "string",
        "recommendations": [
            {"key": "string", "value": "string", "reason": "string", "sources": ["chunk_id"]}
        ],
        "sources": [
            {"id": "chunk_id", "doc_id": "string", "page": 1, "snippet": "string"}
        ],
    }

    return f"""
You are a helpful knowledge assistant. Use ONLY the provided context to answer.
If info is missing, say so.

Return STRICT JSON following this shape:
{json.dumps(schema_hint, ensure_ascii=False, indent=2)}

Question:
{question}

Context:
{context_block}
""".strip()

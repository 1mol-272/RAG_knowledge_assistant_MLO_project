import json
from typing import Any
from rag_assistant.config import settings

def call_llm(prompt: str) -> str:
    if settings.llm_provider == "mock":
        # 简化：直接返回一个可解析 JSON（后面换真实 LLM）
        return json.dumps({
            "answer": "MOCK: I used retrieved context to answer. Replace mock with a real LLM later.",
            "recommendations": [],
            "sources": []
        }, ensure_ascii=False)

    if settings.llm_provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=settings.openai_api_key)
        resp = client.chat.completions.create(
            model=settings.openai_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return resp.choices[0].message.content

    raise ValueError(f"Unknown llm_provider: {settings.llm_provider}")

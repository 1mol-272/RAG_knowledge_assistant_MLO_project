import json
from rag_assistant.rag.retriever import Retriever
from rag_assistant.rag.prompt import build_prompt
from rag_assistant.rag.llm import call_llm
from rag_assistant.schemas import QueryResponse, Source, Recommendation

class RagPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def run(self, question: str) -> QueryResponse:
        contexts = self.retriever.retrieve(question)

        prompt = build_prompt(question, contexts)
        raw = call_llm(prompt)

        # 尝试解析 JSON；解析失败就做降级
        try:
            obj = json.loads(raw)
        except Exception:
            # fallback：直接把检索内容返回，避免服务挂
            sources = [
                Source(
                    id=c["id"], doc_id=c["doc_id"], page=c.get("page"),
                    snippet=c["text"][:300]
                ) for c in contexts
            ]
            return QueryResponse(answer=raw, recommendations=[], sources=sources)

        # 如果模型没填 sources，我们用检索结果补齐
        sources = []
        for c in contexts:
            sources.append(Source(
                id=c["id"], doc_id=c["doc_id"], page=c.get("page"),
                snippet=c["text"][:300]
            ))

        recs = []
        for r in obj.get("recommendations", []):
            recs.append(Recommendation(**r))

        answer = obj.get("answer", "")
        return QueryResponse(answer=answer, recommendations=recs, sources=sources)

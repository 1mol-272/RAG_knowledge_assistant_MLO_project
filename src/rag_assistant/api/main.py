from fastapi import FastAPI
from rag_assistant.schemas import QueryRequest, QueryResponse
from rag_assistant.rag.pipeline import RagPipeline

app = FastAPI(title="RAG Assistant")
pipeline = RagPipeline()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    return pipeline.run(req.question)

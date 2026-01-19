from pydantic import BaseModel, Field
from typing import List, Optional

class Source(BaseModel):
    id: str
    doc_id: str
    page: Optional[int] = None
    snippet: str

class Recommendation(BaseModel):
    key: str
    value: str
    reason: str
    sources: List[str] = Field(default_factory=list)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    recommendations: List[Recommendation]
    sources: List[Source]

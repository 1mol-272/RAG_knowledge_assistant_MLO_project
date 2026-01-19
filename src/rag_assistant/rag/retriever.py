import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from rag_assistant.config import settings
from rag_assistant.indexing.faiss_store import load_meta, search

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)
        self.index = faiss.read_index(settings.index_path)
        self.meta = load_meta(settings.meta_path)

    def retrieve(self, question: str, top_k: int | None = None):
        k = top_k or settings.top_k
        qvec = self.model.encode([question], normalize_embeddings=False)
        qvec = np.array(qvec, dtype="float32")
        scores, idxs = search(self.index, qvec, k)

        results = []
        for score, i in zip(scores, idxs):
            if i < 0:
                continue
            m = self.meta[int(i)]
            results.append({"score": float(score), **m})
        return results

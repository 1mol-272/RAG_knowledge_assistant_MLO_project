import json
from pathlib import Path
from typing import List, Dict, Any
import numpy as np
from sentence_transformers import SentenceTransformer

from rag_assistant.indexing.faiss_store import build_flat_ip, save_meta
from rag_assistant.config import settings

def read_chunks(path: str) -> List[Dict[str, Any]]:
    chunks = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    return chunks

def build_index() -> None:
    chunks = read_chunks(settings.chunks_path)
    texts = [c["text"] for c in chunks]
    if not texts:
        raise RuntimeError(f"No chunks found at {settings.chunks_path}. Run ingest first.")

    model = SentenceTransformer(settings.embedding_model)
    vecs = model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=False)
    vecs = np.array(vecs, dtype="float32")

    index = build_flat_ip(vecs)

    Path(settings.faiss_dir).mkdir(parents=True, exist_ok=True)
    import faiss
    faiss.write_index(index, settings.index_path)
    save_meta(chunks, settings.meta_path)

    cfg = {
        "embedding_model": settings.embedding_model,
        "chunk_size": settings.chunk_size,
        "chunk_overlap": settings.chunk_overlap,
        "dim": int(vecs.shape[1]),
    }
    with open(settings.index_config_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    build_index()

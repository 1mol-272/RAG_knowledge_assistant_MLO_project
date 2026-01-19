from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
import json
from pathlib import Path
import numpy as np
import faiss

@dataclass
class FaissArtifacts:
    index: faiss.Index
    meta: List[Dict[str, Any]]

def save_meta(meta: List[Dict[str, Any]], meta_path: str) -> None:
    Path(meta_path).parent.mkdir(parents=True, exist_ok=True)
    with open(meta_path, "w", encoding="utf-8") as f:
        for m in meta:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")

def load_meta(meta_path: str) -> List[Dict[str, Any]]:
    meta = []
    with open(meta_path, "r", encoding="utf-8") as f:
        for line in f:
            meta.append(json.loads(line))
    return meta

def build_flat_ip(vectors: np.ndarray) -> faiss.Index:
    # cosine similarity = normalize + inner product
    faiss.normalize_L2(vectors)
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)
    return index

def search(index: faiss.Index, query_vec: np.ndarray, top_k: int) -> Tuple[np.ndarray, np.ndarray]:
    q = query_vec.astype("float32")
    faiss.normalize_L2(q)
    scores, idx = index.search(q, top_k)
    return scores[0], idx[0]

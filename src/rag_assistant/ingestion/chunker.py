from typing import Dict, Any, List
import re

def clean_text(s: str) -> str:
    s = re.sub(r"\s+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    text = clean_text(text)
    if not text:
        return []
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunks.append(text[start:end])
        if end == n:
            break
        start = max(0, end - overlap)
    return chunks

def make_chunks(doc_page: Dict[str, Any], chunk_size: int, overlap: int) -> List[Dict[str, Any]]:
    doc_id = doc_page["doc_id"]
    page = doc_page.get("page")
    pieces = chunk_text(doc_page["text"], chunk_size, overlap)
    out = []
    for idx, piece in enumerate(pieces):
        chunk_id = f"{doc_id}#p{page or 0}#c{idx}"
        out.append({
            "id": chunk_id,
            "doc_id": doc_id,
            "page": page,
            "text": piece,
        })
    return out

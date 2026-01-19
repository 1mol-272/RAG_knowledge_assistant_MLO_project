from pathlib import Path
from typing import Iterable, Dict, Any, List
from pypdf import PdfReader

def load_txt(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return [{"doc_id": path.name, "page": None, "text": text}]

def load_md(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return [{"doc_id": path.name, "page": None, "text": text}]

def load_pdf(path: Path) -> List[Dict[str, Any]]:
    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages):
        txt = page.extract_text() or ""
        pages.append({"doc_id": path.name, "page": i + 1, "text": txt})
    return pages

def load_documents(raw_dir: str) -> Iterable[Dict[str, Any]]:
    raw = Path(raw_dir)
    for p in raw.rglob("*"):
        if not p.is_file():
            continue
        suffix = p.suffix.lower()
        if suffix == ".pdf":
            yield from load_pdf(p)
        elif suffix == ".md":
            yield from load_md(p)
        elif suffix in [".txt", ".text"]:
            yield from load_txt(p)
        elif suffix == ".py":
            yield from load_txt(p)
        elif suffix == ".json":
            yield from load_txt(p)


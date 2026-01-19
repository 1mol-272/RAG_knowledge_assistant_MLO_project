import json
from pathlib import Path
from rag_assistant.config import settings
from rag_assistant.ingestion.loader import load_documents
from rag_assistant.ingestion.chunker import make_chunks

def main():
    Path(settings.chunks_path).parent.mkdir(parents=True, exist_ok=True)
    out = open(settings.chunks_path, "w", encoding="utf-8")

    n = 0
    for doc_page in load_documents(settings.raw_dir):
        chunks = make_chunks(doc_page, settings.chunk_size, settings.chunk_overlap)
        for c in chunks:
            out.write(json.dumps(c, ensure_ascii=False) + "\n")
            n += 1

    out.close()
    print(f"Wrote {n} chunks -> {settings.chunks_path}")

if __name__ == "__main__":
    main()

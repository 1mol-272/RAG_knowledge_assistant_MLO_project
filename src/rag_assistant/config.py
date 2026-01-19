from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # data
    raw_dir: str = "data/raw"
    chunks_path: str = "data/processed/chunks.jsonl"

    # artifacts
    faiss_dir: str = "artifacts/faiss"
    index_path: str = "artifacts/faiss/index.faiss"
    meta_path: str = "artifacts/faiss/meta.jsonl"
    index_config_path: str = "artifacts/faiss/config.json"

    # rag
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size: int = 900         
    chunk_overlap: int = 150
    top_k: int = 5

    # llm
    llm_provider: str = "mock"     # mock | openai
    openai_model: str = "gpt-4o-mini"
    openai_api_key: str | None = None

settings = Settings()

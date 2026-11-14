"""Configuration loader for Day 7 Agentic RAG connecting to Day 6 pgvector store."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
DAY6_ROOT = Path(os.getenv("DAY6_ROOT", r"D:\AI thuc chien\K5-L3A-DAY06-2A202603573-DataIngestion"))

DEFAULT_EMBEDDING_MODEL = "gemini-embedding-001"
DEFAULT_EMBEDDING_DIMENSIONS = 768
DEFAULT_AGENT_MODEL = "gemini-2.5-flash"
DEFAULT_PG_TABLE = "day6_chunks_b"


@dataclass(frozen=True)
class Settings:
    database_url: str
    gemini_api_key: str
    embedding_model: str
    embedding_dimensions: int
    agent_model: str
    pg_table: str


def load_settings(*, require_api_key: bool = True, require_db: bool = True) -> Settings:
    """Load settings from `.env` in repo root without exposing secrets."""
    load_dotenv(REPO_ROOT / ".env", override=False)

    database_url = os.getenv("DATABASE_URL", "").strip()
    gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip()
    embedding_model = (os.getenv("EMBEDDING_MODEL", "") or DEFAULT_EMBEDDING_MODEL).strip()
    if embedding_model.startswith("models/"):
        embedding_model = embedding_model.split("/", 1)[1]
    agent_model = (os.getenv("AGENT_MODEL", "") or DEFAULT_AGENT_MODEL).strip()
    pg_table = (os.getenv("DAY6_PG_TABLE", "") or DEFAULT_PG_TABLE).strip()

    if require_db and not database_url:
        raise RuntimeError("DATABASE_URL is missing in .env.")
    if require_api_key and not gemini_api_key:
        raise RuntimeError("GEMINI_API_KEY is missing in .env. Mock fallback is disabled.")

    return Settings(
        database_url=database_url,
        gemini_api_key=gemini_api_key,
        embedding_model=embedding_model,
        embedding_dimensions=DEFAULT_EMBEDDING_DIMENSIONS,
        agent_model=agent_model,
        pg_table=pg_table,
    )

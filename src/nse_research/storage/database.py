from pathlib import Path
from sqlalchemy import create_engine
from nse_research.core.config import get_settings


def get_engine():
    url = get_settings().database_url
    if url.startswith("sqlite:///"):
        Path(url.removeprefix("sqlite:///")).parent.mkdir(parents=True, exist_ok=True)
    return create_engine(url, future=True)

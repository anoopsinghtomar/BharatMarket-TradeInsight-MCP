from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict


class DataProvenance(BaseModel):
    server_name: str
    tool_name: str
    retrieved_at: datetime
    market_date: str | None = None
    arguments: dict[str, Any] = {}
    model_config = ConfigDict(extra="forbid")


class ValidatedPayload(BaseModel):
    data: Any
    provenance: DataProvenance
    validation_status: str
    warnings: list[str] = []

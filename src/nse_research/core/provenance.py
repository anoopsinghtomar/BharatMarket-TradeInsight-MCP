from datetime import datetime
from typing import Any
from nse_research.core.models import DataProvenance


def build_provenance(
    server_name: str, tool_name: str, arguments: dict[str, Any], market_date: str | None = None
) -> DataProvenance:
    return DataProvenance(
        server_name=server_name,
        tool_name=tool_name,
        retrieved_at=datetime.now().astimezone(),
        market_date=market_date,
        arguments=arguments,
    )

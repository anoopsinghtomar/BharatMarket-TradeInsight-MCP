import os
import pytest
from nse_research.core.config import get_settings
from nse_research.data.mcp.client import NSEMCPClient


@pytest.mark.integration
@pytest.mark.asyncio
async def test_cm_market_tool_discovery():
    if os.getenv("RUN_NSE_INTEGRATION") != "1":
        pytest.skip("Set RUN_NSE_INTEGRATION=1 to call the live NSE MCP endpoint")
    settings = get_settings()
    tools = await NSEMCPClient("NSE CM Market MCP", settings.nse_cm_market_mcp_url).discover_tools()
    assert isinstance(tools, list)

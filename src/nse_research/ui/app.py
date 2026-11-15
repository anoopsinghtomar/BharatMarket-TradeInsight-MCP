import streamlit as st

st.set_page_config(page_title="NSE AI Research", page_icon="📈", layout="wide")
st.title("📈 NSE AI Research")
st.caption("Evidence-led Indian equity research using official NSE MCP services")

st.info(
    "Starter dashboard: live market panels remain disabled until the actual NSE MCP "
    "tool catalogue and response schemas have been discovered and reviewed."
)

left, middle, right = st.columns(3)
left.metric("Nifty 50 Pre-Market", "Not configured")
middle.metric("Long-Term Research", "Not configured")
right.metric("AI Research Assistant", "Not configured")

st.subheader("Getting started")
st.code("python scripts/discover_mcp_tools.py\npython scripts/test_nse_connection.py")
st.warning(
    "No market prices are shown in this starter UI. Configure verified NSE MCP workflows "
    "before displaying market figures."
)

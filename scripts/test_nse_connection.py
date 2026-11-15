import asyncio
from nse_research.data.mcp.connection import configured_clients


async def main():
    failures = 0
    for key, client in configured_clients().items():
        try:
            tools = await client.discover_tools()
            print(f"OK: {client.server_name} — {len(tools)} tools discovered")
        except Exception as exc:
            failures += 1
            print(f"FAILED: {key}: {exc}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())

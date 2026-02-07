from __future__ import annotations

import argparse
from services.chart_service import mcp


def main() -> None:
    parser = argparse.ArgumentParser(description="Matplotlib MCP server")
    parser.add_argument(
        "--transport",
        choices=["streamable-http", "stdio"],
        default="streamable-http",
        help="Transport para executar o servidor",
    )

    args = parser.parse_args()

    if args.transport == "streamable-http":
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()

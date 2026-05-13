"""Smoke test: verify DeepSeek API key and connection work."""

import asyncio
from mcp_devtools.llm.deepseek import chat, get_client


async def main():
    print("Testing deepseek-v4-flash...")
    out = await chat("Say 'hello world' in one short sentence.")
    print(f"  Response: {out}\n")

    print("Testing deepseek-v4-pro...")
    out = await chat(
        "What's 17 * 23? Answer with just the number.",
        model="deepseek-v4-pro",
    )
    print(f"  Response: {out}")


if __name__ == "__main__":
    asyncio.run(main())

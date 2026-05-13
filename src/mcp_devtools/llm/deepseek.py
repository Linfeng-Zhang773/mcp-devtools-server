"""Thin wrapper around DeepSeek's API(OpenAI compatible)."""

from openai import AsyncOpenAI
from mcp_devtools.config import settings


def get_client() -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_api_url,
    )


async def chat(prompt: str, model: str | None = None, system: str | None = None) -> str:
    """
    chat helper function for smoke tests and simple calls of deepseek's API.
    """
    client = get_client()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = await client.chat.completions.create(
        model=model or settings.model_flash,
        messages=messages,
    )

    return resp.choices[0].message.content or ""

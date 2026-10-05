"""Stable Octic Agent facade."""
from __future__ import annotations
from typing import Any, Sequence
class OcticAgent:
    def __init__(self, instructions: str, *, name: str = "OcticAgent", model: str | None = None, tools: Sequence[Any] | None = None) -> None:
        from praisonaiagents import Agent
        kwargs: dict[str, Any] = {"name": name, "instructions": instructions}
        if model: kwargs["llm"] = model
        if tools is not None: kwargs["tools"] = list(tools)
        self._agent = Agent(**kwargs)
    def start(self, prompt: str) -> Any:
        return self._agent.start(prompt)
    async def astart(self, prompt: str) -> Any:
        method = getattr(self._agent, "astart", None)
        if method is not None: return await method(prompt)
        import asyncio
        return await asyncio.to_thread(self.start, prompt)

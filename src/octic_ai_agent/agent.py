"""Standalone Octic AI Agent runtime powered by LiteLLM.

The core OcticAgent does not delegate execution to another agent framework.
It supports OpenAI-compatible chat-completion providers and Python callable tools.
"""
from __future__ import annotations

import asyncio
import inspect
import json
import os
import re
import threading
from collections.abc import Mapping, Sequence
from typing import Any, Callable, get_args, get_origin
import types


_DEFAULT_MODEL = "gpt-4o-mini"
_MAX_TOOL_RESULT_CHARS = 50_000


def _get(value: Any, key: str, default: Any = None) -> Any:
    if isinstance(value, Mapping):
        return value.get(key, default)
    return getattr(value, key, default)


def _annotation_to_schema(annotation: Any) -> dict[str, Any]:
    """Convert common Python annotations to JSON Schema types."""
    if annotation is inspect.Signature.empty or annotation is Any:
        return {"type": "string"}

    origin = get_origin(annotation)
    args = get_args(annotation)
    if origin in (types.UnionType, getattr(__import__("typing"), "Union")):
        non_null = [item for item in args if item is not type(None)]
        if len(non_null) == 1:
            return _annotation_to_schema(non_null[0])
        return {"anyOf": [_annotation_to_schema(item) for item in non_null]}

    if annotation is str:
        return {"type": "string"}
    if annotation is bool:
        return {"type": "boolean"}
    if annotation is int:
        return {"type": "integer"}
    if annotation is float:
        return {"type": "number"}
    if annotation is dict or origin is dict:
        return {"type": "object"}
    if annotation is list or annotation is tuple or origin in (list, tuple, Sequence):
        item_type = args[0] if args else str
        return {"type": "array", "items": _annotation_to_schema(item_type)}
    return {"type": "string"}


def _make_tool_schema(tool: Callable[..., Any]) -> tuple[str, dict[str, Any]]:
    if not callable(tool):
        raise TypeError("Each tool must be a callable Python function.")

    raw_name = getattr(tool, "__name__", tool.__class__.__name__)
    name = re.sub(r"[^a-zA-Z0-9_-]", "_", raw_name)[:64] or "tool"
    signature = inspect.signature(tool)
    properties: dict[str, Any] = {}
    required: list[str] = []

    for parameter in signature.parameters.values():
        if parameter.kind in (
            inspect.Parameter.VAR_POSITIONAL,
            inspect.Parameter.VAR_KEYWORD,
        ):
            continue
        properties[parameter.name] = _annotation_to_schema(parameter.annotation)
        if parameter.default is inspect.Signature.empty:
            required.append(parameter.name)

    description = inspect.getdoc(tool) or f"Call the {name} tool."
    schema = {
        "type": "function",
        "function": {
            "name": name,
            "description": description[:1024],
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
                "additionalProperties": False,
            },
        },
    }
    return name, schema


def _safe_json(value: Any) -> str:
    if isinstance(value, str):
        result = value
    else:
        result = json.dumps(value, ensure_ascii=False, default=str)
    if len(result) > _MAX_TOOL_RESULT_CHARS:
        return result[:_MAX_TOOL_RESULT_CHARS] + "\n[Octic truncated this tool result.]"
    return result


def _message_content(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            text = _get(item, "text")
            if text is not None:
                parts.append(str(text))
        return "\n".join(parts)
    return str(content)


def _resolve_awaitable(value: Any) -> Any:
    """Run an async tool even when start() was called from a running event loop."""
    if not inspect.isawaitable(value):
        return value
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(value)

    # start() is a synchronous API. If the caller already owns an event loop,
    # resolve the tool coroutine in a separate thread with its own loop.
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=1) as executor:
        return executor.submit(asyncio.run, value).result()


class OcticAgent:
    """A stateful Octic agent with model responses and optional Python tools.

    Args:
        instructions: System instructions that define the agent's behavior.
        name: Display name used in the system prompt.
        model: LiteLLM model identifier. Defaults to OCTIC_AI_AGENT_MODEL,
            then OPENAI_MODEL, then gpt-4o-mini.
        tools: Python callables the model may request.
        max_iterations: Maximum number of model turns per user prompt.
        temperature: Sampling temperature passed to the model provider.

    Set the provider's API key in its standard environment variable, such as
    OPENAI_API_KEY. For local or OpenAI-compatible providers, set model to the
    appropriate LiteLLM identifier and configure that provider as documented
    by LiteLLM.
    """

    def __init__(
        self,
        instructions: str,
        *,
        name: str = "OcticAgent",
        model: str | None = None,
        tools: Sequence[Callable[..., Any]] | None = None,
        max_iterations: int = 8,
        temperature: float = 0.2,
    ) -> None:
        if not isinstance(instructions, str) or not instructions.strip():
            raise ValueError("instructions must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string.")
        if max_iterations < 1:
            raise ValueError("max_iterations must be at least 1.")
        if not 0 <= temperature <= 2:
            raise ValueError("temperature must be between 0 and 2.")

        self.name = name.strip()
        self.instructions = instructions.strip()
        self.model = (
            model
            or os.environ.get("OCTIC_AI_AGENT_MODEL")
            or os.environ.get("OPENAI_MODEL")
            or _DEFAULT_MODEL
        )
        self.max_iterations = max_iterations
        self.temperature = temperature
        self._tools: dict[str, Callable[..., Any]] = {}
        self._tool_schemas: list[dict[str, Any]] = []

        for tool in tools or ():
            tool_name, schema = _make_tool_schema(tool)
            if tool_name in self._tools:
                raise ValueError(f"Duplicate tool name: {tool_name}")
            self._tools[tool_name] = tool
            self._tool_schemas.append(schema)

        self._history: list[dict[str, Any]] = []
        self._lock = threading.RLock()

    @property
    def history(self) -> list[dict[str, Any]]:
        """Return a copy of the conversation history (excluding system prompt)."""
        with self._lock:
            return [dict(message) for message in self._history]

    def reset(self) -> None:
        """Clear the in-memory conversation history."""
        with self._lock:
            self._history.clear()

    def _run_tool(self, name: str, arguments: Any) -> str:
        tool = self._tools.get(name)
        if tool is None:
            return f"Tool error: '{name}' is not registered."

        try:
            if isinstance(arguments, str):
                parsed = json.loads(arguments or "{}")
            else:
                parsed = arguments
            if not isinstance(parsed, dict):
                raise ValueError("Tool arguments must be a JSON object.")
            result = _resolve_awaitable(tool(**parsed))
            return _safe_json(result)
        except Exception as exc:
            return f"Tool error ({type(exc).__name__}): {exc}"

    def start(self, prompt: str) -> str:
        """Run a prompt to completion and return the final text response."""
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be a non-empty string.")

        with self._lock:
            messages: list[dict[str, Any]] = [
                {
                    "role": "system",
                    "content": f"You are {self.name}.\n\n{self.instructions}",
                },
                *self._history,
                {"role": "user", "content": prompt.strip()},
            ]

            # Import lazily so importing OcticAgent itself is lightweight and
            # gives a clear failure when the model runtime is not installed.
            try:
                from litellm import completion
            except ImportError as exc:
                raise RuntimeError(
                    "LiteLLM is required to run Octic AI Agent. Install with "
                    "'python -m pip install octic-ai-agent'."
                ) from exc

            for turn in range(self.max_iterations):
                kwargs: dict[str, Any] = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": self.temperature,
                }
                if self._tool_schemas:
                    kwargs["tools"] = self._tool_schemas
                    kwargs["tool_choice"] = "auto"

                response = completion(**kwargs)
                choices = _get(response, "choices", [])
                if not choices:
                    raise RuntimeError("The model provider returned no response choices.")
                assistant = _get(choices[0], "message")
                if assistant is None:
                    raise RuntimeError("The model provider returned an invalid response.")

                content = _message_content(_get(assistant, "content"))
                tool_calls = _get(assistant, "tool_calls") or []
                if not tool_calls:
                    if not content.strip():
                        raise RuntimeError("The model returned an empty response.")
                    messages.append({"role": "assistant", "content": content})
                    self._history = [dict(message) for message in messages[1:]]
                    return content

                if turn == self.max_iterations - 1:
                    raise RuntimeError(
                        f"Agent reached max_iterations={self.max_iterations} before "
                        "the model returned a final answer. Increase max_iterations "
                        "if the task legitimately requires more tool rounds."
                    )

                serialized_calls: list[dict[str, Any]] = []
                parsed_calls: list[tuple[str, Any, str]] = []
                for index, call in enumerate(tool_calls):
                    function = _get(call, "function", {})
                    tool_name = str(_get(function, "name", ""))
                    raw_arguments = _get(function, "arguments", "{}")
                    if not isinstance(raw_arguments, str):
                        raw_arguments = json.dumps(raw_arguments, ensure_ascii=False)
                    call_id = str(_get(call, "id", "") or f"call_{turn}_{index}")
                    serialized_calls.append({
                        "id": call_id,
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "arguments": raw_arguments,
                        },
                    })
                    parsed_calls.append((tool_name, raw_arguments, call_id))

                messages.append({
                    "role": "assistant",
                    "content": content or None,
                    "tool_calls": serialized_calls,
                })
                for tool_name, arguments, call_id in parsed_calls:
                    result = self._run_tool(tool_name, arguments)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": call_id,
                        "name": tool_name,
                        "content": result,
                    })

            raise RuntimeError("Agent stopped without producing a final response.")

    async def astart(self, prompt: str) -> str:
        """Async counterpart to start(); provider calls run in a worker thread."""
        return await asyncio.to_thread(self.start, prompt)

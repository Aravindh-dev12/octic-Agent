# Octic AI Agent API Reference

This reference describes the standalone Octic runtime in `src/octic_ai_agent/`. It replaces the former generated reference for a different framework, which pointed to source paths that are not part of the Octic core.

## Python API

The public entry point is `octic_ai_agent.OcticAgent`.

```python
from octic_ai_agent import OcticAgent

agent = OcticAgent(
    instructions="You are a precise research assistant.",
    name="OcticResearch",
    model="gpt-4o-mini",
)
print(agent.start("Explain DNS resolution in five steps."))
```

`model` may be omitted. Octic selects `OCTIC_AI_AGENT_MODEL`, then `OPENAI_MODEL`, then `gpt-4o-mini`. Set the model provider's usual API key in the environment.

### Tools

Python callables are exposed to the model as function tools. If `tools` is omitted, Octic loads its built-in tools; pass `tools=[]` to disable them explicitly.

```python
from octic_ai_agent import OcticAgent

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

agent = OcticAgent(
    instructions="Use available tools when useful.",
    tools=[multiply],
)
print(agent.start("What is 12 times 13?"))
```

Built-in tools include safe arithmetic and current date/time. Install the optional `search` extra for web search. Set `OCTIC_AI_AGENT_WORKSPACE` to enable workspace file listing and reading. File writes and command execution require separate opt-ins; command execution is not a sandbox and must not be enabled on a public service.

### Conversation state

- `start(prompt)` runs a task and returns the final text response.
- `astart(prompt)` provides an asynchronous interface.
- `history` returns a copy of the current in-memory message history.
- `reset()` clears the in-memory history.
- A new agent can be initialized with user/assistant history, limited to 40 messages and 40,000 characters.

## Command line

```bash
octic-ai-agent --help
octic-ai-agent run "Explain DNS resolution"
octic-ai-agent chat
octic-ai-agent doctor
octic-ai-agent serve --host 127.0.0.1 --port 8080
```

Optional historical integration commands are routed through the compatibility extra and are not required by the standalone core.

## HTTP API

Install `octic-ai-agent[api]` (or use the source checkout's editable install) to expose the Flask API.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Process health check |
| GET | `/ready` | Runtime dependency/readiness check |
| GET | `/agents` | List named agent profiles; requires authentication |
| POST | `/chat` | Run an agent request; requires authentication |

The API uses bearer-token authentication by default. Set `OCTIC_AI_AGENT_API_TOKEN` explicitly for deployment; a non-localhost bind requires a token at startup. The API accepts a JSON body such as:

```json
{
  "message": "Explain DNS resolution in five steps.",
  "agent": "research",
  "history": [
    {"role": "user", "content": "What is DNS?"},
    {"role": "assistant", "content": "DNS maps names to network records."}
  ]
}
```

The supported agent profiles are `default`, `research`, `developer`, `data`, and `workflow`. Messages are limited by `OCTIC_AI_AGENT_MAX_MESSAGE_LENGTH` (12,000 characters by default); supplied history is limited to 40 user/assistant messages and 40,000 characters.

## User interfaces and deployment

- `ui/app.py`: local Gradio interface.
- `web/`: Next.js web console that proxies requests to the API using server-side environment variables.
- `docker/Dockerfile`: standalone Octic API image.
- `docker/docker-compose.yml`: Octic API starts by default; previous compatibility services require explicit profiles.

See [README.md](README.md), [ui/README.md](ui/README.md), [web/README.md](web/README.md), and [docker/README.md](docker/README.md) for setup instructions.

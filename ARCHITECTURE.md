# Octic AI Agent Architecture

## Scope

The primary product is the standalone Octic AI Agent runtime. It is packaged from `src/octic_ai_agent/` as `octic-ai-agent` and does not require the previous umbrella agent framework for its default execution path. The repository also retains optional integration packages for compatibility; those keep their low-level dependency/import names until they can be migrated with their call sites and tests.

## Runtime components

```text
Python caller / CLI / Gradio UI / Next.js web console
                     |
                     v
             OcticAgent facade
                     |
          LiteLLM chat completion
                     |
          Optional function-tool loop
          /          |           \
     calculator   date/time   web search*
                                  |
                      workspace tools**
```

`* `web_search` is available when the `search` extra is installed.  
`**` Workspace listing/reading is enabled only when `OCTIC_AI_AGENT_WORKSPACE` points to an existing directory. File writes and command execution require separate environment opt-ins; command execution runs as the current user and is not a sandbox.

## Core runtime

- `agent.py` implements `OcticAgent`, model selection, conversation history, callable tool schemas, tool execution, iteration limits, and sync/async entry points.
- `tools.py` provides built-in calculator/date-time tools, optional public web search, and opt-in workspace operations.
- `cli.py` owns Octic commands: `run`, `chat`, `serve`, and `doctor`. Non-core historical commands may route to the explicit `compat` extra.
- `api_server.py` serves the authenticated HTTP API with health/readiness checks, named agent profiles, input validation, bounded history, and optional CORS origins.

## Interfaces

### Python

`from octic_ai_agent import OcticAgent` is the public import. If `tools` is omitted, the agent loads the safe built-ins available in the current installation; pass `tools=[]` to disable tools.

### HTTP API

`GET /health`, `GET /ready`, `GET /agents`, and `POST /chat` are served by `api_server.py`. Authentication is enabled by default. Set `OCTIC_AI_AGENT_API_TOKEN` for production and do not expose the API publicly without TLS, strong authentication, and network controls.

### Gradio and web console

`ui/app.py` is the local Gradio interface. `web/` is a Next.js console that forwards requests through a server route; its backend URL and bearer token are configured via `OCTIC_AGENT_API_URL` and `OCTIC_AGENT_API_TOKEN`, and the token remains server-side.

### Containers

`docker/Dockerfile` builds the standalone Octic API image. A plain `docker compose up` starts the Octic API service; the historical dashboard, chat, and agents containers are profile-gated to avoid port conflicts.

## Configuration

| Setting | Purpose |
|---|---|
| `OCTIC_AI_AGENT_MODEL` | Default LiteLLM model |
| `OPENAI_API_KEY` | Example provider credential for the default model |
| `OCTIC_AI_AGENT_API_TOKEN` | HTTP bearer token |
| `OCTIC_AI_AGENT_API_HOST` / `OCTIC_AI_AGENT_API_PORT` | API bind address and port |
| `OCTIC_AI_AGENT_API_CORS_ORIGINS` | Comma-separated CORS allowlist |
| `OCTIC_AI_AGENT_WORKSPACE` | Explicit root for local file tools |
| `OCTIC_AI_AGENT_ALLOW_FILE_WRITES=1` | Opt in to workspace writes |
| `OCTIC_AI_AGENT_ALLOW_COMMANDS=1` | Opt in to unsandboxed local command execution |

The root README contains commands for installation, local execution, and API startup.

## Validation

Continuous integration checks installation and compilation on Python 3.10–3.13, runs the core and API tests, builds the Next.js console, validates Docker Compose, and builds the standalone API image. Live model-provider requests require a valid provider credential and are not part of the offline smoke tests.

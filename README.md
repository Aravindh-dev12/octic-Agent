# Octic AI Agent

Octic AI Agent is a Python-based interface for building and running AI agents, with optional API, user-interface, workflow, sandbox, and integration features.

## Get started

Install the package:

    python -m pip install octic-ai-agent

Set your model provider key:

    export OPENAI_API_KEY="your-api-key"

Create and run an agent:

    from octic_ai_agent import OcticAgent

    agent = OcticAgent(
        instructions="You are a helpful research assistant.",
        name="ResearchAssistant",
    )
    result = agent.start("Summarize three important AI developments.")
    print(result)

To select a model, set OCTIC_AI_AGENT_MODEL or pass model when creating the agent.

### Give the agent a tool

Pass ordinary Python callables. Octic builds tool schemas from their signatures and type hints:

```python
from octic_ai_agent import OcticAgent

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

agent = OcticAgent(
    instructions="Use the multiply tool when arithmetic is needed.",
    tools=[multiply],
)
print(agent.start("What is 12 times 13?"))
```

Tools run in your Python process, so register only functions you trust.

## Command-line interface

See the available commands:

    octic-ai-agent --help

## Optional features

Install only the optional features needed by your deployment:

    python -m pip install "octic-ai-agent[api]"
    python -m pip install "octic-ai-agent[ui]"
    python -m pip install "octic-ai-agent[flow]"
    python -m pip install "octic-ai-agent[chat]"
    python -m pip install "octic-ai-agent[browser]"
    python -m pip install "octic-ai-agent[mcp]"
    python -m pip install "octic-ai-agent[sandbox]"
    python -m pip install "octic-ai-agent[deploy]"
    python -m pip install "octic-ai-agent[train]"

Some optional integrations require additional provider credentials or system dependencies.

## Repository layout

- src/octic_ai_agent — Python package and public OcticAgent interface
- src/octic-agent-mcp — MCP integration
- src/octic-agent-sandbox — isolated execution backends
- src/octic-agent-train — training utilities
- src/octic-agent-deploy — deployment utilities
- src/octic-agent-rust — Rust workspace
- ui and web — user-interface projects
- docker — container and Compose configurations
- examples — runnable examples and recipes

## Development

From the repository root, install the package in editable mode with development dependencies:

    python -m pip install -e "src/octic_ai_agent[dev]"

Run the smoke test and compile checks:

    python ci/smoke_test_api.py
    python -m compileall -q src/octic_ai_agent

## Project identity and compatibility

Octic AI Agent is the project name used for the repository, documentation, and user-facing experience. Existing dependency, import, and command identifiers may remain where changing them would break integrations; they should only be migrated as a coordinated compatibility change. Third-party license and authorship notices must be preserved.

## License

See LICENSE for the license terms.

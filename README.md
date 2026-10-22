# Octic AI Agent

Octic AI Agent is a Python-based interface for building and running AI agents, with optional API, user-interface, workflow, sandbox, and integration features.

## Get started

From a source checkout, install Octic and the optional web-search tool:

    git clone https://github.com/Aravindh-dev12/octic-Agent.git
    cd octic-Agent
    python -m pip install -e "src/octic_ai_agent[search]"

Set your model provider key:

    export OPENAI_API_KEY="your-api-key"

Create and run an agent:

    from octic_ai_agent import OcticAgent

    agent = OcticAgent(
        instructions="You are a helpful research assistant.",
        name="ResearchAssistant",
    )
    result = agent.start("Search the web for three important AI developments and summarize them.")
    print(result)

To select a model, set OCTIC_AI_AGENT_MODEL or pass model when creating the agent. Python-created agents automatically load Octic's safe built-in calculator and date/time tools. The `[search]` extra enables web search. Pass `tools=[]` to explicitly disable built-in tools.

### Enable local workspace tools

Configure Octic to list and read files inside a specific local directory:

    export OCTIC_AI_AGENT_WORKSPACE="$PWD"
    octic-ai-agent run "List the files in this workspace and summarize the project."

File writes and command execution are **disabled by default**. For a trusted local workspace only, you can explicitly enable them:

    export OCTIC_AI_AGENT_ALLOW_FILE_WRITES=1
    export OCTIC_AI_AGENT_ALLOW_COMMANDS=1

Command execution is not a sandbox: commands run as your user, with your permissions and environment. Never enable it on an Internet-facing service.

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

    python -m pip install -e "src/octic_ai_agent[api,search]"
    python -m pip install -e "src/octic_ai_agent[ui,search]"
    python -m pip install -e "src/octic_ai_agent[compat,flow]"
    python -m pip install -e "src/octic_ai_agent[compat,chat]"
    python -m pip install -e "src/octic_ai_agent[compat,browser]"
    python -m pip install -e "src/octic_ai_agent[compat,mcp]"
    python -m pip install -e "src/octic_ai_agent[compat,sandbox]"
    python -m pip install -e "src/octic_ai_agent[compat,deploy]"
    python -m pip install -e "src/octic_ai_agent[compat,train]"

Some optional integrations require additional provider credentials or system dependencies. The core Octic runtime and CLI do not require the legacy framework. To keep extended historical CLI commands (such as onboarding or specialized server modes), install the optional bridge:

    python -m pip install "octic-ai-agent[compat]"

Then call those commands through `octic-ai-agent`; when the bridge is not installed, Octic reports how to enable it.

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

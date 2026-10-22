# Octic AI Agent

Octic AI Agent provides a Python interface and command-line entry point for creating and running AI agents, with optional API, UI, workflow, sandbox, and integration features.

## Installation

    python -m pip install -e "src/octic_ai_agent[search]"

Set the credentials required by your model provider, for example:

    export OPENAI_API_KEY="your-api-key"

## Python example

    from octic_ai_agent import OcticAgent

    agent = OcticAgent(
        instructions="You are a helpful research assistant.",
        name="ResearchAssistant",
    )
    result = agent.start("Summarize three important AI developments.")
    print(result)

Use OCTIC_AI_AGENT_MODEL to set a default model, or pass model to OcticAgent directly. Octic's CLI, Gradio UI, and HTTP API also load safe built-in calculator and date/time tools; install the `search` extra to add web search.

### Callable tools

```python
from octic_ai_agent import OcticAgent

def lookup_status(service: str) -> str:
    """Return the status of a service."""
    return f"{service}: healthy"

agent = OcticAgent(
    instructions="Answer clearly and use tools when appropriate.",
    tools=[lookup_status],
)
print(agent.start("Check the status of the billing service."))
```

Tools are ordinary Python functions executed in the same process as the agent. Register only trusted functions.

## Command line

    octic-ai-agent --help

## Optional integrations

Install optional capabilities as needed:

    python -m pip install "octic-ai-agent[api]"
    python -m pip install "octic-ai-agent[ui]"
    python -m pip install "octic-ai-agent[flow]"
    python -m pip install "octic-ai-agent[chat]"
    python -m pip install "octic-ai-agent[browser]"
    python -m pip install "octic-ai-agent[mcp]"
    python -m pip install "octic-ai-agent[sandbox]"
    python -m pip install "octic-ai-agent[deploy]"
    python -m pip install "octic-ai-agent[train]"

Feature availability may depend on provider credentials and platform-specific dependencies.

## Source and support

Source code, architecture notes, and examples are maintained in the Octic AI Agent repository:

https://github.com/Aravindh-dev12/octic-Agent

For development setup, see the repository-level README and CONTRIBUTING guide.

## License

Octic AI Agent is distributed under the terms in the repository LICENSE file.


## Workspace agent tools

Configure `OCTIC_AI_AGENT_WORKSPACE` to expose file listing and read tools for a specific local directory. Octic rejects paths that resolve outside that root and blocks common credential files.

File writes require `OCTIC_AI_AGENT_ALLOW_FILE_WRITES=1`. Command execution requires `OCTIC_AI_AGENT_ALLOW_COMMANDS=1` and uses an argument list rather than a shell. These commands still run with your user permissions and are **not sandboxed**. Do not enable command execution for a public API.

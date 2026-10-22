# Octic AI Agent

Octic AI Agent provides a Python interface and command-line entry point for creating and running AI agents, with optional API, UI, workflow, sandbox, and integration features.

## Installation

    python -m pip install octic-ai-agent

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

Use OCTIC_AI_AGENT_MODEL to set a default model, or pass model to OcticAgent directly.

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

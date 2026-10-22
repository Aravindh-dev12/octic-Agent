# Octic AI Agent UI

The Gradio interface calls the standalone OcticAgent runtime and keeps the conversation history in its UI session.

From the repository root:

```bash
python -m pip install -e "src/octic_ai_agent[ui,search]"
export OPENAI_API_KEY="your-provider-api-key"
python ui/app.py
```

Open the local URL printed by Gradio. Set `OCTIC_AI_AGENT_MODEL` or enter a model identifier in the UI to select a provider. Provider-specific credentials should be set in the environment before launching the app.

Do not expose the development UI to untrusted networks. For a production web console, use the API and the `web/` application with the server-side token configuration described in [web/README.md](../web/README.md).


## Optional local workspace tools

The agent includes calculator and date/time tools. The `search` extra enables public web search.

For local code/document tasks, point Octic at a directory you own:

```bash
export OCTIC_AI_AGENT_WORKSPACE="$PWD"
python ui/app.py
```

The agent can list and read files inside that workspace. File writes and command execution are disabled by default; enable them only for a trusted local workspace:

```bash
export OCTIC_AI_AGENT_ALLOW_FILE_WRITES=1
export OCTIC_AI_AGENT_ALLOW_COMMANDS=1
```

Command execution is **not a sandbox** and runs as your current user with its environment variables. Do not enable it for an Internet-facing UI or API.

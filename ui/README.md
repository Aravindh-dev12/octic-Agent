# Octic AI Agent UI

The Gradio interface calls the standalone OcticAgent runtime and keeps the conversation history in its UI session.

From the repository root:

```bash
python -m pip install -e "src/octic_ai_agent[ui]"
export OPENAI_API_KEY="your-provider-api-key"
python ui/app.py
```

Open the local URL printed by Gradio. Set `OCTIC_AI_AGENT_MODEL` or enter a model identifier in the UI to select a provider. Provider-specific credentials should be set in the environment before launching the app.

Do not expose the development UI to untrusted networks. For a production web console, use the API and the `web/` application with the server-side token configuration described in [web/README.md](../web/README.md).

# Octic AI Agent Examples

This directory contains runnable examples for Octic AI Agent. Each example documents the integration it demonstrates; some advanced examples require optional dependencies, model-provider credentials, or external services.

## Example collections

| Area | Location | What it covers |
|---|---|---|
| Agent-centric API | [agent_centric_api.py](agent_centric_api.py) | Creating and configuring agents |
| API endpoints | [endpoints_example.py](endpoints_example.py) | Calling and exposing agent endpoints |
| Guardrails | [guardrail_example_fixed.py](guardrail_example_fixed.py) | Applying execution and output checks |
| Workflows | [workflows/](workflows/) | Multi-step and multi-agent workflows |
| YAML workflows | [yaml/](yaml/) | Configuration-driven agent workflows |
| Serving and endpoints | [serve/](serve/) | HTTP, MCP, A2A, and related server examples |
| Retrieval-augmented generation | [rag/](rag/) | Document retrieval, search, and RAG patterns |
| Recipes | [recipes/](recipes/) | End-to-end, reusable workflows |
| Skills | [skills/](skills/) | Agent skill examples |
| Tools | [tools/](tools/) | Tool integrations |
| Storage | [storage/](storage/) | Persistence and storage backends |
| Templates | [templates/](templates/) | Reusable agent templates |
| Thinking | [thinking/](thinking/) | Reasoning and execution patterns |
| Tracing | [trace/](trace/) | Observability and tracing |
| Terminal benchmarks | [terminal_bench/](terminal_bench/) | Terminal-task benchmark adapters |
| TypeScript | [typescript/](typescript/) | JavaScript and TypeScript examples |
| Web | [web/](web/) | Web-oriented examples |
| Vector search | [vector/](vector/) | Vector database examples |
| TUI | [tui/](tui/) | Terminal user-interface examples |

## Run examples

From the repository root, install Octic AI Agent:

```bash
python -m pip install -e "src/octic_ai_agent"
export OPENAI_API_KEY="your-api-key"
python examples/agent_centric_api.py
```

To see the available command-line options:

```bash
octic-ai-agent --help
```

Not every example is self-contained. Check the file or its nearby README for extra dependencies and credentials before running it.

## Development checks

Run the repository smoke test from the root:

```bash
python ci/smoke_test_api.py
```

See the [project README](../README.md), [contributing guide](../CONTRIBUTING.md), and [security policy](../SECURITY.md) for repository-wide information.

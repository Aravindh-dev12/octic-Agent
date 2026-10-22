# Contributing to Octic AI Agent

Thank you for helping improve Octic AI Agent. Contributions should be focused, tested, and documented where appropriate.

## Workflow

1. Fork the repository and create a topic branch.
2. Make a focused change with a clear commit message.
3. Add or update tests when behavior changes.
4. Run the relevant checks locally.
5. Open a pull request describing the problem, implementation, and validation.

## Where to make changes

- Python package and public facade: src/octic_ai_agent/
- MCP integration: src/octic-agent-mcp/
- Sandbox integrations: src/octic-agent-sandbox/
- Training utilities: src/octic-agent-train/
- Deployment utilities: src/octic-agent-deploy/
- Rust workspace: src/octic-agent-rust/
- UI and web console: ui/ and web/
- Container setup: docker/
- Examples: examples/

## Python checks

From the repository root:

    python -m pip install -e "src/octic_ai_agent[dev]"
    python ci/smoke_test_api.py
    python -m compileall -q src/octic_ai_agent

Run targeted tests for the component you change. Some integration tests may require provider credentials, network access, or optional system dependencies.

## Rust checks

From src/octic-agent-rust:

    cargo fmt --all -- --check
    cargo test --workspace
    cargo clippy --workspace --all-targets

## Documentation and compatibility

Use Octic AI Agent in user-facing text. Keep examples runnable and links current. Changes to dependency names, import paths, environment variables, or command-line identifiers should include a coordinated migration plan and regression tests. Preserve applicable third-party license and authorship notices.

Please do not commit secrets, local machine paths, generated reports, or unrelated temporary files.

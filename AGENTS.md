# Octic AI Agent — Repository Instructions

These instructions apply to changes across the Octic AI Agent repository.

## Project conventions

- Use Octic AI Agent for user-facing product names, headings, documentation, and examples.
- Keep changes focused and consistent with the existing architecture.
- Prefer small, testable changes over broad refactors.
- Do not add configuration options or public API surface without a clear consumer.
- Avoid committing generated reports, temporary test files, local paths, credentials, or machine-specific configuration.
- Preserve third-party license notices and authorship attribution.
- Existing dependency names, import paths, environment variables, and CLI identifiers can be compatibility-sensitive. Do not mass-rename them without updating their call sites, packaging metadata, tests, and migration guidance together.

## Repository map

- src/octic_ai_agent — Python package and public OcticAgent facade
- src/octic-agent-mcp — MCP integration
- src/octic-agent-sandbox — sandbox runtime integrations
- src/octic-agent-train — training utilities
- src/octic-agent-deploy — deployment utilities
- src/octic-agent-rust — Rust workspace
- ui — application UI
- web — web console
- docker — container and Compose setup
- examples — examples and recipes
- ci — smoke tests

## Validation

Use the checks relevant to the files changed. For the main Python package:

    python -m pip install -e "src/octic_ai_agent[dev]"
    python ci/smoke_test_api.py
    python -m compileall -q src/octic_ai_agent

For the Rust workspace:

    cd src/octic-agent-rust
    cargo fmt --all -- --check
    cargo test --workspace

If a check cannot be run in the available environment, state that clearly rather than implying it passed.

## Documentation

Keep commands and paths aligned with the current repository layout. Prefer links to files and directories that actually exist. Do not add promotional claims, external endorsements, or author identities unless they are verified and relevant.

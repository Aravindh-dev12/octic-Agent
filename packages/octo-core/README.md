# Octo Core Engine

**Containerized Autonomous AI Agent Engine with Filesystem Isolation**

Octo Core powers the secure execution runtime for the Octo Agent platform. Agents run in their own dedicated Linux containers with explicit filesystem mounts, structured state, and multi-channel messaging adapters.

---

## Key Features

- **Filesystem Isolation**: Agents execute inside containerized environments and can only access directories mounted by the user.
- **Multi-Channel Adapters**: Native messaging adapters for Slack, Discord, Telegram, WhatsApp, Webhooks, and CLI.
- **SQLite State Management**: Persistent memory, conversation sessions, scheduled tasks, and token metrics backed by `better-sqlite3`.
- **Octo CLI**: Command-line control interface (`octo`) to manage groups, sessions, and agents.

---

## Quick Start

```bash
# Start the Octo Core development daemon
pnpm dev

# Run the Octo Agent CLI
pnpm octo -- help
```

---

## Architecture

- `src/container-runner.ts` — Manages Docker/container lifecycle and filesystem boundaries.
- `src/channels/` — Channel adapters (Slack, Discord, Telegram, WhatsApp, Webhooks).
- `src/session-manager.ts` — State, session serialization, and memory management.
- `src/router.ts` — Command routing and prompt pipeline.
- `src/cli/` — Terminal client (`octo`).

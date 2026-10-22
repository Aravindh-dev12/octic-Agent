# Octo Agent — Agent & Workforce Guide

This document defines development standards, monorepo architecture, and workforce orchestration guidelines for **Octo Agent**.

---

## Project Overview

Octo Agent combines a 3D virtual office workspace, containerized agent engine, and live request dashboard:

1. **Octo 3D (`packages/octo-3d`)**: Walkable retro office workspace with desks, meeting spaces, PR review center, and 3D floorplan builder.
2. **Octo Core (`packages/octo-core`)**: Lightweight agent runtime powered by Linux containers, filesystem isolation, SQLite state management, and multi-channel messaging (Slack, Discord, Telegram, WhatsApp, CLI).
3. **Octo Office (`packages/octo-office`)**: 2D isometric office dashboard with multi-step request pipeline visualization, live agent activity logs, and token/cost tracking.
4. **Chief Octo Mascot (`public/mascot`)**: Interactive WebGL 3D GLTF model (`octopus.wasm`) with mouse gaze tracking, wave kinematics, and live speech bubbles.

---

## Monorepo Layout

```
octic-Agent/
├── packages/
│   ├── octo-3d/         Claw3D retro virtual office (Three.js / React Three Fiber / Next.js)
│   ├── octo-core/       NanoClaw containerized agent runtime & CLI (`octo`)
│   └── octo-office/     OpenClaw 2D isometric dashboard & workflow pipeline (Next.js)
├── public/
│   ├── mascot/          3D octopus model (octopus.wasm) & WebGL interactive viewer
│   └── logo.svg         Official Octo Agent brand logo
├── assets/              Branding, flat SVG icons, mascot assets
├── scripts/             Launch, dev, and test scripts
├── package.json         Root monorepo workspace orchestration
└── pnpm-workspace.yaml  Workspace configuration
```

---

## Workforce Roles & Personas

In Octo Agent, autonomous agents operate in dedicated office zones:

| Agent Role | Package / Zone | Responsibilities |
|---|---|---|
| **Chief Octo** | Office Lobby / 3D Mascot | Coordinates tasks, delegates incoming requests across specialist agents. |
| **Code Reviewer** | PR Room (`octo-3d`) | Reviews pull requests, runs lint and unit test checks, delivers code feedback. |
| **Security Auditor** | Sandbox Hub (`octo-core`) | Verifies container isolation, inspects file mounts, guards credential store. |
| **DevOps Specialist** | Server Bay (`octo-3d`) | Monitors deployment, manages Docker/container lifecycles, checks system health. |
| **Pipeline Visualizer** | Dashboard (`octo-office`) | Tracks real-time token spend, step execution graph, and workflow latency. |

---

## Development Standards

1. **Decoupled Packages**: Each package in `packages/` is self-contained with independent dependencies and configuration, connected via standard HTTP/WebSocket gateways.
2. **Preserve Isolation**: Containerized agent actions inside `packages/octo-core` must remain strictly sandboxed. Never bypass filesystem isolation without explicit confirmation.
3. **Maintain 3D Performance**: Keep 3D retro office shaders and Three.js draw calls optimized for 60 FPS.
4. **Naming Consistency**: The project name is **Octo Agent** (CLI: `octo`).
5. **Brand Integrity**: All visual touchpoints use flat vector iconography and the consistent purple/slate theme (`#805ad5`, `#b794f6`, `#0f0c1b`).

---

## Key Commands

```bash
# Start 3D Retro Office (Port 3000)
npm run dev:3d

# Start 2D Isometric Dashboard (Port 4200)
npm run dev:office

# Start Octo Core Container Runtime
npm run dev:core

# Launch Interactive 3D Octopus Mascot
npm run mascot

# Run Octo Agent CLI
npm run octo -- --help
```

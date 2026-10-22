# 🐙 Octo Agent — Agent & Workforce Guide

Welcome to the **Octo Agent** monorepo. This document defines the development rules, architecture conventions, and multi-agent workforce guidelines for Octo Agent.

---

## 🌟 Project Overview

**Octo Agent** is a unified 3D Virtual Workspace, Real-Time Dashboard, and Containerized Multi-Agent Workforce platform. It merges three core foundations:

1. **Octo Core (`packages/octo-core`)**: Lightweight, secure agent runtime powered by Linux containers, filesystem isolation, SQLite state management, and multi-channel messaging (Slack, Discord, Telegram, WhatsApp, CLI).
2. **Octo 3D (`packages/octo-3d`)**: Walkable 3D retro office workspace with desks, conference rooms, PR review center, gym, office layout builder, and live agent avatars.
3. **Octo Office (`packages/octo-office`)**: 2D isometric office dashboard with multi-step request pipeline visualization, live agent activity logs, and token/cost tracking.
4. **Octo Mascot (3D Purple Octopus)**: Interactive WebGL GLTF model with mouse gaze tracking, wave kinematics, and live speech bubbles, acting as the Chief Orchestrator avatar.

---

## 🏛️ Monorepo Structure

```
octic-Agent/
├── packages/
│   ├── octo-core/       # Containerized agent runtime & CLI (`octo`)
│   ├── octo-3d/         # 3D Retro virtual office (Three.js / React Three Fiber / Next.js)
│   └── octo-office/     # 2D Isometric dashboard & workflow pipeline (Next.js)
├── public/
│   ├── mascot/          # 3D Octopus model (octopus.wasm) & WebGL interactive viewer
│   └── logo.svg         # Official Octo Agent SVG brand logo
├── assets/              # Branding, diagrams, mascot visual assets
├── scripts/             # Unified launch, dev, and test scripts
├── package.json         # Root monorepo workspace orchestration
└── pnpm-workspace.yaml  # Workspace configuration
```

---

## 📋 Workforce Roles & Personas

In Octo Agent, autonomous agents work in a 3D virtual office:

| Agent Role | Package / Zone | Responsibilities |
|---|---|---|
| **Chief Octo** | Office Lobby / 3D Mascot | Coordinates tasks, delegates incoming requests across the 8 tentacles (specialist agents). |
| **Code Reviewer** | PR Room (`octo-3d`) | Reviews pull requests, runs lint and unit test checks, gives code feedback. |
| **Security Auditor** | Sandbox Hub (`octo-core`) | Verifies container isolation, inspects file mounts, guards credential store. |
| **DevOps Specialist** | Server Bay (`octo-3d`) | Monitors deployment, manages Docker/container lifecycles, checks system health. |
| **Pipeline Visualizer** | Dashboard (`octo-office`) | Tracks real-time token spend, step execution graph, and workflow latency. |

---

## 🛠️ Development Rules

1. **Keep Packages Decoupled**: Each package in `packages/` is self-contained with its own dependencies and configuration, connected via standard HTTP/WebSocket gateways.
2. **Preserve Isolation**: Containerized agent actions inside `packages/octo-core` must remain strictly sandboxed. Never bypass filesystem isolation without explicit user confirmation.
3. **Maintain 3D Office Performance**: Keep 3D retro office shaders and Three.js draw calls optimized (target 60 FPS).
4. **Naming Consistency**: The official project name is **Octo Agent** (CLI: `octo`). Do not refer to the project as "octic" or legacy names.
5. **Brand Integrity**: All visual touchpoints should feature the Purple Octopus mascot and consistent cyber-retro palette (`#805ad5`, `#b794f6`, `#120c24`).

---

## 🚀 Key Commands

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

# Octo Agent — Agent & Workforce Guide

This document defines development standards, monorepo architecture, and workforce orchestration guidelines for **Octo Agent**.

---

## Project Overview

Octo Agent connects autonomous AI agents directly to 3D model creation, parametric mesh synthesis, and spatial 3D virtual workspaces:

1. **Octo 3D Model Studio (`packages/octo-3d/src/app/create-3d`)**: Natural language prompt-to-3D agent synthesis, procedural geometry assembly, PBR material customization, and 3D JSON/GLTF export.
2. **Octo 3D Workspace (`packages/octo-3d`)**: Walkable retro 3D workspace with interactive terminals, spatial agent presence, and 3D layout builder.
3. **Chief Octo Mascot (`public/mascot`)**: Interactive WebGL 3D GLTF model (`octopus.wasm`) with real-time mouse gaze tracking, wave kinematics, and live speech bubbles.
4. **Octo Core (`packages/octo-core`)**: Lightweight agent runtime powered by Linux containers, filesystem isolation, SQLite state management, and multi-channel messaging (CLI, Webhooks).

---

## Monorepo Layout

```
octo-agent-workforce/
├── packages/
│   ├── octo-3d/         Octo 3D virtual workspace & Agent 3D Model Studio (Three.js / React Three Fiber / Next.js)
│   └── octo-core/       Octo Core containerized agent runtime & CLI (`octo`)
├── public/
│   ├── mascot/          3D octopus model (octopus.wasm) & WebGL interactive viewer
│   └── logo.svg         Official Octo Agent brand logo
├── assets/              Branding, flat vector SVG icons, mascot assets
├── scripts/             Launch, dev, and test scripts
├── package.json         Root monorepo workspace orchestration
└── pnpm-workspace.yaml  Workspace configuration
```

---

## Workforce Roles & Personas

In Octo Agent, autonomous agents specialize in 3D generative synthesis and spatial coordination:

| Agent Role | Package / Zone | Responsibilities |
|---|---|---|
| **Chief Octo** | Studio Hub / 3D Mascot | Coordinates tasks, delegates user 3D design prompts across specialist synthesis agents. |
| **3D Mesh Architect** | 3D Studio (`/create-3d`) | Deconstructs natural language prompts into parametric 3D primitive geometry (boxes, spheres, cylinders, cones, toruses). |
| **PBR Material Specialist** | 3D Studio (`/create-3d`) | Configures colors, roughness, metalness, and emissive neon shaders for 3D components. |
| **Spatial Coordinator** | Workspace (`/office`) | Positions synthesized 3D models into spatial workspace layouts and validates collision bounds. |
| **Security Auditor** | Sandbox Hub (`octo-core`) | Verifies container isolation, inspects file mounts, and guards credential stores during synthesis jobs. |

---

## Development Standards

1. **Decoupled Packages**: Each package in `packages/` is self-contained with independent dependencies and configuration, connected via standard HTTP/WebSocket gateways.
2. **Preserve Isolation**: Containerized agent actions inside `packages/octo-core` must remain strictly sandboxed. Never bypass filesystem isolation without explicit confirmation.
3. **Maintain 3D Performance**: Keep 3D retro office shaders, procedural mesh generation, and Three.js draw calls optimized for 60 FPS.
4. **Naming Consistency**: The project name is **Octo Agent** (CLI: `octo`).
5. **Brand Integrity**: All visual touchpoints use flat vector iconography and the consistent purple/slate theme (`#805ad5`, `#b794f6`, `#0f0c1b`).

---

## Key Commands

```bash
# Start Agent 3D Model Studio & 3D Workspace (Port 3000)
npm run dev:3d

# Launch Interactive 3D Octopus Mascot (Port 8080)
npm run mascot

# Start Octo Core Container Runtime
npm run dev:core

# Run Octo Agent CLI
npm run octo -- --help
```

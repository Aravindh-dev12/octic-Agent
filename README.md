<p align="center">
  <img src="assets/octo-logo.svg" alt="Octo Agent" width="800">
</p>

<p align="center">
  <strong>The 3D Autonomous Multi-Agent Workforce &amp; Virtual Office Platform</strong>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Status-Production%20Ready-10b981?style=for-the-badge" alt="Status"></a>
  <a href="#-the-3-in-1-architecture"><img src="https://img.shields.io/badge/Architecture-3--in--1%20Monorepo-8b5cf6?style=for-the-badge" alt="Architecture"></a>
  <a href="public/mascot/index.html"><img src="https://img.shields.io/badge/3D%20Mascot-Purple%20Octopus%20GLTF-ec4899?style=for-the-badge&logo=three.js" alt="3D Mascot"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-3b82f6?style=for-the-badge" alt="License"></a>
</p>

---

## 🌟 What is Octo Agent?

**Octo Agent** is a full-stack, 3D-first autonomous agent workforce platform. Instead of managing AI agents through boring terminal logs and flat text dumps, **Octo Agent** gives your AI team physical presence, spatial awareness, and real-time collaboration inside an immersive virtual office.

We have unified the best of three open-source agent ecosystems into one powerhouse monorepo:

1. **🎮 Claw3D (Octo 3D Workspace)** — Walkable retro 3D office, customizable floorplans, agent desk avatars, PR review rooms, gym, and live collaboration.
2. **🛡️ NanoClaw (Octo Core Engine)** — Lightweight, hyper-secure containerized runtime. Every agent runs in its own isolated Linux container with strict filesystem mounts, SQLite state, and multi-channel adapters (Slack, Discord, Telegram, WhatsApp, CLI).
3. **🏢 OpenClaw Office (Octo Office Dashboard)** — 2D isometric dashboard, multi-step pipeline visualizer (User $\to$ Chief Octo $\to$ Specialist $\to$ Delivery), token spend and cost savings analytics.
4. **🐙 Chief Octo 3D Mascot** — Animated 3D WebGL purple octopus model with procedural harmonic tentacle physics, mouse-gaze tracking, blinking, and live speech bubbles.

---

## 🐙 Meet the 3D Purple Octopus Mascot

<p align="center">
  <img src="assets/octo-logo.svg" alt="Octo Mascot" width="480">
</p>

Octo Agent's official mascot and chief orchestrator is the **3D Purple Octopus**, built directly from the high-fidelity GLTF/GLB model (`octopus.wasm`):

- **Procedural Arm Kinematics**: Custom vertex shaders dynamically ripple each of the 8 arms using harmonic phase offsets ($\Delta \theta = 2.399 \text{ rad}$).
- **Mouse & Cursor Eye Tracking**: Screen-to-UV Jacobian mapping calculates the precise direction of your cursor so the octopus watches you as you navigate.
- **Natural Blinking & Mood**: Periodic smooth eyelid squashing and pupil dilation.
- **Embedded Mascot Viewer**: Run `npm run mascot` to spin up a standalone WebGL viewer on `http://localhost:8080`, or visit `/mascot` inside the 3D office suite!

---

## 🏛️ The 3-in-1 Architecture

```
octic-Agent/
├── packages/
│   ├── octo-core/        🛡️ Core Engine (Containerized Agents, CLI, Channels, SQLite)
│   ├── octo-3d/          🎮 3D Retro Virtual Office & Studio (Three.js / React Three Fiber)
│   └── octo-office/      🏢 2D Isometric Dashboard & Real-Time Pipeline (Next.js)
├── public/
│   ├── mascot/           🐙 3D Animated Octopus (octopus.wasm & WebGL Interactive Canvas)
│   └── logo.svg          🎨 Official Octo Agent Brand SVG
├── assets/               🖼️ Branding assets, screenshots, and visual badges
├── scripts/              ⚡ Standalone mascot server, launch scripts, test runners
├── AGENTS.md             📋 Multi-agent workforce guide and development policies
├── ARCHITECTURE.md       📐 In-depth system diagrams and technical specifications
└── package.json          📦 Root monorepo workspace orchestrator
```

### Feature Comparison

| Feature | Octo 3D (`packages/octo-3d`) | Octo Office (`packages/octo-office`) | Octo Core (`packages/octo-core`) |
|---|:---:|:---:|:---:|
| **Primary Environment** | 3D Retro Office (WebGL) | 2D Isometric Dashboard | Headless Daemon & CLI |
| **Agent Visuals** | Walkable 3D Avatars & Desks | 2D Sprites & Desks | Container IDs & Logs |
| **Office Builder** | Built-in 3D Layout Editor | Config JSON Wizard | N/A |
| **Agent Isolation** | Web/Studio UI layer | Gateway telemetry layer | Linux Container Sandboxes |
| **Channel Integrations** | Web chat & studio console | REST/WebSocket notifications | Slack, Discord, Telegram, WhatsApp, CLI |
| **3D Octopus Mascot** | Embedded interactive page (`/mascot`) | Mascot tab in dashboard | Chief Orchestrator Avatar |

---

## 🚀 Quick Start

### 1. Prerequisites
- **Node.js**: v20 or v22+
- **Docker** (optional, recommended for OS-level container isolation)
- **Git**

### 2. Clone and Install

```bash
git clone https://github.com/Aravindh-dev12/octic-Agent.git
cd octic-Agent

# Install dependencies across all packages
npm install
```

### 3. Launch Services

You can run individual services or start the entire suite:

```bash
# 🎮 Launch the 3D Retro Virtual Office (Default Port: 3000)
npm run dev:3d
# Open: http://localhost:3000/office

# 🐙 Launch the Standalone 3D Octopus Mascot Viewer (Port: 8080)
npm run mascot
# Open: http://localhost:8080

# 🏢 Launch the 2D Isometric Office Dashboard (Default Port: 4200)
npm run dev:office
# Open: http://localhost:4200

# 🛡️ Launch the Octo Core Agent Container Runtime
npm run dev:core
```

Or on Windows PowerShell:
```powershell
.\scripts\start-all.ps1
```

Or on Linux / macOS:
```bash
bash scripts/start-all.sh
```

---

## 💻 CLI Reference (`octo`)

Octo Agent includes a terminal CLI to control your workforce:

```bash
# Display CLI commands
npm run octo -- --help

# Chat directly with your agent workforce
npm run octo -- chat

# Check system health, container runtimes, and gateway connections
npm run octo -- doctor

# Inspect active agent sessions
npm run octo -- sessions
```

---

## 🎮 Exploring the 3D Retro Office

Once `npm run dev:3d` is running at `http://localhost:3000/office`:

- **Move Around**: Use `WASD` or Arrow keys to walk your avatar across the office floor.
- **Camera Angles**: Click and drag to orbit, rotate, and zoom the 3D workspace.
- **Desks & Rooms**: Walk up to desks to see which agent is working, their current task, and live tool execution.
- **PR Review Center**: Review pull requests collaboratively inside the office.
- **Office Builder (`/office/builder`)**: Customize your office layout — add desks, servers, meeting tables, coffee machines, and neon signs.
- **Chief Octo Mascot (`/mascot`)**: Visit the dedicated 3D Octopus mascot chamber to view real-time multi-agent orchestration.

---

## 🏢 Exploring the 2D Isometric Dashboard

Once `npm run dev:office` is running at `http://localhost:4200`:

- **Request Pipeline**: Watch real-time task handoffs (e.g., Slack query $\to$ Orchestrator $\to$ Code Specialist $\to$ Tester).
- **Activity Stream**: Filter logs by agent, error level, or token cost.
- **Cost Savings**: Track cumulative token savings and speedups compared to manual workflows.
- **3D Mascot Tab**: Switch to the Mascot tab to view the interactive 3D Octopus model directly within the dashboard.

---

## 🔒 Security & Containment

In Octo Agent, security is not an afterthought:
- **Filesystem Isolation**: Agents cannot modify files outside their designated project mount.
- **Container Sandboxing**: Terminal commands run inside a dedicated container rather than on the host machine.
- **Human-in-the-Loop Approvals**: High-risk actions (e.g. bash commands, deleting files) trigger interactive approval prompts in the 3D Studio and terminal.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Built with ❤️ by the **Octo Agent Team**.

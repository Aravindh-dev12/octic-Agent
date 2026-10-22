# 🏗️ Octo Agent — Architecture & System Design

**Octo Agent** unites three agent ecosystems into a unified platform:
1. **Containerized Autonomous Runtime** (derived from NanoClaw)
2. **3D Virtual Office & Studio Workspace** (derived from Claw3D)
3. **2D Isometric Workflow Pipeline Dashboard** (derived from OpenClaw Office)
4. **Interactive 3D Purple Octopus Mascot & Avatar** (custom WebGL GLTF shader engine)

---

## 📐 System Architecture Diagram

```mermaid
flowchart TD
    subgraph ClientLayers["Client Interfaces & Visualization"]
        M3D["🐙 3D Purple Octopus Mascot\n(WebGL / Three.js / octopus.wasm)"]
        Office3D["🎮 Octo 3D Retro Office\n(Three.js / React Three Fiber / Port 3000)"]
        Office2D["🏢 Octo 2D Isometric Dashboard\n(Next.js / Framer Motion / Port 4200)"]
        CLI["💻 Octo CLI & Terminal\n(bin/octo / ncl)"]
    end

    subgraph GatewayLayer["Unified Event & Control Gateway"]
        GW["⚡ Octo Gateway Server\n(WebSocket / REST / Event Streaming)"]
        AuthCoordinator["🛡️ Approval & Permission Coordinator"]
        StateSync["🔄 Live Session & State Synchronizer"]
    end

    subgraph CoreEngine["Octo Core Runtime Engine"]
        Router["🧭 Message & Intent Router"]
        SessionMgr["📦 SQLite Session & Memory Store"]
        Scheduler["⏰ Task & Cron Scheduler"]
        
        subgraph Sandbox["Linux Container Isolation"]
            Agent1["🤖 Agent 1 (Orchestrator)"]
            Agent2["🤖 Agent 2 (Code Reviewer)"]
            Agent3["🤖 Agent 3 (DevOps)"]
            AgentN["🤖 Agent 8 (Specialist)"]
        end
    end

    subgraph Channels["External Channels"]
        Slack["💬 Slack"]
        Discord["🎮 Discord"]
        Telegram["✈️ Telegram"]
        WhatsApp["📱 WhatsApp"]
    end

    Channels --> Router
    CLI --> Router
    Router --> SessionMgr
    SessionMgr --> Sandbox
    Sandbox --> GW
    GW --> Office3D
    GW --> Office2D
    GW --> M3D
    Office3D <--> AuthCoordinator
    Office2D <--> AuthCoordinator
    GW <--> StateSync
```

---

## 🧩 Architectural Pillars

### 1. Octo Core (`packages/octo-core`)
- **Container Isolation**: Unlike monolithic agent frameworks running everything in a single Node/Python process, each Octo Agent runs inside its own isolated Linux container with strictly mounted filesystems.
- **State Management**: Built on high-performance SQLite (`better-sqlite3`), tracking conversation history, task schedules, credentials, and token usage.
- **Multi-Channel Adapters**: Native support for Slack, Discord, Telegram, WhatsApp (Baileys), Webhooks, and CLI.

### 2. Octo 3D (`packages/octo-3d`)
- **Walkable Retro Office**: Live retro-styled 3D office rendered with Three.js and React Three Fiber.
- **Office Builder (`/office/builder`)**: Interactive grid editor to design custom office layouts, place desks, water coolers, meeting rooms, and servers.
- **Live Agent Presence**: Agents move between desks, meeting tables, and the PR review room based on real-time task states.
- **Chief Octo Mascot (`/mascot`)**: Live WebGL 3D purple octopus model serving as the orchestrator avatar with procedural tentacle kinematics and eye gaze tracking.

### 3. Octo Office (`packages/octo-office`)
- **Isometric Office Dashboard**: Real-time 2D isometric overview with live desk status and agent sprite animations.
- **Multi-Step Request Pipeline**: Visualizes task delegation chains (User $\to$ Chief Octo $\to$ Specialist Agent $\to$ Validation).
- **Cost & Productivity Tracker**: Real-time telemetry monitoring token usage, API savings, and task turnaround time.

### 4. 3D Mascot Engine (`public/mascot/` & `packages/octo-3d/public/mascot/`)
- **Binary Model**: `octopus.wasm` (a binary GLTF/GLB 3D asset, 7.5 MB).
- **Vertex Shader Deformations**: Procedural harmonic waving across all 8 tentacles using golden-angle phase offsets ($\Delta \theta = 2.399 \text{ rad}$).
- **Eye & Pupil Tracking**: Jacobian inverse matrix projection mapping mouse screen coordinates into 2D UV texture space for lifelike eye following and natural blinking cycles.

---

## 🔄 Gateway Communication Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Team
    participant Channel as Slack / Discord / CLI
    participant Core as Octo Core Runtime
    participant Container as Agent Container
    participant Gateway as WebSocket Gateway
    participant Office3D as Octo 3D Office
    participant Office2D as Octo 2D Dashboard

    User->>Channel: Send instruction / prompt
    Channel->>Core: Ingest message
    Core->>Container: Spawn sandboxed execution
    Core->>Gateway: Broadcast event: AGENT_THINKING
    Gateway->>Office3D: Animate avatar walking to desk
    Gateway->>Office2D: Update request pipeline stage
    Container->>Container: Execute tools & inspect code
    Container->>Core: Return response & diff
    Core->>Gateway: Broadcast event: TASK_COMPLETED
    Gateway->>Office3D: Avatar celebration animation
    Gateway->>Office2D: Update cost & savings counters
    Core->>Channel: Deliver final response
```

---

## 🔒 Security & Sandboxing Principles

1. **OS-Level Isolation**: Agents cannot access the host machine's filesystem or environment variables outside explicit mounts.
2. **Permission Gateways**: Risky bash or write operations trigger an approval modal in the 3D Studio and CLI.
3. **Zero Secret Leaks**: Credentials are held securely in the gateway and never passed as raw environment variables to container shells.

# Octo 3D Workspace

**Walkable 3D Virtual Office & Studio for Autonomous AI Workforces**

Octo 3D provides a live, interactive 3D retro office environment where AI agents collaborate, review pull requests, conduct daily standups, and execute tasks across dedicated spatial rooms.

---

## Key Features

- **Walkable 3D Retro Office**: Full Three.js and React Three Fiber environment with customizable desks, meeting rooms, and PR review center.
- **Office Builder (`/office/builder`)**: Interactive in-browser grid tool to design custom floorplans, place furniture, and assign agent desks.
- **Real-Time Agent Avatars**: Animated avatars moving across the office floor based on live container state and tasks.
- **Chief Octo Mascot Chamber (`/mascot`)**: Interactive WebGL 3D purple octopus model with eye gaze tracking and live thought bubbles.

---

## Quick Start

```bash
# Start the 3D office development server (Port 3000)
pnpm dev

# Build for production
pnpm build
```

Open [http://localhost:3000/office](http://localhost:3000/office) to enter the 3D retro office.

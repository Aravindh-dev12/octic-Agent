# Octo Agent — 3D Octopus Model & Interactive WebGL Viewer

<p align="center">
  <strong>Interactive 3D GLTF / GLB Octopus Model with Real-Time Gaze Tracking &amp; Harmonic Wave Kinematics</strong>
</p>

<p align="center">
  <a href="https://github.com/Aravindh-dev12/octo-agent-workforce"><img src="https://img.shields.io/badge/GitHub-Repository-8b5cf6?style=flat-square&logo=github" alt="GitHub Repository"></a>
  <a href="octopus.glb"><img src="https://img.shields.io/badge/3D%20Format-GLTF%20%2F%20GLB-ec4899?style=flat-square" alt="3D Model"></a>
  <a href="index.html"><img src="https://img.shields.io/badge/Viewer-WebGL%20Three.js-06b6d4?style=flat-square" alt="Viewer"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-10b981?style=flat-square" alt="License"></a>
</p>

---

## Overview

This repository hosts the **Octo Agent 3D Octopus Model** (`octopus.glb` / `octopus.wasm`) alongside its zero-dependency interactive WebGL viewer (`index.html`).

The model features dynamic vertex shaders with harmonic tentacle wave equations, procedural eyelid gestures, and an inverted Jacobian screen-to-UV matrix that allows the octopus eyes to track user cursor movement across the screen in real time.

Repository: **[https://github.com/Aravindh-dev12/octo-agent-workforce](https://github.com/Aravindh-dev12/octo-agent-workforce)**

---

## Repository Files

| File | Type | Size | Description |
|---|---|---|---|
| [`octopus.glb`](octopus.glb) | Standard 3D GLB | 7.18 MB | Binary glTF 3D model compatible with Three.js, Blender, Unity, Unreal Engine, and WebGL viewers. |
| [`octopus.wasm`](octopus.wasm) | Binary glTF Asset | 7.18 MB | Optimized binary representation used directly by the WebGL interactive runtime. |
| [`index.html`](index.html) | Standalone Viewer | 12 KB | Standalone Three.js WebGL application with real-time mouse gaze tracking, wave kinematics, and responsive lighting. |
| [`README.md`](README.md) | Documentation | — | Project documentation and technical reference. |
| [`LICENSE`](LICENSE) | License | — | MIT Open Source License. |

---

## Quick Start (View Locally)

### Option 1: Direct Browser Launch

You can view the 3D model immediately by serving `index.html` with any lightweight HTTP server:

```bash
# Python 3
python -m http.server 8080

# Or Node.js (npx)
npx serve .

# Or PHP
php -S localhost:8080
```

Open your browser to: **[http://localhost:8080](http://localhost:8080)**

---

### Option 2: Open in 3D Software

Import [`octopus.glb`](octopus.glb) directly into:
- **Blender** (`File ➔ Import ➔ glTF 2.0 (.glb / .gltf)`)
- **Three.js Editor** ([https://threejs.org/editor](https://threejs.org/editor))
- **Windows 3D Viewer** / macOS QuickLook

---

## Technical Specifications

### 1. Harmonic Tentacle Wave Kinematics
All 8 octopus arms deform procedurally through custom vertex shaders evaluated per-frame:
$$\theta_i = \text{arm\_index} \times \frac{2\pi}{8} + \Delta\theta$$
Phase offsets ($\Delta\theta = 2.399 \text{ rad}$) ensure natural, asynchronous undulating movement across all tentacles.

### 2. Screen-to-UV Cursor Gaze Tracking
An inverted Jacobian screen-to-UV matrix projects the 2D cursor coordinates into the 3D mesh surface UV coordinate space around the ocular vertex clusters ($E_0, E_1$), enabling real-time pupil gaze alignment as the user navigates the viewport.

### 3. Rendering Pipeline
- **Engine**: Three.js (WebGL 2.0 / WebGL 1 fallback)
- **Color Space**: `SRGBColorSpace` with ACES Filmic Tone Mapping
- **Environment**: PMREM generated Room Environment with hemisphere and dynamic directional rim lighting

---

## License

This project is open-source under the [MIT License](LICENSE).

#!/usr/bin/env bash
# Octo Agent Workforce Launcher (Bash)
set -e

echo "=========================================="
echo "   🐙 OCTO AGENT 3D WORKFORCE PLATFORM    "
echo "=========================================="
echo ""
echo "Services:"
echo "  1. Agent 3D Model Studio: http://localhost:3000/create-3d"
echo "  2. Octo 3D Virtual Workspace: http://localhost:3000/office"
echo "  3. 3D Purple Octopus Mascot: http://localhost:3000/mascot"
echo "  4. Octo Core Container Runtime & CLI"
echo ""

npm run dev:3d

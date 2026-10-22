#!/usr/bin/env bash
# Octo Agent Workforce Launcher (Bash)
set -e

echo "=========================================="
echo "   🐙 OCTO AGENT 3D WORKFORCE PLATFORM    "
echo "=========================================="
echo ""
echo "Services:"
echo "  1. Octo 3D Virtual Office: http://localhost:3000/office"
echo "  2. 3D Purple Octopus Mascot: http://localhost:3000/mascot"
echo "  3. Octo 2D Office Dashboard: http://localhost:4200"
echo "  4. Octo Core Container Runtime & CLI"
echo ""

npm run dev:3d

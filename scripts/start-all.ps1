# Octo Agent Workforce Launcher (PowerShell)
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   🐙 OCTO AGENT 3D WORKFORCE PLATFORM    " -ForegroundColor Magenta
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting Octo Agent services:" -ForegroundColor Yellow
Write-Host "  1. Octo 3D Virtual Office: http://localhost:3000/office" -ForegroundColor Green
Write-Host "  2. 3D Purple Octopus Mascot: http://localhost:3000/mascot" -ForegroundColor Green
Write-Host "  3. Octo 2D Office Dashboard: http://localhost:4200" -ForegroundColor Green
Write-Host "  4. Octo Core Container Runtime & CLI" -ForegroundColor Green
Write-Host ""

npm run dev:3d

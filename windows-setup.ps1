# AWS-InfoBlox Integration Setup for Windows WSL2
# PowerShell Version

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "AWS-InfoBlox Integration Setup for Windows WSL2" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as Administrator (recommended)
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "WARNING: Not running as Administrator. Some features may not work." -ForegroundColor Yellow
    Write-Host ""
}

# Check WSL2 installation
try {
    $wslStatus = wsl --status 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "WSL not installed"
    }
    Write-Host "✓ WSL2 is installed" -ForegroundColor Green
} catch {
    Write-Host "✗ WSL2 is not installed" -ForegroundColor Red
    Write-Host "Please install WSL2 by running: wsl --install" -ForegroundColor Yellow
    exit 1
}

# Check Docker Desktop
try {
    $dockerVersion = docker version 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Docker not running"
    }
    Write-Host "✓ Docker Desktop is running" -ForegroundColor Green
} catch {
    Write-Host "✗ Docker Desktop is not running" -ForegroundColor Red
    Write-Host "Please start Docker Desktop" -ForegroundColor Yellow
    exit 1
}

# Check for Ubuntu distribution
$distributions = wsl -l -q
if ($distributions -notcontains "Ubuntu") {
    Write-Host "✗ Ubuntu distribution not found in WSL" -ForegroundColor Red
    Write-Host "Installing Ubuntu..." -ForegroundColor Yellow
    wsl --install -d Ubuntu
    Write-Host "Please complete Ubuntu setup and run this script again" -ForegroundColor Yellow
    exit 1
}
Write-Host "✓ Ubuntu distribution found" -ForegroundColor Green

Write-Host ""
Write-Host "Prerequisites check passed!" -ForegroundColor Green
Write-Host ""

# Create project directory
Write-Host "Creating project directory in WSL Ubuntu..." -ForegroundColor Cyan
wsl -d Ubuntu -e bash -c "mkdir -p ~/marriot-infoblox"

# Get WSL username
$wslUser = wsl -d Ubuntu -e bash -c "echo `$USER"
$projectPath = "\\wsl$\Ubuntu\home\$wslUser\marriot-infoblox"

Write-Host ""
Write-Host "Project directory created at: $projectPath" -ForegroundColor Green
Write-Host ""

# List required files
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Required Files from Mac System" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Core files (REQUIRED):" -ForegroundColor Yellow
Write-Host "  1. config.env - Your InfoBlox credentials and settings"
Write-Host "  2. vpc_data.csv or vpc_data2.csv - AWS VPC data"
Write-Host "  3. aws_infoblox_vpc_manager_enhanced.py - Main application"
Write-Host ""
Write-Host "Optional files:" -ForegroundColor Yellow
Write-Host "  4. modified_properties_file.csv - For property imports"
Write-Host "  5. Terminal test files:"
Write-Host "     - terminal_integration_summary.md"
Write-Host "     - terminal_test_results.txt"
Write-Host "     - terminal_test_detailed.json"
Write-Host "     - comprehensive_terminal_test.py"
Write-Host "     - interactive_terminal_test.py"
Write-Host "     - test_terminal_integration.py"
Write-Host ""

# Create helper function for file copying
Write-Host "Creating file copy helper..." -ForegroundColor Cyan

$copyScript = @'
# File Copy Helper Function
function Copy-ToWSL {
    param(
        [string]$SourcePath,
        [string]$FileName
    )
    
    if (Test-Path "$SourcePath\$FileName") {
        Copy-Item "$SourcePath\$FileName" -Destination "\\wsl$\Ubuntu\home\$env:WSL_USER\marriot-infoblox\" -Force
        Write-Host "✓ Copied $FileName" -ForegroundColor Green
    } else {
        Write-Host "✗ File not found: $FileName" -ForegroundColor Red
    }
}

# Set WSL username
$env:WSL_USER = (wsl -d Ubuntu -e bash -c "echo `$USER").Trim()

# Example usage:
# Copy-ToWSL -SourcePath "C:\YourPath" -FileName "config.env"
# Copy-ToWSL -SourcePath "C:\YourPath" -FileName "vpc_data.csv"
'@

Write-Host $copyScript -ForegroundColor Gray
Write-Host ""

# Create application files in WSL
Write-Host "Creating application structure..." -ForegroundColor Cyan

# Create requirements.txt
$requirements = @"
pandas>=1.3.0
requests>=2.25.0
urllib3>=1.26.0
python-dotenv>=0.19.0
"@

$requirements | wsl -d Ubuntu -e bash -c "cat > ~/marriot-infoblox/requirements.txt"

# Create docker-compose.yml
$dockerCompose = @"
services:
  infoblox-tag-mapper:
    image: python:3.9-slim
    container_name: infoblox-tag-mapper
    working_dir: /app
    volumes:
      - ./:/app
      - ./logs:/app/logs
      - ./reports:/app/reports
    environment:
      - PYTHONUNBUFFERED=1
    ports:
      - '5002:5002'
    command: tail -f /dev/null
    restart: unless-stopped
"@

$dockerCompose | wsl -d Ubuntu -e bash -c "cat > ~/marriot-infoblox/docker-compose.yml"

# Create Dockerfile
$dockerfile = @"
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs reports data

ENV PYTHONUNBUFFERED=1

CMD ['tail', '-f', '/dev/null']
"@

$dockerfile | wsl -d Ubuntu -e bash -c "cat > ~/marriot-infoblox/Dockerfile"

# Create setup script
$setupScript = @'
#!/bin/bash
echo "Setting up AWS-InfoBlox Integration..."

# Create necessary directories
mkdir -p logs reports data

# Set permissions
chmod +x *.sh 2>/dev/null

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "Docker not found in WSL. Ensure Docker Desktop WSL integration is enabled."
    echo "Go to Docker Desktop Settings > Resources > WSL Integration"
    exit 1
fi

# Build container
echo "Building Docker container..."
docker compose build

# Start container
echo "Starting container..."
docker compose up -d

# Wait for container
sleep 3

# Check status
if docker ps | grep -q infoblox-tag-mapper; then
    echo ""
    echo "✓ Setup complete! Container is running."
    echo ""
    echo "To run the import:"
    echo "  docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager_enhanced.py"
    echo ""
    echo "To check logs:"
    echo "  docker logs infoblox-tag-mapper"
else
    echo "✗ Container failed to start. Check Docker Desktop."
    exit 1
fi
'@

$setupScript | wsl -d Ubuntu -e bash -c "cat > ~/marriot-infoblox/setup.sh && chmod +x ~/marriot-infoblox/setup.sh"

# Create run script
$runScript = @'
#!/bin/bash
if [ ! -f "config.env" ]; then
    echo "ERROR: config.env not found. Please copy it from your Mac system."
    exit 1
fi

if [ ! -f "aws_infoblox_vpc_manager_enhanced.py" ]; then
    echo "ERROR: aws_infoblox_vpc_manager_enhanced.py not found."
    exit 1
fi

echo "Running AWS-InfoBlox VPC Manager..."
docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager_enhanced.py
'@

$runScript | wsl -d Ubuntu -e bash -c "cat > ~/marriot-infoblox/run.sh && chmod +x ~/marriot-infoblox/run.sh"

Write-Host "✓ Application structure created" -ForegroundColor Green
Write-Host ""

# Final instructions
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Setup Complete! Next Steps:" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Copy your files to WSL:" -ForegroundColor Yellow
Write-Host "   Option A: Use Windows Explorer" -ForegroundColor White
Write-Host "   - Open: $projectPath" -ForegroundColor Gray
Write-Host "   - Drag and drop your files there" -ForegroundColor Gray
Write-Host ""
Write-Host "   Option B: Use PowerShell commands" -ForegroundColor White
Write-Host "   - Use the Copy-ToWSL function shown above" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Enter WSL Ubuntu:" -ForegroundColor Yellow
Write-Host "   wsl -d Ubuntu" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Navigate to project:" -ForegroundColor Yellow
Write-Host "   cd ~/marriot-infoblox" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Run setup:" -ForegroundColor Yellow
Write-Host "   ./setup.sh" -ForegroundColor Gray
Write-Host ""
Write-Host "5. Execute import:" -ForegroundColor Yellow
Write-Host "   ./run.sh" -ForegroundColor Gray
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan

# Offer to open WSL path in Explorer
$openExplorer = Read-Host "Would you like to open the WSL project folder in Windows Explorer? (Y/N)"
if ($openExplorer -eq 'Y' -or $openExplorer -eq 'y') {
    Start-Process "explorer.exe" -ArgumentList $projectPath
}

# Offer to start WSL
$startWSL = Read-Host "Would you like to open WSL Ubuntu now? (Y/N)"
if ($startWSL -eq 'Y' -or $startWSL -eq 'y') {
    wsl -d Ubuntu
}
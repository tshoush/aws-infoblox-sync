# PowerShell Setup Script for AWS to InfoBlox Tag Mapper
# Run this script as Administrator for best results

param(
    [string]$InstallPath = "C:\infoblox-tag-mapper",
    [switch]$SkipPrerequisites,
    [switch]$CreateShortcuts
)

# Set script parameters
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

# Color functions
function Write-Success { Write-Host $args -ForegroundColor Green }
function Write-Info { Write-Host $args -ForegroundColor Cyan }
function Write-Warning { Write-Host $args -ForegroundColor Yellow }
function Write-Error { Write-Host $args -ForegroundColor Red }

# Banner
Clear-Host
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "    AWS to InfoBlox Tag Mapper Setup" -ForegroundColor Cyan
Write-Host "    PowerShell Installation Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
if (-not $isAdmin) {
    Write-Warning "Not running as Administrator. Some features may not work."
    Write-Warning "For best results, run PowerShell as Administrator."
    Write-Host ""
}

# Function to check if a command exists
function Test-Command {
    param($Command)
    try {
        Get-Command $Command -ErrorAction Stop | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Check prerequisites
if (-not $SkipPrerequisites) {
    Write-Info "Checking prerequisites..."
    
    # Check Windows version
    $os = Get-CimInstance -ClassName Win32_OperatingSystem
    $version = [version]$os.Version
    if ($version.Major -lt 10 -or ($version.Major -eq 10 -and $version.Build -lt 19041)) {
        Write-Error "Windows 10 version 2004 or higher is required."
        Write-Error "Your version: $($os.Caption) (Build $($os.BuildNumber))"
        exit 1
    }
    Write-Success "✓ Windows version: OK"
    
    # Check WSL
    if (-not (Test-Command "wsl")) {
        Write-Error "WSL is not installed."
        Write-Host ""
        Write-Info "To install WSL, run this command as Administrator:"
        Write-Host "  wsl --install" -ForegroundColor White
        Write-Host ""
        
        if ($isAdmin) {
            $install = Read-Host "Would you like to install WSL now? (Y/N)"
            if ($install -eq 'Y') {
                Write-Info "Installing WSL..."
                wsl --install
                Write-Warning "Please restart your computer after installation completes."
                exit 0
            }
        }
        exit 1
    }
    Write-Success "✓ WSL: Installed"
    
    # Check Ubuntu
    $distros = wsl -l -q
    if ($distros -notcontains "Ubuntu") {
        Write-Error "Ubuntu is not installed in WSL."
        Write-Info "Please install Ubuntu from Microsoft Store."
        exit 1
    }
    Write-Success "✓ Ubuntu: Installed"
    
    # Check Docker Desktop
    $dockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    if (-not (Test-Path $dockerPath)) {
        Write-Error "Docker Desktop is not installed."
        Write-Info "Please download from: https://www.docker.com/products/docker-desktop/"
        Write-Info "Make sure to enable WSL2 integration during installation."
        exit 1
    }
    Write-Success "✓ Docker Desktop: Installed"
    
    # Check if Docker is running
    $dockerProcess = Get-Process "Docker Desktop" -ErrorAction SilentlyContinue
    if (-not $dockerProcess) {
        Write-Warning "Docker Desktop is not running. Starting it now..."
        Start-Process $dockerPath
        Write-Info "Waiting 30 seconds for Docker to start..."
        Start-Sleep -Seconds 30
    } else {
        Write-Success "✓ Docker Desktop: Running"
    }
}

# Create directory structure
Write-Host ""
Write-Info "Setting up directory structure..."

if (-not (Test-Path $InstallPath)) {
    New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null
    Write-Success "Created: $InstallPath"
} else {
    Write-Info "Directory exists: $InstallPath"
}

# Create subdirectories
$subdirs = @("data", "reports", "logs", "templates", "static")
foreach ($dir in $subdirs) {
    $path = Join-Path $InstallPath $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

# Check for required files
Write-Host ""
Write-Info "Checking application files..."
$requiredFiles = @(
    "tag_mapping_web_app.py",
    "aws_infoblox_vpc_manager_complete.py",
    "requirements_web.txt",
    "Dockerfile",
    "docker-compose.yml",
    "docker-entrypoint.sh",
    "setup.sh"
)

$missingFiles = @()
foreach ($file in $requiredFiles) {
    $filePath = Join-Path $InstallPath $file
    if (-not (Test-Path $filePath)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Error "Missing required files:"
    $missingFiles | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    Write-Host ""
    Write-Info "Please copy all application files to: $InstallPath"
    exit 1
}
Write-Success "✓ All required files present"

# Create config.env if not exists
$configPath = Join-Path $InstallPath "config.env"
if (-not (Test-Path $configPath)) {
    Write-Info "Creating config.env template..."
    @"
# InfoBlox Configuration
GRID_MASTER=
NETWORK_VIEW=default
INFOBLOX_USERNAME=
PASSWORD=

# CSV File Configuration
CSV_FILE=vpc_data.csv

# Container Detection Configuration
PARENT_CONTAINER_PREFIXES=
CONTAINER_HIERARCHY_MODE=strict
"@ | Out-File -FilePath $configPath -Encoding UTF8
    Write-Warning "Please edit config.env with your InfoBlox credentials"
}

# Copy Windows batch files
Write-Host ""
Write-Info "Setting up Windows integration..."
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$batchFiles = @(
    "start-tag-mapper.bat",
    "stop-tag-mapper.bat",
    "status-tag-mapper.bat",
    "logs-tag-mapper.bat"
)

foreach ($file in $batchFiles) {
    $source = Join-Path $scriptPath $file
    $dest = Join-Path $InstallPath $file
    if ((Test-Path $source) -and (-not (Test-Path $dest))) {
        Copy-Item $source $dest
    }
}

# Run setup in WSL
Write-Host ""
Write-Info "Running Docker setup in WSL Ubuntu..."
Write-Host ""

$wslCommand = "cd /mnt/c/infoblox-tag-mapper && chmod +x setup.sh && ./setup.sh"
$setupResult = wsl -d Ubuntu -- bash -c $wslCommand

if ($LASTEXITCODE -eq 0) {
    Write-Success "✓ Docker setup completed successfully!"
} else {
    Write-Error "Docker setup failed. Check the error messages above."
    exit 1
}

# Create shortcuts if requested
if ($CreateShortcuts) {
    Write-Host ""
    Write-Info "Creating desktop shortcuts..."
    
    $desktop = [Environment]::GetFolderPath("Desktop")
    $shell = New-Object -ComObject WScript.Shell
    
    # Start shortcut
    $shortcut = $shell.CreateShortcut("$desktop\Start Tag Mapper.lnk")
    $shortcut.TargetPath = "$InstallPath\start-tag-mapper.bat"
    $shortcut.WorkingDirectory = $InstallPath
    $shortcut.IconLocation = "shell32.dll,137"
    $shortcut.Description = "Start AWS to InfoBlox Tag Mapper"
    $shortcut.Save()
    
    # Stop shortcut
    $shortcut = $shell.CreateShortcut("$desktop\Stop Tag Mapper.lnk")
    $shortcut.TargetPath = "$InstallPath\stop-tag-mapper.bat"
    $shortcut.WorkingDirectory = $InstallPath
    $shortcut.IconLocation = "shell32.dll,131"
    $shortcut.Description = "Stop AWS to InfoBlox Tag Mapper"
    $shortcut.Save()
    
    # Status shortcut
    $shortcut = $shell.CreateShortcut("$desktop\Tag Mapper Status.lnk")
    $shortcut.TargetPath = "$InstallPath\status-tag-mapper.bat"
    $shortcut.WorkingDirectory = $InstallPath
    $shortcut.IconLocation = "shell32.dll,23"
    $shortcut.Description = "Check Tag Mapper Status"
    $shortcut.Save()
    
    Write-Success "✓ Desktop shortcuts created"
}

# Final summary
Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "    Setup Complete!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Success "Installation path: $InstallPath"
Write-Host ""
Write-Info "Next steps:"
Write-Host "1. Edit config.env with your InfoBlox credentials"
Write-Host "2. Copy your VPC CSV file to $InstallPath"
Write-Host "3. Run start-tag-mapper.bat to start the application"
Write-Host ""
Write-Info "Available commands:"
Write-Host "  start-tag-mapper.bat  - Start the application"
Write-Host "  stop-tag-mapper.bat   - Stop the application"
Write-Host "  status-tag-mapper.bat - Check status"
Write-Host "  logs-tag-mapper.bat   - View logs"
Write-Host ""

# Ask to start now
$start = Read-Host "Would you like to start the application now? (Y/N)"
if ($start -eq 'Y') {
    Write-Info "Starting AWS to InfoBlox Tag Mapper..."
    Start-Process -FilePath "$InstallPath\start-tag-mapper.bat" -WorkingDirectory $InstallPath
}

Write-Host ""
Write-Success "Setup script completed!"
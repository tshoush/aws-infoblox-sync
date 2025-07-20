# AWS to InfoBlox Tag Mapper - Windows WSL Setup Guide

This guide provides detailed step-by-step instructions for setting up the AWS to InfoBlox Tag Mapping Web Interface on Windows using WSL (Windows Subsystem for Linux) with Ubuntu.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Part 1: WSL and Ubuntu Setup](#part-1-wsl-and-ubuntu-setup)
- [Part 2: Docker Installation](#part-2-docker-installation)
- [Part 3: Application Setup](#part-3-application-setup)
- [Part 4: Running the Application](#part-4-running-the-application)
- [Part 5: Accessing from Windows](#part-5-accessing-from-windows)
- [Troubleshooting](#troubleshooting)
- [Windows Integration](#windows-integration)

## Prerequisites

- Windows 10 version 2004 or higher (Build 19041 or higher) or Windows 11
- Administrator access on Windows
- At least 4GB of free disk space
- Internet connection

## Part 1: WSL and Ubuntu Setup

### Step 1: Enable WSL on Windows

1. **Open PowerShell as Administrator**
   - Right-click on Start Menu
   - Select "Windows PowerShell (Admin)"

2. **Enable WSL and Virtual Machine Platform**
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

3. **Restart your computer**

4. **Set WSL 2 as default version**
   ```powershell
   wsl --set-default-version 2
   ```

### Step 2: Install Ubuntu from Microsoft Store

1. Open Microsoft Store
2. Search for "Ubuntu" or "Ubuntu 22.04 LTS"
3. Click "Install"
4. Once installed, click "Open" or search for "Ubuntu" in Start Menu

### Step 3: Initial Ubuntu Setup

1. **First launch will ask for username and password**
   - Choose a username (lowercase, no spaces)
   - Set a password (you'll need this for sudo commands)

2. **Update Ubuntu packages**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

## Part 2: Docker Installation

### Step 1: Install Docker Desktop for Windows

1. **Download Docker Desktop**
   - Visit: https://www.docker.com/products/docker-desktop/
   - Download Docker Desktop for Windows

2. **Install Docker Desktop**
   - Run the installer
   - Ensure "Use WSL 2 instead of Hyper-V" is selected
   - Click "Install"

3. **Configure Docker Desktop**
   - Start Docker Desktop
   - Go to Settings → Resources → WSL Integration
   - Enable integration with your Ubuntu distro
   - Click "Apply & Restart"

### Step 2: Verify Docker in Ubuntu

1. **Open Ubuntu terminal**

2. **Test Docker**
   ```bash
   docker --version
   docker-compose --version
   ```

   If these commands work, Docker is properly integrated with WSL!

### Alternative: Install Docker directly in WSL (if Docker Desktop doesn't work)

```bash
# Install Docker in Ubuntu
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect
exit
# Then reopen Ubuntu
```

## Part 3: Application Setup

### Step 1: Create Windows Directory Structure

1. **Open PowerShell** (regular, not admin)

2. **Create win directory**
   ```powershell
   mkdir C:\infoblox-tag-mapper
   cd C:\infoblox-tag-mapper
   ```

### Step 2: Access from Ubuntu WSL

1. **Open Ubuntu terminal**

2. **Navigate to Windows directory**
   ```bash
   cd /mnt/c/infoblox-tag-mapper
   ```

### Step 3: Download Application Files

1. **Clone or download the repository**
   ```bash
   # If you have git
   git clone <your-repository-url> .
   
   # OR download and extract files manually to C:\infoblox-tag-mapper
   ```

2. **Ensure you have these files:**
   ```bash
   ls -la
   # Should show:
   # - tag_mapping_web_app.py
   # - aws_infoblox_vpc_manager_complete.py
   # - requirements_web.txt
   # - Dockerfile
   # - docker-compose.yml
   # - docker-entrypoint.sh
   # - setup.sh
   # - templates/index.html
   ```

### Step 4: Prepare Configuration

1. **Create config.env file**
   ```bash
   nano config.env
   ```

2. **Add your InfoBlox configuration**
   ```ini
   # InfoBlox Configuration
   GRID_MASTER=your-infoblox-server.com
   NETWORK_VIEW=default
   INFOBLOX_USERNAME=your-username
   PASSWORD=your-password
   
   # CSV File Configuration
   CSV_FILE=vpc_data.csv
   
   # Container Detection Configuration
   PARENT_CONTAINER_PREFIXES=
   CONTAINER_HIERARCHY_MODE=strict
   ```

3. **Save and exit** (Ctrl+X, then Y, then Enter)

4. **Copy your VPC data CSV file**
   - From Windows: Copy your CSV file to `C:\infoblox-tag-mapper\vpc_data.csv`

### Step 5: Run Setup Script

1. **Make setup script executable**
   ```bash
   chmod +x setup.sh
   ```

2. **Run setup**
   ```bash
   ./setup.sh
   ```

3. **Setup script will:**
   - Check Docker installation ✓
   - Find available port (e.g., 5000) ✓
   - Create directories ✓
   - Build Docker image ✓
   - Create management scripts ✓
   - Ask if you want to start now → Type 'y'

## Part 4: Running the Application

### Starting the Application

```bash
./start.sh
```

You'll see:
```
Starting AWS to InfoBlox Tag Mapper...
Container started successfully!
Web interface available at: http://localhost:5000

To view logs: ./logs.sh
To stop: ./stop.sh
```

### Accessing the Web Interface

1. **Open Windows browser** (Chrome, Edge, Firefox)
2. **Navigate to:** `http://localhost:5000` (or the port shown)
3. **You should see the Tag Mapping interface!**

### Management Commands

All commands should be run from Ubuntu terminal in `/mnt/c/infoblox-tag-mapper`:

```bash
# Check status
./status.sh

# View logs
./logs.sh

# Stop application
./stop.sh

# Restart application
./restart.sh

# Access container shell
./shell.sh
```

## Part 5: Accessing from Windows

### File Access

Your files are accessible from both Windows and WSL:

- **From Windows:** `C:\infoblox-tag-mapper\`
- **From WSL:** `/mnt/c/infoblox-tag-mapper/`

### Useful File Locations

- **Tag mappings:** `C:\infoblox-tag-mapper\data\tag_mappings.json`
- **Reports:** `C:\infoblox-tag-mapper\reports\`
- **Logs:** `C:\infoblox-tag-mapper\logs\`
- **CSV files:** `C:\infoblox-tag-mapper\*.csv`

### Creating Windows Shortcuts

1. **Create Start Script for Windows** (optional)
   
   Create `start-tag-mapper.bat` in `C:\infoblox-tag-mapper\`:
   ```batch
   @echo off
   echo Starting AWS to InfoBlox Tag Mapper...
   wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./start.sh"
   pause
   ```

2. **Create Stop Script for Windows**
   
   Create `stop-tag-mapper.bat` in `C:\infoblox-tag-mapper\`:
   ```batch
   @echo off
   echo Stopping AWS to InfoBlox Tag Mapper...
   wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./stop.sh"
   pause
   ```

3. **Create Desktop Shortcut**
   - Right-click on Desktop → New → Shortcut
   - Location: `C:\infoblox-tag-mapper\start-tag-mapper.bat`
   - Name: "Start InfoBlox Tag Mapper"

## Troubleshooting

### Issue: "Cannot connect to Docker daemon"

**Solution:**
1. Ensure Docker Desktop is running
2. Check WSL integration in Docker Desktop settings
3. Restart Docker Desktop

### Issue: "Port 5000 already in use"

**Solution:**
The setup script automatically finds an available port. Check the output for the assigned port.

### Issue: "Permission denied" errors

**Solution:**
```bash
# Fix permissions
chmod +x *.sh
chmod +x docker-entrypoint.sh
```

### Issue: Can't access from Windows browser

**Solution:**
1. Check Windows Firewall
2. Ensure Docker Desktop is running
3. Try `http://127.0.0.1:5000` instead of `localhost`
4. Check if port is correct: `./status.sh`

### Issue: WSL2 memory usage is high

**Solution:**
Create `.wslconfig` in your Windows user directory:
```ini
[wsl2]
memory=4GB
processors=2
```

Then restart WSL:
```powershell
wsl --shutdown
```

## Windows Integration

### PowerShell Function (Optional)

Add to your PowerShell profile:

```powershell
# Open PowerShell profile
notepad $PROFILE

# Add these functions:
function Start-TagMapper {
    wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./start.sh"
}

function Stop-TagMapper {
    wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./stop.sh"
}

function Show-TagMapperLogs {
    wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./logs.sh"
}
```

Now you can use from PowerShell:
```powershell
Start-TagMapper
Stop-TagMapper
Show-TagMapperLogs
```

### Windows Terminal Integration

Add custom profile for quick access:

1. Open Windows Terminal Settings
2. Add new profile:
```json
{
    "name": "InfoBlox Tag Mapper",
    "commandline": "wsl.exe -d Ubuntu --cd /mnt/c/infoblox-tag-mapper",
    "icon": "🏷️",
    "startingDirectory": "//wsl$/Ubuntu/mnt/c/infoblox-tag-mapper"
}
```

## Best Practices

1. **Always run commands from WSL Ubuntu terminal**
2. **Keep Docker Desktop running** when using the application
3. **Edit files from Windows** using your favorite editor
4. **Access web interface from Windows browser**
5. **Store CSV files in Windows directory** for easy access

## Quick Reference Card

```bash
# Navigate to project (from Ubuntu)
cd /mnt/c/infoblox-tag-mapper

# Start application
./start.sh

# Check status and get URL
./status.sh

# View logs
./logs.sh

# Stop application
./stop.sh

# Access from Windows browser
http://localhost:5000
```

## Support

If you encounter issues:

1. Check Docker Desktop is running
2. Ensure WSL2 is properly installed
3. Verify all files are present
4. Check logs with `./logs.sh`
5. Try restarting Docker Desktop
6. Restart WSL with `wsl --shutdown` then reopen Ubuntu

---

**Note:** This application requires both Docker Desktop and WSL2 to be running. The web interface is accessible from Windows browsers while the application runs in the WSL2 Ubuntu environment.
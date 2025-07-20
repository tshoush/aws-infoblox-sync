# AWS-InfoBlox Integration for Windows 11 WSL2

## Quick Start

### Prerequisites
1. Windows 11 with WSL2 installed
2. Ubuntu installed in WSL2 (`wsl --install -d Ubuntu`)
3. Docker Desktop for Windows with WSL2 integration enabled

### Setup Instructions

#### Step 1: Run Windows Setup
Choose one of these methods:

**PowerShell (Recommended):**
```powershell
# Right-click and "Run with PowerShell"
.\windows-setup.ps1
```

**Command Prompt:**
```cmd
windows-setup.bat
```

#### Step 2: Copy Files to WSL2
1. Copy this entire folder to your WSL2 Ubuntu home directory
2. The easiest way is to open File Explorer and navigate to:
   ```
   \\wsl$\Ubuntu\home\[your-username]\
   ```
3. Create a folder called `marriot-infoblox` and copy all files there

#### Step 3: Configure Credentials
1. Copy `config.env.example` to `config.env`
2. Edit `config.env` and add your credentials:
   ```bash
   # In WSL2 Ubuntu
   cd ~/marriot-infoblox
   cp config.env.example config.env
   nano config.env  # or use your preferred editor
   ```

#### Step 4: Run Setup in WSL2
```bash
# In WSL2 Ubuntu
cd ~/marriot-infoblox
chmod +x *.sh
./setup.sh
```

### Usage

#### Using the Control Script

**From Windows (PowerShell):**
```powershell
# Start the application
.\web-control.ps1 start

# Check status
.\web-control.ps1 status

# Stop the application
.\web-control.ps1 stop

# Restart the application
.\web-control.ps1 restart
```

**From Windows (Command Prompt):**
```cmd
REM Start the application
web-control.bat start

REM Check status
web-control.bat status

REM Stop the application
web-control.bat stop
```

**From WSL2:**
```bash
# Start the application
./web-control.sh start

# Check status
./web-control.sh status

# Stop the application
./web-control.sh stop
```

The control scripts will:
- Automatically find an available port if the default (5000) is busy
- Show the URL to access the web interface
- Display container health status

#### Step 5: Run the Application
```bash
./run.sh
```

## Files Included

### Core Application Files
- `aws_infoblox_vpc_manager_enhanced.py` - Main application
- `requirements.txt` - Python dependencies
- `config.env.example` - Configuration template (rename to config.env)
- `vpc_data_sample.csv` - Sample VPC data file

### Docker Files
- `docker-compose.yml` - Docker container configuration
- `Dockerfile` - Container build instructions

### Setup Scripts
- `windows-setup.ps1` - PowerShell setup script for Windows
- `windows-setup.bat` - Batch setup script for Windows
- `setup.sh` - Setup script for WSL2 Ubuntu
- `run.sh` - Run the application
- `stop.sh` - Stop the container
- `logs.sh` - View container logs

### Terminal Test Files (Optional)
- `terminal_integration_summary.md` - Terminal test documentation
- `comprehensive_terminal_test.py` - Comprehensive terminal tests
- `interactive_terminal_test.py` - Interactive terminal tests
- `test_terminal_integration.py` - Integration tests
- Various other test files

### Documentation
- `WINDOWS_WSL2_TRANSFER_GUIDE.md` - Detailed transfer guide
- This README.md

## Important Notes

1. **Credentials**: Never commit config.env with real credentials to version control
2. **Docker Desktop**: Ensure WSL2 integration is enabled in Docker Desktop settings
3. **File Permissions**: The setup.sh script will set correct permissions automatically
4. **Data Files**: Replace vpc_data_sample.csv with your actual VPC data file

## Troubleshooting

### Docker not found in WSL2
1. Open Docker Desktop
2. Go to Settings > Resources > WSL Integration
3. Enable integration with your Ubuntu distribution
4. Restart Docker Desktop

### Permission Denied
```bash
chmod +x *.sh
```

### Container won't start
```bash
# Check Docker logs
docker logs infoblox-tag-mapper

# Check if port 5002 is in use
docker ps
```

### Can't access WSL2 from Windows
Ensure WSL2 is running:
```powershell
wsl --list --running
```

## Support

For issues or questions:
1. Check the logs: `./logs.sh`
2. Review `WINDOWS_WSL2_TRANSFER_GUIDE.md`
3. Ensure all prerequisites are installed correctly
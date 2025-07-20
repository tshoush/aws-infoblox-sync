# AWS to InfoBlox Tag Mapper - Windows Quick Start Guide

This guide provides a simplified setup process for Windows users using the provided batch files.

## Prerequisites

Before starting, ensure you have:
- Windows 10 (version 2004 or higher) or Windows 11
- Administrator access (for WSL installation)
- Docker Desktop for Windows installed
- At least 4GB free disk space

## Quick Setup (5 Minutes)

### Step 1: Install WSL and Ubuntu

1. **Open PowerShell as Administrator**
   - Right-click Start Menu → Windows PowerShell (Admin)

2. **Install WSL and Ubuntu** (if not already installed)
   ```powershell
   wsl --install
   ```
   - This installs WSL2 and Ubuntu automatically
   - Restart your computer when prompted

3. **Set up Ubuntu**
   - Open Ubuntu from Start Menu
   - Create a username and password when prompted

### Step 2: Install Docker Desktop

1. **Download Docker Desktop**
   - Visit: https://www.docker.com/products/docker-desktop/
   - Download and run the installer

2. **During installation:**
   - Select "Use WSL 2 instead of Hyper-V"
   - Complete the installation
   - Start Docker Desktop

3. **Configure Docker Desktop**
   - Go to Settings → Resources → WSL Integration
   - Enable integration with Ubuntu
   - Click Apply & Restart

### Step 3: Set Up the Application

1. **Extract application files** to `C:\infoblox-tag-mapper\`

2. **Run the Windows setup wizard:**
   - Navigate to `C:\infoblox-tag-mapper\win\`
   - Double-click `setup-tag-mapper.bat`
   - Follow the prompts

The setup wizard will:
- ✓ Check all prerequisites
- ✓ Create necessary directories
- ✓ Run the Docker setup
- ✓ Create management shortcuts

### Step 4: Configure InfoBlox Credentials

1. **Edit the configuration file:**
   - Open `C:\infoblox-tag-mapper\config.env` in Notepad
   - Add your InfoBlox details:
   ```ini
   GRID_MASTER=your-infoblox-server.com
   INFOBLOX_USERNAME=your-username
   PASSWORD=your-password
   ```
   - Save the file

2. **Add your CSV file:**
   - Copy your VPC data CSV to `C:\infoblox-tag-mapper\vpc_data.csv`

## Using the Application

### Starting the Application

1. **Double-click** `C:\infoblox-tag-mapper\start-tag-mapper.bat`
2. The script will:
   - Check if Docker is running (and start it if needed)
   - Start the web application
   - Display the port number (usually 5000)
   - Open your web browser automatically

### Stopping the Application

1. **Double-click** `C:\infoblox-tag-mapper\stop-tag-mapper.bat`

### Checking Status

1. **Double-click** `C:\infoblox-tag-mapper\status-tag-mapper.bat`
2. Shows if the application is running and the URL

### Viewing Logs

1. **Double-click** `C:\infoblox-tag-mapper\logs-tag-mapper.bat`
2. Press Ctrl+C to stop viewing logs

## Desktop Shortcuts (Optional)

Create shortcuts for easier access:

1. **Right-click** on `start-tag-mapper.bat`
2. Select **"Send to" → "Desktop (create shortcut)"**
3. Repeat for other .bat files as needed

## File Locations

- **Application files:** `C:\infoblox-tag-mapper\`
- **Tag mappings:** `C:\infoblox-tag-mapper\data\tag_mappings.json`
- **Reports:** `C:\infoblox-tag-mapper\reports\`
- **Logs:** `C:\infoblox-tag-mapper\logs\`

## Troubleshooting

### "Docker Desktop is not running"
- Start Docker Desktop from Start Menu
- Wait for it to fully start (system tray icon)
- Try again

### "WSL is not installed"
- Run PowerShell as Administrator
- Execute: `wsl --install`
- Restart computer

### "Port 5000 already in use"
- The setup automatically finds an available port
- Check the displayed port number when starting

### Cannot access web interface
- Ensure Docker Desktop is running
- Check Windows Firewall settings
- Try http://127.0.0.1:5000 instead of localhost

## Quick Commands Reference

All commands are available as .bat files in `C:\infoblox-tag-mapper\`:

| Action | File | Description |
|--------|------|-------------|
| Setup | `win\setup-tag-mapper.bat` | Initial setup wizard |
| Start | `start-tag-mapper.bat` | Start the application |
| Stop | `stop-tag-mapper.bat` | Stop the application |
| Status | `status-tag-mapper.bat` | Check if running |
| Logs | `logs-tag-mapper.bat` | View application logs |

## Tips

1. **Keep Docker Desktop running** when using the application
2. **Edit files normally** in Windows using any text editor
3. **Access the web interface** from any Windows browser
4. **CSV files** can be edited in Excel and saved in the application directory

## Next Steps

1. Start the application: Double-click `start-tag-mapper.bat`
2. Open your browser to the displayed URL
3. Configure your AWS tag mappings
4. Run the import process

---

For detailed setup instructions and advanced configuration, see `README_WSL_SETUP.md`
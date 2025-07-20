# Troubleshooting Guide - Blank Page Issue

If you're seeing a blank page when accessing the web interface, follow these steps:

## Quick Diagnosis

1. **Run the troubleshooting script:**
   ```bash
   # From Windows
   C:\infoblox-tag-mapper\win\troubleshoot-tag-mapper.bat
   
   # From WSL Ubuntu
   cd /mnt/c/infoblox-tag-mapper
   chmod +x troubleshoot.sh
   ./troubleshoot.sh
   ```

2. **Check these URLs in your browser:**
   - Health check: `http://localhost:5000/health`
   - Debug info: `http://localhost:5000/debug`
   - Alternative: `http://127.0.0.1:5000`

## Common Causes and Solutions

### 1. Templates Directory Missing

**Symptom:** Debug endpoint shows `templates_exists: false`

**Fix:**
```bash
# Stop the container
./stop.sh

# Rebuild with proper file structure
docker-compose build --no-cache

# Start again
./start.sh
```

### 2. Port Binding Issue

**Symptom:** Cannot reach any URL

**Fix:**
```bash
# Check what port is actually being used
docker-compose ps

# Check if port is already in use
netstat -an | findstr :5000

# Use a different port
WEB_PORT=8080 ./start.sh
```

### 3. Flask Static Files Issue

**Symptom:** Page loads but no content

**Fix:**
```bash
# Access the container
./shell.sh

# Inside container, check files
ls -la /app/templates/
cat /app/templates/index.html

# Exit container
exit

# If files are missing, copy them manually
docker cp templates/index.html $(docker-compose ps -q tag-mapper):/app/templates/
```

### 4. Browser Cache Issue

**Fix:**
- Press `Ctrl + F5` to hard refresh
- Open Developer Tools (F12) → Network tab → Disable cache
- Try an incognito/private window
- Try a different browser

## Step-by-Step Recovery

If nothing above works, do a complete reset:

```bash
# 1. Stop everything
./stop.sh

# 2. Remove the container and image
docker-compose down --rmi all

# 3. Clean up Docker
docker system prune -f

# 4. Ensure templates exist
cd /mnt/c/infoblox-tag-mapper
mkdir -p templates
# Make sure templates/index.html exists

# 5. Rebuild from scratch
docker-compose build --no-cache

# 6. Start fresh
./start.sh

# 7. Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/debug
```

## Manual Testing

Test if Flask is working at all:

```bash
# Access container shell
docker-compose exec tag-mapper /bin/bash

# Inside container
python -c "from tag_mapping_web_app import app; print(app.url_map)"

# Test Flask directly
python tag_mapping_web_app.py
```

## Windows-Specific Issues

### WSL2 Networking
Sometimes WSL2 has networking issues. Try:

```powershell
# In PowerShell as Admin
wsl --shutdown
# Wait 10 seconds
wsl

# Then restart Docker Desktop
```

### Firewall
Windows Defender Firewall might block the port:

1. Open Windows Defender Firewall
2. Click "Allow an app or feature"
3. Ensure Docker Desktop is allowed
4. Or temporarily disable firewall to test

### Docker Desktop Settings
1. Open Docker Desktop
2. Settings → Resources → WSL Integration
3. Ensure Ubuntu is enabled
4. Apply & Restart

## Getting Help

If you still see a blank page after trying everything:

1. Run `./logs.sh` and look for Python errors
2. Check `http://localhost:5000/debug` response
3. Share the output of the troubleshooting script

The debug endpoint should show:
- `templates_exists: true`
- `index_html_exists: true`
- `working_directory: /app`

If these are false, the templates aren't being copied correctly into the Docker container.
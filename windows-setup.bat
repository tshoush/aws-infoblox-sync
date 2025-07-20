@echo off
echo ================================================
echo AWS-InfoBlox Integration Setup for Windows WSL2
echo ================================================
echo.

REM Check if WSL is installed
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: WSL2 is not installed. Please install WSL2 first.
    echo Run: wsl --install
    exit /b 1
)

REM Check if Docker Desktop is running
docker version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not running. Please start Docker Desktop.
    exit /b 1
)

echo Prerequisites check passed.
echo.

REM Create project directory in WSL
echo Creating project directory in WSL...
wsl -d Ubuntu mkdir -p ~/marriot-infoblox

REM Copy necessary files to WSL
echo.
echo Copying project files to WSL...
echo Please ensure you have copied the following files to your Windows system first:

echo.
echo Required files from Mac:
echo 1. config.env (with your credentials)
echo 2. vpc_data.csv or vpc_data2.csv (your data files)
echo 3. modified_properties_file.csv (if using property import)
echo 4. Terminal test files (optional):
echo    - terminal_integration_summary.md
echo    - terminal_test_results.txt
echo    - terminal_test_detailed.json
echo    - comprehensive_terminal_test.py
echo    - interactive_terminal_test.py
echo    - test_terminal_integration.py
echo.

echo Copy command for WSL (run from Windows folder containing files):
echo wsl cp *.csv ~/marriot-infoblox/
echo wsl cp config.env ~/marriot-infoblox/
echo wsl cp terminal*.* ~/marriot-infoblox/
echo wsl cp *terminal*.py ~/marriot-infoblox/
echo.

pause

REM Create core Python files in WSL
echo Creating Python application files...

REM Create main manager script
wsl -d Ubuntu bash -c "cat > ~/marriot-infoblox/aws_infoblox_vpc_manager.py << 'EOF'
# Copy the content of aws_infoblox_vpc_manager_enhanced.py here
# This is a placeholder - actual content should be copied
EOF"

REM Create requirements.txt
wsl -d Ubuntu bash -c "cat > ~/marriot-infoblox/requirements.txt << 'EOF'
pandas>=1.3.0
requests>=2.25.0
urllib3>=1.26.0
python-dotenv>=0.19.0
EOF"

REM Create docker-compose.yml
wsl -d Ubuntu bash -c "cat > ~/marriot-infoblox/docker-compose.yml << 'EOF'
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
      - "5002:5002"
    command: tail -f /dev/null
    restart: unless-stopped
EOF"

REM Create Dockerfile
wsl -d Ubuntu bash -c "cat > ~/marriot-infoblox/Dockerfile << 'EOF'
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

CMD ["tail", "-f", "/dev/null"]
EOF"

REM Create setup script for WSL
wsl -d Ubuntu bash -c "cat > ~/marriot-infoblox/setup.sh << 'EOF'
#!/bin/bash
echo \"Setting up AWS-InfoBlox Integration...\"

# Create necessary directories
mkdir -p logs reports data

# Set permissions
chmod +x *.sh

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo \"Docker not found in WSL. Using Docker Desktop integration...\"
fi

# Build container
docker compose build

# Start container
docker compose up -d

echo \"Setup complete! Container is running.\"
echo \"To run the import: docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager.py\"
EOF"

wsl -d Ubuntu chmod +x ~/marriot-infoblox/setup.sh

echo.
echo ================================================
echo Setup script created in WSL!
echo.
echo Next steps:
echo 1. Copy your files to WSL Ubuntu:
echo    - From Windows: Copy files to \\wsl$\Ubuntu\home\{username}\marriot-infoblox
echo    - Or use the wsl cp commands shown above
echo.
echo 2. In WSL Ubuntu, navigate to the project:
echo    wsl -d Ubuntu
echo    cd ~/marriot-infoblox
echo.
echo 3. Run the setup:
echo    ./setup.sh
echo.
echo 4. Execute the import:
echo    docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager.py
echo ================================================
pause
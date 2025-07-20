@echo off
title AWS to InfoBlox Tag Mapper - Setup
color 0A
cls

echo ===============================================
echo     AWS to InfoBlox Tag Mapper
echo     Windows WSL Setup Wizard
echo ===============================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    color 0E
    echo WARNING: Not running as administrator.
    echo Some features may not work properly.
    echo.
)

REM Check if WSL is installed
echo Checking WSL installation...
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo ERROR: WSL is not installed.
    echo.
    echo Please install WSL first by running this in PowerShell as Admin:
    echo   wsl --install
    echo.
    echo Then install Ubuntu from Microsoft Store.
    echo.
    pause
    exit /b 1
)
echo WSL: OK

REM Check if Ubuntu is installed
echo Checking Ubuntu installation...
wsl -l -q | findstr /i "Ubuntu" >nul
if %errorlevel% neq 0 (
    color 0C
    echo ERROR: Ubuntu is not installed in WSL.
    echo.
    echo Please install Ubuntu from Microsoft Store.
    echo.
    pause
    exit /b 1
)
echo Ubuntu: OK

REM Check if Docker Desktop is installed
echo Checking Docker Desktop...
if exist "C:\Program Files\Docker\Docker\Docker Desktop.exe" (
    echo Docker Desktop: INSTALLED
    
    REM Check if Docker Desktop is running
    tasklist /FI "IMAGENAME eq Docker Desktop.exe" 2>NUL | find /I /N "Docker Desktop.exe">NUL
    if %errorlevel% neq 0 (
        color 0E
        echo Docker Desktop: NOT RUNNING
        echo.
        echo Starting Docker Desktop...
        start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
        echo Please wait for Docker Desktop to fully start (30 seconds)...
        timeout /t 30 /nobreak >nul
    ) else (
        echo Docker Desktop: RUNNING
    )
) else (
    color 0C
    echo ERROR: Docker Desktop is not installed.
    echo.
    echo Please download and install Docker Desktop from:
    echo https://www.docker.com/products/docker-desktop/
    echo.
    echo Make sure to enable WSL2 integration during installation.
    echo.
    pause
    exit /b 1
)

echo.
echo ===============================================
echo All prerequisites checked!
echo ===============================================
echo.

REM Create directory structure
echo Creating directory structure...
if not exist "C:\infoblox-tag-mapper" (
    mkdir C:\infoblox-tag-mapper
    echo Created: C:\infoblox-tag-mapper
) else (
    echo Directory already exists: C:\infoblox-tag-mapper
)

REM Check if files exist
echo.
echo Checking application files...
cd /d C:\infoblox-tag-mapper

set missing_files=0
if not exist "tag_mapping_web_app.py" (
    echo MISSING: tag_mapping_web_app.py
    set missing_files=1
)
if not exist "aws_infoblox_vpc_manager_complete.py" (
    echo MISSING: aws_infoblox_vpc_manager_complete.py
    set missing_files=1
)
if not exist "requirements_web.txt" (
    echo MISSING: requirements_web.txt
    set missing_files=1
)
if not exist "Dockerfile" (
    echo MISSING: Dockerfile
    set missing_files=1
)
if not exist "docker-compose.yml" (
    echo MISSING: docker-compose.yml
    set missing_files=1
)
if not exist "setup.sh" (
    echo MISSING: setup.sh
    set missing_files=1
)

if %missing_files% equ 1 (
    color 0E
    echo.
    echo WARNING: Some files are missing!
    echo Please copy all application files to C:\infoblox-tag-mapper\
    echo.
    pause
    exit /b 1
) else (
    echo All required files found!
)

REM Check for config.env
echo.
if not exist "config.env" (
    echo Creating config.env template...
    (
        echo # InfoBlox Configuration
        echo GRID_MASTER=
        echo NETWORK_VIEW=default
        echo INFOBLOX_USERNAME=
        echo PASSWORD=
        echo.
        echo # CSV File Configuration
        echo CSV_FILE=vpc_data.csv
        echo.
        echo # Container Detection Configuration
        echo PARENT_CONTAINER_PREFIXES=
        echo CONTAINER_HIERARCHY_MODE=strict
    ) > config.env
    echo.
    echo IMPORTANT: Please edit C:\infoblox-tag-mapper\config.env
    echo and add your InfoBlox credentials before running the application.
)

REM Copy Windows batch files
echo.
echo Copying Windows management scripts...
if not exist "start-tag-mapper.bat" (
    copy "%~dp0start-tag-mapper.bat" . >nul
)
if not exist "stop-tag-mapper.bat" (
    copy "%~dp0stop-tag-mapper.bat" . >nul
)
if not exist "status-tag-mapper.bat" (
    copy "%~dp0status-tag-mapper.bat" . >nul
)
if not exist "logs-tag-mapper.bat" (
    copy "%~dp0logs-tag-mapper.bat" . >nul
)

echo.
echo ===============================================
echo Running setup in WSL Ubuntu...
echo ===============================================
echo.

REM Run the setup script in WSL
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && chmod +x setup.sh && ./setup.sh"

if %errorlevel% equ 0 (
    echo.
    echo ===============================================
    echo Setup completed successfully!
    echo ===============================================
    echo.
    echo You can now use these commands from C:\infoblox-tag-mapper\:
    echo   - start-tag-mapper.bat    (Start the application)
    echo   - stop-tag-mapper.bat     (Stop the application)
    echo   - status-tag-mapper.bat   (Check status)
    echo   - logs-tag-mapper.bat     (View logs)
    echo.
    echo Or create desktop shortcuts to these files for easy access.
) else (
    color 0C
    echo.
    echo ERROR: Setup failed. Please check the error messages above.
)

echo.
pause
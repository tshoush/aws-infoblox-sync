@echo off
title AWS to InfoBlox Tag Mapper - Status
color 0B
cls

echo ===============================================
echo     AWS to InfoBlox Tag Mapper
echo     Checking Status...
echo ===============================================
echo.

REM Check if WSL is installed
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo ERROR: WSL is not installed or not available.
    echo.
    pause
    exit /b 1
)

REM Check if Docker Desktop is running
echo Checking Docker Desktop...
tasklist /FI "IMAGENAME eq Docker Desktop.exe" 2>NUL | find /I /N "Docker Desktop.exe">NUL
if %errorlevel% equ 0 (
    echo Docker Desktop: RUNNING
) else (
    color 0E
    echo Docker Desktop: NOT RUNNING
    echo Please start Docker Desktop first.
)

echo.
echo Checking application status...
echo.

REM Navigate to the correct directory and check status
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && if [ -f ./status.sh ]; then ./status.sh; else echo 'Error: status.sh not found.'; fi"

echo.
echo ===============================================
echo.
echo Press any key to open the web interface...
pause >nul
start http://localhost:5000
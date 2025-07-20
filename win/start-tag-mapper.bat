@echo off
title AWS to InfoBlox Tag Mapper - Start
color 0A
cls

echo ===============================================
echo     AWS to InfoBlox Tag Mapper
echo     Starting Web Interface...
echo ===============================================
echo.

REM Check if WSL is installed
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo ERROR: WSL is not installed or not available.
    echo Please install WSL and Ubuntu from Microsoft Store.
    echo.
    pause
    exit /b 1
)

REM Check if Docker Desktop is running
tasklist /FI "IMAGENAME eq Docker Desktop.exe" 2>NUL | find /I /N "Docker Desktop.exe">NUL
if %errorlevel% neq 0 (
    color 0E
    echo WARNING: Docker Desktop is not running.
    echo Starting Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    echo Waiting for Docker to start (30 seconds)...
    timeout /t 30 /nobreak >nul
)

echo Starting application in WSL Ubuntu...
echo.

REM Navigate to the correct directory and start the application
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && if [ -f ./start.sh ]; then ./start.sh; else echo 'Error: start.sh not found. Please run setup first.'; fi"

if %errorlevel% equ 0 (
    echo.
    echo ===============================================
    echo Application started successfully!
    echo.
    echo Opening web browser in 5 seconds...
    timeout /t 5 /nobreak >nul
    start http://localhost:5000
) else (
    color 0C
    echo.
    echo ERROR: Failed to start application.
    echo Please check if all files are in C:\infoblox-tag-mapper\
)

echo.
pause
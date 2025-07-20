@echo off
title AWS to InfoBlox Tag Mapper - Logs
color 0E
cls

echo ===============================================
echo     AWS to InfoBlox Tag Mapper
echo     Viewing Application Logs
echo ===============================================
echo.
echo Press Ctrl+C to stop viewing logs
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

REM Navigate to the correct directory and show logs
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && if [ -f ./logs.sh ]; then ./logs.sh; else echo 'Error: logs.sh not found.'; fi"

echo.
pause
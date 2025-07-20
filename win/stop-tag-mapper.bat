@echo off
title AWS to InfoBlox Tag Mapper - Stop
color 0C
cls

echo ===============================================
echo     AWS to InfoBlox Tag Mapper
echo     Stopping Web Interface...
echo ===============================================
echo.

REM Check if WSL is installed
wsl --status >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: WSL is not installed or not available.
    echo.
    pause
    exit /b 1
)

echo Stopping application...
echo.

REM Navigate to the correct directory and stop the application
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && if [ -f ./stop.sh ]; then ./stop.sh; else echo 'Error: stop.sh not found.'; fi"

if %errorlevel% equ 0 (
    color 0A
    echo.
    echo ===============================================
    echo Application stopped successfully!
    echo ===============================================
) else (
    echo.
    echo ERROR: Failed to stop application.
)

echo.
pause
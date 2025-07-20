@echo off
title AWS to InfoBlox Tag Mapper - Troubleshooting
color 0E
cls

echo ===============================================
echo     Tag Mapper Troubleshooting
echo ===============================================
echo.

REM Get the port from .env file
set /p WEB_PORT=<.env 2>nul
if "%WEB_PORT%"=="" set WEB_PORT=5000
for /f "tokens=2 delims==" %%a in ('findstr /i "WEB_PORT" .env 2^>nul') do set WEB_PORT=%%a

echo Application should be running on port: %WEB_PORT%
echo.

echo 1. Testing basic connectivity...
echo --------------------------------
curl -s http://localhost:%WEB_PORT%/health >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Can reach the application
    echo.
    echo Health check response:
    curl -s http://localhost:%WEB_PORT%/health 2>nul
    echo.
) else (
    echo [FAIL] Cannot reach http://localhost:%WEB_PORT%
    echo.
    echo Trying alternative addresses...
    curl -s http://127.0.0.1:%WEB_PORT%/health >nul 2>&1
    if %errorlevel% equ 0 (
        echo [OK] Can reach via http://127.0.0.1:%WEB_PORT%
    ) else (
        echo [FAIL] Cannot reach the application on any address
    )
)

echo.
echo 2. Debug information...
echo ----------------------
echo Fetching debug info from http://localhost:%WEB_PORT%/debug
curl -s http://localhost:%WEB_PORT%/debug 2>nul
echo.

echo.
echo 3. Quick fixes to try:
echo ---------------------
echo.
echo If you see a BLANK PAGE:
echo   1. First try: http://localhost:%WEB_PORT%/health
echo   2. Then try: http://localhost:%WEB_PORT%/debug
echo   3. Clear browser cache (Ctrl+F5)
echo   4. Try a different browser
echo.
echo If NOTHING WORKS:
echo   1. Run: wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && ./troubleshoot.sh"
echo   2. Restart the container: stop-tag-mapper.bat then start-tag-mapper.bat
echo   3. Rebuild: wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && docker-compose build"
echo.
echo Press any key to run the Linux troubleshooting script...
pause >nul

echo.
echo Running detailed diagnostics in WSL...
echo =====================================
wsl -d Ubuntu -- bash -c "cd /mnt/c/infoblox-tag-mapper && chmod +x troubleshoot.sh && ./troubleshoot.sh"

echo.
pause
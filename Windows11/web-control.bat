@echo off
setlocal enabledelayedexpansion

:: AWS to InfoBlox Tag Mapper - Windows Control Script
:: Usage: web-control.bat [start|stop|restart|status|help]

set "CONTAINER_NAME=infoblox-tag-mapper"
set "SERVICE_NAME=tag-mapper"
set "DEFAULT_PORT=5000"

if "%1"=="" goto :help
if /i "%1"=="start" goto :start
if /i "%1"=="stop" goto :stop
if /i "%1"=="restart" goto :restart
if /i "%1"=="status" goto :status
if /i "%1"=="help" goto :help

echo Unknown command: %1
goto :help

:start
echo Checking if container is already running...
docker ps -q -f name=%CONTAINER_NAME% 2>nul | findstr . >nul
if %errorlevel%==0 (
    echo Container is already running
    goto :status
)

echo Checking port availability...
set "PORT=%WEB_PORT%"
if "%PORT%"=="" set "PORT=%DEFAULT_PORT%"

netstat -an | findstr ":%PORT%" >nul 2>&1
if %errorlevel%==0 (
    echo Port %PORT% is already in use, finding a free port...
    set /a PORT=%PORT%+1
    :findport
    netstat -an | findstr ":%PORT%" >nul 2>&1
    if %errorlevel%==0 (
        set /a PORT=!PORT!+1
        if !PORT! GTR 5010 (
            echo No available ports found
            exit /b 1
        )
        goto :findport
    )
    echo Found available port: !PORT!
    set "PORT=!PORT!"
)

echo Building Docker image...
docker-compose build %SERVICE_NAME% >nul 2>&1

echo Starting container on port %PORT%...
set "WEB_PORT=%PORT%"
docker-compose up -d %SERVICE_NAME%

echo.
echo Container started successfully
echo Access the web interface at: http://localhost:%PORT%
goto :eof

:stop
echo Stopping container...
docker stop %CONTAINER_NAME% >nul 2>&1
docker rm %CONTAINER_NAME% >nul 2>&1
echo Container stopped
goto :eof

:restart
call :stop
call :start
goto :eof

:status
echo.
echo ===============================================================
echo        AWS to InfoBlox Tag Mapper - Status
echo ===============================================================
docker ps -q -f name=%CONTAINER_NAME% 2>nul | findstr . >nul
if %errorlevel%==0 (
    echo Status: Running
    for /f "tokens=2 delims=:" %%i in ('docker port %CONTAINER_NAME% 5000/tcp 2^>nul') do (
        echo Port: %%i
        echo URL: http://localhost:%%i
    )
    docker inspect --format="{{.State.Health.Status}}" %CONTAINER_NAME% 2>nul | findstr . >nul
    if %errorlevel%==0 (
        for /f %%i in ('docker inspect --format="{{.State.Health.Status}}" %CONTAINER_NAME% 2^>nul') do echo Health: %%i
    )
    echo.
    echo Container logs: docker logs -f %CONTAINER_NAME%
) else (
    echo Status: Stopped
)
echo ===============================================================
goto :eof

:help
echo AWS to InfoBlox Tag Mapper - Control Script
echo.
echo Usage: %~nx0 [command]
echo.
echo Commands:
echo   start    - Start the web application
echo   stop     - Stop the web application
echo   restart  - Restart the web application
echo   status   - Show application status
echo   help     - Show this help message
echo.
echo Environment variables:
echo   WEB_PORT - Preferred port (default: %DEFAULT_PORT%)
echo.
echo Examples:
echo   %~nx0 start
echo   set WEB_PORT=5001 ^& %~nx0 start
echo   %~nx0 status
goto :eof

endlocal
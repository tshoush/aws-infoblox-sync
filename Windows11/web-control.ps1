# AWS to InfoBlox Tag Mapper - PowerShell Control Script
# Usage: .\web-control.ps1 [start|stop|restart|status|help]

param(
    [Parameter(Position=0)]
    [ValidateSet('start', 'stop', 'restart', 'status', 'help')]
    [string]$Command = 'help'
)

$ContainerName = "infoblox-tag-mapper"
$ServiceName = "tag-mapper"
$DefaultPort = 5000

function Test-Port {
    param($Port)
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    try {
        $tcpClient.Connect("localhost", $Port)
        $tcpClient.Close()
        return $true
    } catch {
        return $false
    }
}

function Find-FreePort {
    param($StartPort = 5000)
    $port = $StartPort
    while ($port -le 5010) {
        if (-not (Test-Port $port)) {
            return $port
        }
        $port++
    }
    return $null
}

function Start-Container {
    # Check if already running
    $running = docker ps -q -f name=$ContainerName 2>$null
    if ($running) {
        Write-Host "Container is already running" -ForegroundColor Yellow
        Show-Status
        return
    }

    # Find available port
    $port = if ($env:WEB_PORT) { $env:WEB_PORT } else { $DefaultPort }
    
    Write-Host "Checking port availability..."
    if (Test-Port $port) {
        Write-Host "Port $port is already in use, finding a free port..." -ForegroundColor Yellow
        $port = Find-FreePort ($port + 1)
        if (-not $port) {
            Write-Host "No available ports found" -ForegroundColor Red
            exit 1
        }
        Write-Host "Found available port: $port" -ForegroundColor Green
    }

    Write-Host "Building Docker image..."
    docker-compose build $ServiceName 2>&1 | Out-Null

    Write-Host "Starting container on port $port..."
    $env:WEB_PORT = $port
    docker-compose up -d $ServiceName

    Write-Host "`nContainer started successfully" -ForegroundColor Green
    Write-Host "Access the web interface at: " -NoNewline
    Write-Host "http://localhost:$port" -ForegroundColor Cyan
}

function Stop-Container {
    Write-Host "Stopping container..."
    docker stop $ContainerName 2>&1 | Out-Null
    docker rm $ContainerName 2>&1 | Out-Null
    Write-Host "Container stopped" -ForegroundColor Green
}

function Restart-Container {
    Stop-Container
    Start-Container
}

function Show-Status {
    Write-Host "`n===============================================================" -ForegroundColor Blue
    Write-Host "       AWS to InfoBlox Tag Mapper - Status" -ForegroundColor Blue
    Write-Host "===============================================================" -ForegroundColor Blue
    
    $running = docker ps -q -f name=$ContainerName 2>$null
    if ($running) {
        Write-Host "Status: " -NoNewline
        Write-Host "Running" -ForegroundColor Green
        
        $portInfo = docker port $ContainerName 5000/tcp 2>$null
        if ($portInfo) {
            $port = $portInfo.Split(':')[1]
            Write-Host "Port: $port"
            Write-Host "URL: " -NoNewline
            Write-Host "http://localhost:$port" -ForegroundColor Cyan
        }
        
        $health = docker inspect --format='{{.State.Health.Status}}' $ContainerName 2>$null
        if ($health) {
            Write-Host "Health: $health"
        }
        
        Write-Host "`nContainer logs: docker logs -f $ContainerName" -ForegroundColor Gray
    } else {
        Write-Host "Status: " -NoNewline
        Write-Host "Stopped" -ForegroundColor Red
    }
    Write-Host "===============================================================" -ForegroundColor Blue
}

function Show-Help {
    Write-Host "AWS to InfoBlox Tag Mapper - Control Script" -ForegroundColor Cyan
    Write-Host "`nUsage: .\$($MyInvocation.MyCommand.Name) [command]"
    Write-Host "`nCommands:"
    Write-Host "  start    - Start the web application" -ForegroundColor Green
    Write-Host "  stop     - Stop the web application" -ForegroundColor Green
    Write-Host "  restart  - Restart the web application" -ForegroundColor Green
    Write-Host "  status   - Show application status" -ForegroundColor Green
    Write-Host "  help     - Show this help message" -ForegroundColor Green
    Write-Host "`nEnvironment variables:"
    Write-Host "  WEB_PORT - Preferred port (default: $DefaultPort)" -ForegroundColor Yellow
    Write-Host "`nExamples:"
    Write-Host "  .\$($MyInvocation.MyCommand.Name) start"
    Write-Host "  `$env:WEB_PORT=5001; .\$($MyInvocation.MyCommand.Name) start"
    Write-Host "  .\$($MyInvocation.MyCommand.Name) status"
}

# Execute command
switch ($Command) {
    'start'   { Start-Container }
    'stop'    { Stop-Container }
    'restart' { Restart-Container }
    'status'  { Show-Status }
    'help'    { Show-Help }
}
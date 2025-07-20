#!/bin/bash

# AWS to InfoBlox Tag Mapper - Control Script
# Usage: ./web-control.sh [start|stop|restart|status]

set -e

# Configuration
DEFAULT_PORT=5000
CONTAINER_NAME="infoblox-tag-mapper"
SERVICE_NAME="tag-mapper"
MAX_PORT=5010

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if a port is available
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        return 1  # Port is in use
    else
        return 0  # Port is available
    fi
}

# Function to find an available port
find_free_port() {
    local start_port=$1
    local port=$start_port
    
    while [ $port -le $MAX_PORT ]; do
        if check_port $port; then
            echo $port
            return 0
        fi
        port=$((port + 1))
    done
    
    return 1  # No free port found
}

# Function to get container status
get_status() {
    if docker ps -q -f name=$CONTAINER_NAME 2>/dev/null | grep -q .; then
        # Container is running
        local port=$(docker port $CONTAINER_NAME 2>/dev/null | grep '5000/tcp' | cut -d':' -f2)
        local health=$(docker inspect --format='{{.State.Health.Status}}' $CONTAINER_NAME 2>/dev/null || echo "unknown")
        echo "running:$port:$health"
    else
        echo "stopped"
    fi
}

# Function to stop container
stop_container() {
    local status=$(get_status)
    if [[ $status == "stopped" ]]; then
        echo -e "${YELLOW}Container is not running${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}Stopping container...${NC}"
    docker stop $CONTAINER_NAME >/dev/null 2>&1 || true
    docker rm $CONTAINER_NAME >/dev/null 2>&1 || true
    echo -e "${GREEN}✓ Container stopped${NC}"
}

# Function to start container
start_container() {
    local status=$(get_status)
    if [[ $status != "stopped" ]]; then
        echo -e "${YELLOW}Container is already running${NC}"
        show_status
        return 0
    fi
    
    # Check if docker-compose.yml exists
    if [ ! -f "docker-compose.yml" ]; then
        echo -e "${RED}Error: docker-compose.yml not found in current directory${NC}"
        exit 1
    fi
    
    # Find available port
    REQUESTED_PORT=${WEB_PORT:-$DEFAULT_PORT}
    echo -e "Checking port availability..."
    
    if check_port $REQUESTED_PORT; then
        WEB_PORT=$REQUESTED_PORT
        echo -e "${GREEN}✓ Port $WEB_PORT is available${NC}"
    else
        echo -e "${YELLOW}⚠ Port $REQUESTED_PORT is already in use${NC}"
        WEB_PORT=$(find_free_port $((REQUESTED_PORT + 1)))
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Found available port: $WEB_PORT${NC}"
        else
            echo -e "${RED}✗ No available ports found between $REQUESTED_PORT and $MAX_PORT${NC}"
            exit 1
        fi
    fi
    
    # Build and start container
    echo -e "\nBuilding Docker image..."
    docker-compose build $SERVICE_NAME >/dev/null 2>&1
    
    echo -e "Starting container on port $WEB_PORT..."
    export WEB_PORT
    docker-compose up -d $SERVICE_NAME >/dev/null 2>&1
    
    # Wait for container to be ready
    echo -n "Waiting for service to be ready"
    RETRY_COUNT=0
    while [ $RETRY_COUNT -lt 15 ]; do
        if docker ps --filter "name=$CONTAINER_NAME" -q 2>/dev/null | grep -q .; then
            echo ""
            echo -e "${GREEN}✓ Container started successfully${NC}"
            echo -e "\nAccess the web interface at: ${GREEN}http://localhost:$WEB_PORT${NC}"
            return 0
        fi
        echo -n "."
        sleep 1
        RETRY_COUNT=$((RETRY_COUNT + 1))
    done
    
    echo -e "\n${RED}✗ Container failed to start${NC}"
    echo -e "Check logs with: docker logs $CONTAINER_NAME"
    exit 1
}

# Function to restart container
restart_container() {
    echo -e "${BLUE}Restarting container...${NC}"
    stop_container
    echo ""
    start_container
}

# Function to show status
show_status() {
    local status_info=$(get_status)
    IFS=':' read -r status port health <<< "$status_info"
    
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}       AWS to InfoBlox Tag Mapper - Status${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [[ $status == "running" ]]; then
        echo -e "Status: ${GREEN}Running${NC}"
        echo -e "Port: ${GREEN}$port${NC}"
        echo -e "Health: ${health}"
        echo -e "URL: ${GREEN}http://localhost:$port${NC}"
        echo -e "\nContainer logs: ${YELLOW}docker logs -f $CONTAINER_NAME${NC}"
    else
        echo -e "Status: ${RED}Stopped${NC}"
    fi
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
}

# Function to show help
show_help() {
    echo -e "${BLUE}AWS to InfoBlox Tag Mapper - Control Script${NC}"
    echo -e "\nUsage: $0 [command]"
    echo -e "\nCommands:"
    echo -e "  ${GREEN}start${NC}    - Start the web application"
    echo -e "  ${GREEN}stop${NC}     - Stop the web application"
    echo -e "  ${GREEN}restart${NC}  - Restart the web application"
    echo -e "  ${GREEN}status${NC}   - Show application status"
    echo -e "  ${GREEN}help${NC}     - Show this help message"
    echo -e "\nEnvironment variables:"
    echo -e "  ${YELLOW}WEB_PORT${NC} - Preferred port (default: $DEFAULT_PORT)"
    echo -e "\nExamples:"
    echo -e "  $0 start"
    echo -e "  WEB_PORT=5001 $0 start"
    echo -e "  $0 status"
}

# Main script logic
case "${1:-help}" in
    start)
        start_container
        ;;
    stop)
        stop_container
        ;;
    restart)
        restart_container
        ;;
    status)
        show_status
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}"
        show_help
        exit 1
        ;;
esac
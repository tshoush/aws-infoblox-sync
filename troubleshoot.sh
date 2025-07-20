#!/bin/bash

# Troubleshooting script for AWS to InfoBlox Tag Mapper

echo "==================================="
echo "Tag Mapper Troubleshooting Script"
echo "==================================="
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if container is running
echo "1. Checking Docker container status..."
if docker-compose ps | grep -q "Up"; then
    echo -e "${GREEN}✓ Container is running${NC}"
    CONTAINER_NAME=$(docker-compose ps -q tag-mapper)
    echo "   Container ID: $CONTAINER_NAME"
else
    echo -e "${RED}✗ Container is not running${NC}"
    echo "   Run ./start.sh to start the container"
    exit 1
fi

# Get the port
source .env 2>/dev/null
PORT=${WEB_PORT:-5000}
echo ""
echo "2. Container port configuration: $PORT"

# Check if port is accessible
echo ""
echo "3. Testing port accessibility..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:$PORT/health | grep -q "200"; then
    echo -e "${GREEN}✓ Port $PORT is accessible${NC}"
else
    echo -e "${RED}✗ Cannot reach port $PORT${NC}"
    echo "   Checking alternative ports..."
    
    # Try common alternative URLs
    for url in "http://127.0.0.1:$PORT/health" "http://0.0.0.0:$PORT/health"; do
        if curl -s -o /dev/null -w "%{http_code}" $url | grep -q "200"; then
            echo -e "${GREEN}✓ Accessible at: $url${NC}"
            break
        fi
    done
fi

# Check health endpoint
echo ""
echo "4. Checking health endpoint..."
HEALTH_RESPONSE=$(curl -s http://localhost:$PORT/health 2>/dev/null)
if [ ! -z "$HEALTH_RESPONSE" ]; then
    echo -e "${GREEN}✓ Health endpoint responding:${NC}"
    echo "$HEALTH_RESPONSE" | python -m json.tool 2>/dev/null || echo "$HEALTH_RESPONSE"
else
    echo -e "${RED}✗ Health endpoint not responding${NC}"
fi

# Check debug endpoint
echo ""
echo "5. Checking debug information..."
DEBUG_RESPONSE=$(curl -s http://localhost:$PORT/debug 2>/dev/null)
if [ ! -z "$DEBUG_RESPONSE" ]; then
    echo -e "${GREEN}✓ Debug endpoint responding:${NC}"
    echo "$DEBUG_RESPONSE" | python -m json.tool 2>/dev/null || echo "$DEBUG_RESPONSE"
else
    echo -e "${RED}✗ Debug endpoint not responding${NC}"
fi

# Check container logs
echo ""
echo "6. Recent container logs:"
echo "------------------------"
docker-compose logs --tail=20 tag-mapper

# Check file system
echo ""
echo "7. Checking file system inside container..."
docker-compose exec tag-mapper ls -la /app/templates/ 2>/dev/null || echo "Cannot list templates directory"

# Check processes
echo ""
echo "8. Checking processes inside container..."
docker-compose exec tag-mapper ps aux | grep python || echo "No Python process found"

# Network diagnostics
echo ""
echo "9. Container network information..."
docker inspect $CONTAINER_NAME | grep -A 10 "NetworkSettings" | grep -E "IPAddress|Ports"

# Suggestions
echo ""
echo "==================================="
echo "Troubleshooting suggestions:"
echo "==================================="
echo ""
echo "If you see a blank page:"
echo "1. Try accessing: http://localhost:$PORT/health"
echo "2. Try accessing: http://localhost:$PORT/debug"
echo "3. Check if templates/index.html exists in the container"
echo "4. Restart the container: ./restart.sh"
echo "5. Rebuild the container: docker-compose build && ./start.sh"
echo ""
echo "If the port is not accessible:"
echo "1. Check Windows Firewall settings"
echo "2. Try http://127.0.0.1:$PORT instead of localhost"
echo "3. Ensure Docker Desktop is running"
echo "4. Check if another application is using port $PORT"
echo ""
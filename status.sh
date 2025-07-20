#!/bin/bash
source .env
echo "=== AWS to InfoBlox Tag Mapper Status ==="
echo ""
if docker-compose ps | grep -q "Up"; then
    echo "Status: RUNNING ✓"
    echo "Web interface: http://localhost:${WEB_PORT}"
    echo ""
    echo "Container details:"
    docker-compose ps
else
    echo "Status: STOPPED ✗"
fi
echo ""
echo "Data directory: $(pwd)/data"
echo "Logs directory: $(pwd)/logs"
echo "Reports directory: $(pwd)/reports"

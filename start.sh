#!/bin/bash
source .env
echo "Starting AWS to InfoBlox Tag Mapper..."
docker-compose up -d
echo ""
echo "Container started successfully!"
echo "Web interface available at: http://localhost:${WEB_PORT}"
echo ""
echo "To view logs: ./logs.sh"
echo "To stop: ./stop.sh"

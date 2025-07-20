#!/bin/bash
echo "Restarting AWS to InfoBlox Tag Mapper..."
docker-compose restart
source .env
echo "Container restarted."
echo "Web interface available at: http://localhost:${WEB_PORT}"

#!/bin/bash

# Check if config.env exists
if [ ! -f "config.env" ]; then
    echo "ERROR: config.env not found!"
    echo "Please create config.env from config.env.example and add your credentials"
    exit 1
fi

# Check if main script exists
if [ ! -f "aws_infoblox_vpc_manager_enhanced.py" ]; then
    echo "ERROR: aws_infoblox_vpc_manager_enhanced.py not found!"
    exit 1
fi

# Check if container is running
if ! docker ps | grep -q infoblox-tag-mapper; then
    echo "Container not running. Starting it..."
    docker compose up -d
    sleep 3
fi

echo "Running AWS-InfoBlox VPC Manager..."
echo "================================================"
docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager_enhanced.py
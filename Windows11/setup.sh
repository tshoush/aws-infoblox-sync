#!/bin/bash
echo "================================================"
echo "AWS-InfoBlox Integration Setup for WSL2 Ubuntu"
echo "================================================"
echo ""

# Create necessary directories
echo "Creating directories..."
mkdir -p logs reports data

# Check if config.env exists
if [ ! -f "config.env" ]; then
    echo "WARNING: config.env not found!"
    echo "Please copy config.env.example to config.env and update with your credentials"
    echo ""
fi

# Set permissions
chmod +x *.sh 2>/dev/null

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "ERROR: Docker not found in WSL."
    echo "Please ensure Docker Desktop WSL integration is enabled:"
    echo "  Docker Desktop > Settings > Resources > WSL Integration"
    exit 1
fi

# Build container
echo "Building Docker container..."
docker compose build

if [ $? -ne 0 ]; then
    echo "ERROR: Docker build failed"
    exit 1
fi

# Start container
echo "Starting container..."
docker compose up -d

# Wait for container to start
sleep 3

# Check if container is running
if docker ps | grep -q infoblox-tag-mapper; then
    echo ""
    echo "✓ Setup complete! Container is running."
    echo ""
    echo "Next steps:"
    echo "1. Copy your config.env file and update credentials"
    echo "2. Copy your vpc_data.csv file"
    echo "3. Run: ./run.sh"
    echo ""
else
    echo "ERROR: Container failed to start"
    echo "Check logs: docker logs infoblox-tag-mapper"
    exit 1
fi
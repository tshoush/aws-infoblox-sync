#!/bin/bash
set -e

# Docker entrypoint script for AWS to InfoBlox Tag Mapper

echo "Starting AWS to InfoBlox Tag Mapper..."

# Create necessary directories if they don't exist
mkdir -p /app/data /app/reports /app/logs

# Check if tag_mappings.json exists in the data directory
if [ ! -f "/app/data/tag_mappings.json" ] && [ -f "/app/tag_mappings.json" ]; then
    echo "Moving tag_mappings.json to data directory..."
    mv /app/tag_mappings.json /app/data/
fi

# Create symbolic link for tag_mappings.json if it doesn't exist
if [ -f "/app/data/tag_mappings.json" ] && [ ! -f "/app/tag_mappings.json" ]; then
    ln -s /app/data/tag_mappings.json /app/tag_mappings.json
fi

# Check if config.env exists
if [ ! -f "/app/config.env" ]; then
    echo "WARNING: config.env not found. The application may not connect to InfoBlox."
    echo "Please mount your config.env file to /app/config.env"
fi

# Set Flask environment
export FLASK_APP=tag_mapping_web_app.py
export FLASK_ENV=${FLASK_ENV:-production}

# Update the Flask app to bind to all interfaces and use the PORT env variable
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=${PORT:-5000}

# Execute the command
exec "$@"
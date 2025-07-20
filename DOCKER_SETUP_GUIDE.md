# Docker Setup Guide for AWS to InfoBlox Tag Mapper

This guide explains how to set up and run the AWS to InfoBlox Tag Mapper web interface using Docker.

## Prerequisites

- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)
- Your AWS VPC data in CSV format
- InfoBlox credentials (optional for initial setup)

## Quick Start

### 1. Run the Setup Script

The easiest way to get started is using the automated setup script:

```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Check for Docker and Docker Compose
- Find an available port (starting from 5000)
- Create necessary directories
- Build the Docker image
- Create management scripts
- Optionally start the container

### 2. Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Create necessary directories
mkdir -p data reports logs static

# Build the Docker image
docker-compose build

# Start the container
docker-compose up -d
```

## Port Configuration

The setup script automatically finds an available port. You can also specify a preferred port:

```bash
WEB_PORT=8080 ./setup.sh
```

The assigned port is saved in `.env` file and displayed after setup.

## Management Commands

After running setup.sh, you'll have these commands available:

### Start the Application
```bash
./start.sh
```
Starts the container in detached mode. The web interface URL will be displayed.

### Stop the Application
```bash
./stop.sh
```
Stops and removes the container (data is preserved).

### Restart the Application
```bash
./restart.sh
```
Restarts the container without losing data.

### View Logs
```bash
./logs.sh
```
Shows real-time logs from the container (Ctrl+C to exit).

### Check Status
```bash
./status.sh
```
Shows if the container is running and displays the web interface URL.

### Access Container Shell
```bash
./shell.sh
```
Opens a bash shell inside the running container for debugging.

## Directory Structure

```
.
├── data/               # Persistent data (tag_mappings.json)
├── reports/            # Generated reports
├── logs/               # Application logs
├── config.env          # InfoBlox configuration
├── vpc_data.csv        # Your AWS VPC data
└── docker-compose.yml  # Docker configuration
```

## Configuration

### InfoBlox Credentials

Edit `config.env` to add your InfoBlox credentials:

```bash
# InfoBlox Configuration
GRID_MASTER=your-infoblox-server.com
NETWORK_VIEW=default
INFOBLOX_USERNAME=your-username
PASSWORD=your-password

# CSV File Configuration
CSV_FILE=vpc_data.csv
```

### Tag Mappings

Tag mappings are stored in `data/tag_mappings.json` and persist between container restarts.

## Data Persistence

The following data persists between container restarts:
- Tag mappings (`data/tag_mappings.json`)
- Generated reports (`reports/`)
- Application logs (`logs/`)

## Updating the Application

To update the application:

```bash
# Stop the container
./stop.sh

# Pull latest changes
git pull

# Rebuild the image
docker-compose build

# Start the container
./start.sh
```

## Troubleshooting

### Port Already in Use

If the default port (5000) is in use, the setup script will automatically find an available port. You can also manually specify a port:

```bash
WEB_PORT=8080 docker-compose up -d
```

### Cannot Connect to InfoBlox

The web interface will work without InfoBlox connection, but you won't see available Extended Attributes. Ensure:
1. `config.env` has correct credentials
2. Your Docker container can reach the InfoBlox server
3. The InfoBlox API is accessible

### Container Won't Start

Check logs for errors:
```bash
docker-compose logs
```

### Permission Issues

Ensure the setup script has execute permissions:
```bash
chmod +x setup.sh
chmod +x *.sh
```

## Security Considerations

1. The `config.env` file contains sensitive credentials - keep it secure
2. Consider using Docker secrets for production deployments
3. The web interface runs on localhost by default - use a reverse proxy for external access
4. Ensure proper firewall rules if exposing the service

## Advanced Usage

### Custom Docker Network

The application creates its own bridge network (`infoblox-net`). To connect other containers:

```bash
docker network connect infoblox-net your-other-container
```

### Environment Variables

You can override settings using environment variables:

```bash
FLASK_ENV=development WEB_PORT=8080 docker-compose up
```

### Volume Mounts

Customize volume mounts in `docker-compose.yml` to map different directories or files.

## Uninstalling

To completely remove the application:

```bash
# Stop and remove container
./stop.sh

# Remove Docker image
docker rmi infoblox-tag-mapper

# Remove data (optional - this deletes your mappings!)
rm -rf data reports logs

# Remove scripts
rm -f start.sh stop.sh restart.sh logs.sh status.sh shell.sh
```
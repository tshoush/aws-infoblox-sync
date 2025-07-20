#!/bin/bash

# AWS to InfoBlox Tag Mapper - Docker Setup Script
# This script sets up and configures the Docker environment

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "═══════════════════════════════════════════════════════════════"
echo "    AWS to InfoBlox Tag Mapper - Docker Setup"
echo "═══════════════════════════════════════════════════════════════"
echo -e "${NC}"

# Function to print colored messages
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to find an available port
find_available_port() {
    local port=$1
    local max_port=$((port + 100))
    
    while [ $port -le $max_port ]; do
        if ! lsof -i:$port >/dev/null 2>&1 && ! netstat -tuln 2>/dev/null | grep -q ":$port "; then
            echo $port
            return
        fi
        ((port++))
    done
    
    # If no port found in range, return 0
    echo 0
}

# Check prerequisites
print_info "Checking prerequisites..."

if ! command_exists docker; then
    print_error "Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command_exists docker-compose && ! docker compose version >/dev/null 2>&1; then
    print_error "Docker Compose is not installed. Please install Docker Compose."
    echo "Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

print_success "Prerequisites check passed"

# Check if Docker daemon is running
if ! docker info >/dev/null 2>&1; then
    print_error "Docker daemon is not running. Please start Docker."
    exit 1
fi

# Create necessary directories
print_info "Creating necessary directories..."
mkdir -p data reports logs static
print_success "Directories created"

# Check for required files
print_info "Checking required files..."
required_files=("tag_mapping_web_app.py" "aws_infoblox_vpc_manager_complete.py" "requirements_web.txt")
missing_files=()

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -ne 0 ]; then
    print_error "Missing required files:"
    for file in "${missing_files[@]}"; do
        echo "  - $file"
    done
    exit 1
fi
print_success "All required files present"

# Check for config.env
if [ ! -f "config.env" ]; then
    print_warning "config.env not found. Creating template..."
    cat > config.env << 'EOF'
# InfoBlox Configuration
GRID_MASTER=
NETWORK_VIEW=default
INFOBLOX_USERNAME=
PASSWORD=

# CSV File Configuration
CSV_FILE=vpc_data.csv

# Container Detection Configuration
PARENT_CONTAINER_PREFIXES=
CONTAINER_HIERARCHY_MODE=strict
EOF
    print_warning "Please edit config.env with your InfoBlox credentials"
fi

# Check for CSV file
if [ ! -f "vpc_data.csv" ]; then
    print_warning "vpc_data.csv not found. Make sure to add your CSV file before running."
fi

# Port configuration
print_info "Configuring port..."
DEFAULT_PORT=5000
PREFERRED_PORT=${WEB_PORT:-$DEFAULT_PORT}

# Find available port
AVAILABLE_PORT=$(find_available_port $PREFERRED_PORT)

if [ "$AVAILABLE_PORT" -eq 0 ]; then
    print_error "No available ports found in range $PREFERRED_PORT-$((PREFERRED_PORT + 100))"
    exit 1
fi

if [ "$AVAILABLE_PORT" -ne "$PREFERRED_PORT" ]; then
    print_warning "Port $PREFERRED_PORT is not available. Using port $AVAILABLE_PORT instead."
fi

# Save port configuration
echo "WEB_PORT=$AVAILABLE_PORT" > .env
print_success "Web interface will run on port: $AVAILABLE_PORT"

# Create management scripts
print_info "Creating management scripts..."

# Create start script
cat > start.sh << 'EOF'
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
EOF
chmod +x start.sh

# Create stop script
cat > stop.sh << 'EOF'
#!/bin/bash
echo "Stopping AWS to InfoBlox Tag Mapper..."
docker-compose down
echo "Container stopped."
EOF
chmod +x stop.sh

# Create restart script
cat > restart.sh << 'EOF'
#!/bin/bash
echo "Restarting AWS to InfoBlox Tag Mapper..."
docker-compose restart
source .env
echo "Container restarted."
echo "Web interface available at: http://localhost:${WEB_PORT}"
EOF
chmod +x restart.sh

# Create logs script
cat > logs.sh << 'EOF'
#!/bin/bash
echo "Showing logs (press Ctrl+C to exit)..."
docker-compose logs -f
EOF
chmod +x logs.sh

# Create status script
cat > status.sh << 'EOF'
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
EOF
chmod +x status.sh

# Create shell access script
cat > shell.sh << 'EOF'
#!/bin/bash
echo "Accessing container shell..."
docker-compose exec tag-mapper /bin/bash
EOF
chmod +x shell.sh

print_success "Management scripts created"

# Build Docker image
print_info "Building Docker image..."
docker-compose build
print_success "Docker image built successfully"

# Display summary
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}    Setup Complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Web interface will be available on port: $AVAILABLE_PORT"
echo ""
echo "Available commands:"
echo "  ./start.sh   - Start the container"
echo "  ./stop.sh    - Stop the container"
echo "  ./restart.sh - Restart the container"
echo "  ./logs.sh    - View container logs"
echo "  ./status.sh  - Check container status"
echo "  ./shell.sh   - Access container shell"
echo ""
echo "Next steps:"
echo "  1. Edit config.env with your InfoBlox credentials (if not done)"
echo "  2. Ensure your CSV file (vpc_data.csv) is in place"
echo "  3. Run ./start.sh to start the application"
echo ""

# Ask if user wants to start now
read -p "Would you like to start the container now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    ./start.sh
fi
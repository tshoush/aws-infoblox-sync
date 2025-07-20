FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements_web.txt .
RUN pip install --no-cache-dir -r requirements_web.txt

# Copy application files
COPY tag_mapping_web_app.py .
COPY aws_infoblox_vpc_manager_complete.py .

# Create directories
RUN mkdir -p templates static static/presentations

# Copy templates
COPY templates/ templates/

# Create directories for data persistence
RUN mkdir -p /app/data /app/reports /app/logs

# Copy entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose port (will be mapped dynamically)
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=tag_mapping_web_app.py
ENV PYTHONUNBUFFERED=1

# Volume for persistent data
VOLUME ["/app/data"]

# Use entrypoint script
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "tag_mapping_web_app.py"]
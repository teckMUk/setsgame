# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MONGODB_HOST=mongodb \
    MONGODB_PORT=27017

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements files
COPY requirements.txt requirements_dev.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create .version file if it doesn't exist (required by setup.py)
RUN echo "1.0.0" > .version

# Install the package
RUN pip install -e .

# Expose port (if needed for future web interface)
EXPOSE 8000

# Default command - run the game
CMD ["python", "setsgame.py"]

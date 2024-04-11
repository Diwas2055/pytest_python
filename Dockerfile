# Stage 1: Build Stage
FROM python:3.9 as builder

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Stage 2: Production Stage
FROM python:3.9-slim as production

# Set working directory
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app /app

# Set environment variables
ENV ENVIRONMENT=production
ENV PYTHONUNBUFFERED=1

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install production dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the FastAPI application in production
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2", "--proxy-headers"]

# Stage 3: Cleanup Stage
FROM scratch
COPY --from=production / /

# Set a non-root user for improved security
USER 1001

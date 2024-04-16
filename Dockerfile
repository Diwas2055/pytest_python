# Stage 1: Build Stage
FROM python:3.11 as base

# Set environment variables
ENV ENVIRONMENT=production

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app/

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY /src/ .

# Stage 2: Production Stage
FROM python:3.11-slim as production

# Set working directory
WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=base /app /app
COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base /usr/local/bin /usr/local/bin


# Expose the port for FastAPI
EXPOSE 8001

# # Command to run the FastAPI application in production
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "2", "--proxy-headers"]

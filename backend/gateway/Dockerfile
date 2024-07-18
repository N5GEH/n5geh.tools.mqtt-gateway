# Install from the official python image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install required packages, including PostgreSQL client
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY ./backend/gateway/requirements.txt ./

# Copy settings.py
COPY settings.py ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY ./backend/gateway/. ./

# Run the gateway
CMD ["python", "gateway.py"]

# Install from the official python image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Create directories for logs
RUN mkdir /var/log/supervisord /var/log/api /var/log/gateway

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY . ./

# Expose application on port 8000
EXPOSE 8000

# Install supervisord
RUN apt-get update && apt-get install -y supervisor

# Copy supervisord.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run the app with supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
# Install from the official python image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY ./backend/requirements.txt ./

# Copy settings.py
COPY settings.py ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY ./backend/gateway/. ./

# Run the gateway
CMD ["python", "gateway.py"]

# Install from the official python image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY ./backend/api/requirements.txt ./

# Copy settings.py
COPY settings.py ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY ./backend/api/. ./

# Expose application on port 8000
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

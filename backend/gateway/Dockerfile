# Install from the official python image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt
RUN pip uninstall -y pydantic
RUN pip install pydantic[dotenv]==1.7.2

# Copy source code
COPY . ./

# Run the gateway
CMD ["python", "gateway.py"]

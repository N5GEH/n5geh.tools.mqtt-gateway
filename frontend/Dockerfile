# Dockerfile for the frontend application
# Build the image with: docker build -t gateway-frontend .
# Run the container with: docker run -d -p 5173:5173 gateway-frontend

# Single stage
FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./
COPY . ./

# Initialization
RUN npm ci
RUN npm install -g vite

# Debug
# CMD ["sh", "-c", "while true; do sleep 3600; done"]

# Runner script here
RUN chmod +x ./runner.sh
CMD ["./runner.sh"]

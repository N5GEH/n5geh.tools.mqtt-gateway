# Dockerfile for the frontend application
# Build the image with: docker build -t gateway-frontend .
# Run the container with: docker run -d -p 5173:5173 gateway-frontend

# build stage
FROM node:lts-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . ./

# Build the application
RUN npm run build

# production stage
FROM node:lts-alpine AS production

# Set working directory
WORKDIR /app

# Install vite globally
RUN npm install -g vite

# Copy the built application
COPY --from=build /app/dist ./dist

# Expose application on port 5173
EXPOSE 5173

# Run the app with serve (-s flag is to serve the static files from the dist directory, -l is to set the port, and dist is the directory to serve)
#CMD ["serve", "-s", "-l", "5173", "dist"]

# Run the app with vite (to enable hot module reloading)
CMD ["vite", "preview", "--port", "5173", "--host"]
# Dockerfile for the frontend application
# Build the image with: docker build -t frontend .
# Run the container with: docker run -d -p 5173:5173 frontend

# Stage 1 - the build process
FROM node:lts-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the main application
COPY . ./

# Build the application
RUN npm run build

# Stage 2 - the production environment
FROM node:lts-alpine AS production

# Set working directory
WORKDIR /app

# Install 'serve' to run your application
RUN npm install -g serve

# Copy build folder from builder stage
COPY --from=build /app/dist ./dist

# Expose application on port 5173
EXPOSE 5173

# Run the app
CMD ["serve", "-s", "-l", "5173", "dist"]

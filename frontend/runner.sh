#!/bin/sh
# npm ci
# Build the application
npm run build
# Install vite globally
# npm install -g vite
# Run the app with vite (to enable hot module reloading)
vite preview --port 5173 --host
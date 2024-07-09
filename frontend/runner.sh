#!/bin/sh
# npm ci
# Build the application
npm run build
# Install vite globally
# npm install -g vite
# Run the app with vite (to enable hot module reloading)

# Check if the environment variables are set
if [ -z "$CERT_KEY_PATH" ] || [ -z "$CERT_CERT_PATH" ]; then
  echo "Error: CERT_KEY_PATH and CERT_CERT_PATH environment variables must be set."
  exit 1
fi

# Print paths for debugging purposes
echo "Using certificate key: $CERT_KEY_PATH"
echo "Using certificate cert: $CERT_CERT_PATH"

# Run the app with vite, ensuring it uses the environment variables for the certificate paths
vite --port 5173 --host

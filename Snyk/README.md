# Snyk Container Image Scanning

## Overview

This repository contains a script to scan all active Docker images for vulnerabilities using Snyk. The results of the scan are stored in individual Markdown files within the `scan_results` directory.

## Prerequisites

- Ensure Docker is installed and running on your system.

- Ensure Snyk CLI is installed. You can install it using npm:
  ```commandline
  npm install -g snyk 
  ```

- Authenticate Snyk CLI using your Snyk API token:
  ```commandline
  snyk auth YOUR_SNYK_API_TOKEN
  ```

## Running the script

- Clone the repository (if you haven't already):
    ```commandline
    git clone https://github.com/N5GEH/n5geh.tools.mqtt-gateway.git
    cd n5geh.tools.mqtt-gateway/
    ```
- The repository contains a `docker-compose.yml` file that can be used to start building the image and then start the gateway services.
    The gateway can be started with the following command:

    ```commandline
    cd fiware-environment
    docker compose pull
    docker compose up -d

    cd..

    cd n5geh.tools.mqtt-gateway/
    docker compose build
    docker compose up -d
    ```

- Navigate to the Snyk directory:
    ```commandline
    cd Snyk
    ```
- Set permissions and run the script:
    ```commandline
    chmod +x scan.sh
    ./scan.sh
    ```
- The script will create a scan_results directory and store the results of the scans for each active Docker image in separate Markdown files.
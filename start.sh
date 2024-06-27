#!/bin/bash

# Start the Fiware Environment
cd fiware-environment
docker compose pull
docker compose up -d

# Start the containers
cd ..
docker compose build
docker compose up -d
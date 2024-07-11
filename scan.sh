#!/bin/bash

# List of images to scan
images=(
    "n5gehtoolsmqtt-gateway-api:latest"
    "n5gehtoolsmqtt-gateway1-api:latest"
    "n5gehtoolsmqtt-gateway-frontend:latest"
    "n5gehtoolsmqtt-gateway1-frontend:latest"
    "n5gehtoolsmqtt-gateway-gateway:latest"
    "n5gehtoolsmqtt-gateway1-gateway:latest"
    "fiware/orion:latest"
    "redis:7.0"
    "mongo-express:1.0.2-20"
    "mongo:4.4"
    "mongo:5.0.24"
    "portainer/portainer-ce:2.19.4"
    "eclipse-mosquitto:2.0.15"
    "eclipse-mosquitto:2.0.14"
    "postgres:15.2"
    "dpage/pgadmin4:7.1"
    "telefonicaiot/fiware-orion:3.8.1"
    "fiware/iotagent-json:1.26.0"
    "grafana/grafana:9.3.0"
    "fiware/orion:3.7.0"
    "orchestracities/quantumleap:0.8.3"
    "crate/crate:4.6.6"
)

# Scan each image
for image in "${images[@]}"
do
    echo "Scanning $image..."
    snyk container test $image
done
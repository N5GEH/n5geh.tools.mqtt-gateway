# MQTT Gateway

## Overview
This is a universal MQTT gateway for the NGSI-V2 Context Broker, e.g. FIWARE-Orion. It supports any MQTT-based data ingress, using JSON as payload format. Data points can be simply registed using jsonpath and MQTT-topic.
It acts as a software-based IoT Gateway that helps manage heterogeneous field devices. The gateway is implemented in Python and uses the [FastAPI](https://fastapi.tiangolo.com/) framework for a RESTful-API. A web-UI is also provided based on [Svelte](https://svelte.dev/).


## Quickstart
Clone the repository to your local environment.
```bash
git clone https://github.com/N5GEH/n5geh.tools.mqtt-gateway.git
cd n5geh.tools.mqtt-gateway/
```


### Requirement
The MQTT gateway acts as a southbound interface of the NGSI-V2 context broker.
Its operation requires an MVP FIWARE platform with at least two components:
- NGSI-V2 Context Broker (and its database)
- MQTT Broker

If you are new to the FIWARE platform, it is highly recommended to start with the [platform tutorials](https://github.com/N5GEH/n5geh.platform).
Otherwise, a `docker-compose.yml` is also provided in this repo.
Set up this MVP FIWARE platform with:
```bash
cd fiware-environment
docker compose pull
docker compose up -d
```
Please only use this platform setup for testing purposes.

### Deployment
Before deploying the gateway via docker containers, the environment variables need to be configured in `.env` in the root directory.
This can be created from the provided `env.EXAMPLE`.
The default values can be directly used for the test deployment.
Check [here](https://github.com/N5GEH/n5geh.tools.mqtt-gateway#environment-variables) for more information about the environment variables. 

There are two methods to deploy the gateway:
- [Pull images from GitHub Container Registry](https://github.com/N5GEH/n5geh.tools.mqtt-gateway#pull-docker-images)
- [Building your local images](https://github.com/N5GEH/n5geh.tools.mqtt-gateway#build-your-own-docker-images).

#### Pull docker images
The recommended way to deploy the MQTT gateway is to use the pre-built docker images. Under the packages of this repository, you can find the images for the `gateway`, `frontend`, and `API`. In oder to pull these images, you need to first sign in to the `ghcr.io` (GitHub Container Registry).
````commandline
cd n5geh.tools.mqtt-gateway/
export CR_PAT=YOUR_TOKEN
echo $CR_PAT | docker login ghcr.io -u YOUR_USERNAME --password-stdin
````
`YOUR_TOKEN` (classic [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)) and `USERNAME` must be replaced with yours. Check [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classic) for more information.

After the login, you should be able to pull the images and start the gateway services.
````commandline
docker compose -f docker-compose.ghcr.yml pull
docker compose -f docker-compose.ghcr.yml up -d
````


#### Build your own docker images
The repository contains a `docker-compose.yml` file that can be used to start building the image and then start the gateway services.
The gateway can be started with the following command:
```commandline
cd n5geh.tools.mqtt-gateway/
docker compose build
docker compose up -d
```

### API interaction
After deploying the gateway, you can access a swagger API specification under the end point `/docs`.
For example, if the gateway is deployed locally, then you can access the swagger ui through [localhost:8000/docs](http://localhost:8000/docs)

### Environment variables
The gateway can be configured with the following environment variables:
- `ORION_URL` - the URL of the Orion Context Broker
- `MQTT_HOST` - the hostname of the MQTT broker
- `MQTT_PORT` - the port of the MQTT broker
- `POSTGRES_HOST` - the hostname of the PostgreSQL database
- `POSTGRES_USER` - the username for the PostgreSQL database
- `POSTGRES_PASSWORD` - the password for the PostgreSQL database
- `POSTGRES_DB` - the name of the PostgreSQL database
- `REDIS_URL` - the URL of the Redis database (used for caching)
- `FIWARE_SERVICE` - the FIWARE service name
- `FIWARE_SERVICEPATH` - the FIWARE service path
- `VITE_API_URL` - the URL to access the Gateway API from the client side (i.e., from your browser)

## Preview
### Web UI
![Frontend](frontend/preview/preview_v0.2.png)

### Singel Gateway Instance
#### Latency
![Latency](load-tests/results/gateway1x_latency.png "Latency")

#### Message loss
![Message loss](load-tests/results/gateway1x_message_loss_bar.png "Message loss")

### Four Gateway Instance
#### Latency
![Latency](load-tests/results/gateway4x_latency.png "Latency")

#### Message loss
![Message loss](load-tests/results/gateway4x_message_loss_bar.png "Message loss")

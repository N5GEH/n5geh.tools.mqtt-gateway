#!/bin/bash

# Stop all running docker containers and remove them for safer start
docker stop $(docker ps -q)
docker rm $(docker ps -q -a)
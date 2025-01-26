#!/usr/bin/env bash

docker build -t bridge-client .
docker run -d --name bridge-client --network="host" bridge-client

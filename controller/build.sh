#!/usr/bin/env bash

docker build -t centralized-mqtt-broker .
docker run -d --name centralized-mqtt-broker -p 1884:1883 centralized-mqtt-broker

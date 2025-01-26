#!/usr/bin/env bash
docker build -t local-mqtt-broker .
docker run -d --name local-mqtt-broker -p 1883:1883 local-mqtt-broker
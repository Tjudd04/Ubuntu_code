#!/bin/bash

# Builds the Dockerfile
sudo DOCKER_BUILDKIT=1 docker build -t dohtest:latest .

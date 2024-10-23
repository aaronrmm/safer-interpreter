#!/bin/bash

docker build -t ollama_test_app . && \
docker run --rm \
    -v "$PWD/app:/app" \
    -w /app \
    --network="bridge" \
    ollama_test_app

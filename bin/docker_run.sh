#!/bin/bash

# build container
docker build -t nodejs_python_scrape .

cd ../

# run interactive terminal with mounted project
docker run -it --mount type=bind,source="$(pwd)", \
target=/app \
nodejs_python_scrape:latest \
bash
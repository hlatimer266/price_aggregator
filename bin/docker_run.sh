#!/bin/bash

cd price_agg_frontend/

# run interactive terminal with mounted project
docker run -e AWSAccessKey=${AWSAccessKey} \
           -e AWSSecretKey=${AWSSecretKey} \
           -p 64333:3000 \
           -d nodejs_cs361:latest
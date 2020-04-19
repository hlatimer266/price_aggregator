# build container
docker build -t nodejs_python_scrape .

# run interactive terminal with mounted project
docker run -it --mount type=bind,source="$(pwd)", \
target=/app \
nodejs_python_scrape:latest \
bash
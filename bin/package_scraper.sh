#!/bin/bash
APP_HOME=$(pwd)

pushd python_lambdas
    rm -rf scrape_monitors.zip
    rm -rf scrape_laptops.zip
popd

pushd venv/lib/python3.7/site-packages
    # zip -r9 ${APP_HOME}/scrape_monitors.zip ./bs4 \
    # ./soupsieve \
    # ./requests \
    # ./certifi \
    # ./chardet \
    # ./idna \
    # ./urllib3

    zip -r ${APP_HOME}/scrape_laptops.zip ./bs4 \
    ./soupsieve \
    ./requests \
    ./certifi \
    ./chardet \
    ./idna \
    ./urllib3

popd

mv scrape_laptops.zip python_lambdas

pushd python_lambdas
    # zip -r scrape_monitors.zip price_scraper_lambda_mn.py
    zip -r scrape_laptops.zip price_scraper_lambda_laptops.py
popd
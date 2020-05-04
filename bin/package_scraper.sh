#!/bin/bash
APP_HOME=$(pwd)

pushd python_lambdas
    rm -rf scrape_monitors.zip
    rm -rf scrape_phones.zip
popd

pushd venv/lib/python3.7/site-packages
    zip -r ${APP_HOME}/scrape_monitors.zip ./bs4 \
    ./soupsieve \
    ./requests \
    ./certifi \
    ./chardet \
    ./idna \
    ./urllib3

    zip -r ${APP_HOME}/scrape_phones.zip ./bs4 \
    ./soupsieve \
    ./requests \
    ./certifi \
    ./chardet \
    ./idna \
    ./urllib3

popd

mv scrape_phones.zip scrape_monitors.zip python_lambdas

pushd python_lambdas
    zip -r scrape_monitors.zip price_scraper_lambda_mn.py
    zip -r scrape_phones.zip price_scraper_lambda_phones.py
popd
#!/bin/bash
APP_HOME=$(pwd)

pushd venv/lib/python3.7/site-packages
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./bs4
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./soupsieve
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./requests
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./certifi
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./chardet
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./idna
    zip -r9 ${APP_HOME}/scrape_monitors.zip ./urllib3
popd

zip -r scrape_monitors.zip price_scraper_lambda_mn.py
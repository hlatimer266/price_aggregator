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

<<<<<<< HEAD
popd

mv scrape_phones.zip scrape_monitors.zip python_lambdas
=======
    zip -r ${APP_HOME}/scrape_tvs.zip ./bs4 \
    ./soupsieve \
    ./requests \
    ./certifi \
    ./chardet \
    ./idna \
    ./urllib3

popd

mv scrape_phones.zip scrape_monitors.zip scrape_tvs.zip python_lambdas
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00

pushd python_lambdas
    zip -r scrape_monitors.zip price_scraper_lambda_mn.py
    zip -r scrape_phones.zip price_scraper_lambda_phones.py
<<<<<<< HEAD
=======
    zip -r scrape_tvs.zip price_scraper_lambda_tvs.py
>>>>>>> fbd997fe7313ea166d5a5e224e6a5efb17e26a00
popd
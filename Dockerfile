FROM python:3

ADD price_scraper.py /

RUN pip install bs4
RUN pip install requests

CMD [ "python", "./price_scraper.py" ]
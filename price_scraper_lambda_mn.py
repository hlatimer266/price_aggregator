import requests
from bs4 import BeautifulSoup
import time
import json


def lambda_handler(event, context):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(event['url'], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    if event['vendor'] == "walmart":
        price = soup.find(class_=event['html_tag'])
        try:
            print(price['content'])
        except Exception as e:
            print(e)
            print("in exception block")
            time.sleep(20)
            response = requests.get(event['url'], headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
            price = soup.find(class_=event['html_tag'])
            print(price['content'])

    elif event['vendor'] == "office_depot":
        price = soup.find(class_=event['html_tag'])
        print(price.span.get_text().strip())
    elif event['vendor'] == "monoprice":
        price = soup.find(class_=event['html_tag'])
        print(price.get_text().strip())
    elif event['vendor'] == "ebay":
        price = soup.find(class_=event['html_tag'])
        print(price.get_text().strip())
    elif event['vendor'] == "bh":
        price = soup.find(class_=event['html_tag'])
        try:
            print(price.get_text().strip())
        except Exception as e:
            print("in exception block")
            time.sleep(20)
            response = requests.get(event['url'], headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find(class_=event['html_tag'])
            print(price.get_text().strip())
    elif event['vendor'] == "cdw":
        price = soup.find(class_=event['html_tag'])
        print(price['content'])

    






import requests
from bs4 import BeautifulSoup
import time
import json


def lambda_handler(event, context):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'From' : 'latimerh@oregonstate.edu'}
    response = requests.get(event['url'], headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    if event['vendor'] == "walmart":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price['content']
    elif event['vendor'] == "office_depot":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price.span.get_text().strip()
    elif event['vendor'] == "monoprice":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price.get_text().strip()
    elif event['vendor'] == "ebay":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price.get_text().strip()
    elif event['vendor'] == "bh":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price.get_text().strip()
    elif event['vendor'] == "cdw":
        price = soup.find(class_=event['html_tag'])
        formatted_price = price['content']
        
    if formatted_price is None:
        return {
            'statusCode' : 400,
            'body' : 'url returned no results - ' + json.dumps(str(event['url']))
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(str(formatted_price))
        }
import requests
from bs4 import BeautifulSoup 
import time
import re
import json

def lambda_handler(event,context): 

    results_obj = {"results": []}

    for reqs in event['request']: 

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'From': 'mercadoa@oregonstate.edu'}
        try:
            response = requests.get(reqs['url'], headers=headers, verify=False, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
        except:
            print("request timed out for " + reqs['url'])
        if reqs['vendor'] == "walmart":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "newegg":
            data = soup.find_all(type=reqs['html_tag'])
            try:
                json_data=json.loads(data[2].contents[0])
                dictionary_data = json_data.get("offers")
                formatted_price = dictionary_data.get('price')
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "shopdevicesnow":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "ebay":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "bhphotovideo":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        
        results_obj['results'].append({'vendor': str(reqs['vendor']), 'price': str(formatted_price)})
        
 
    return {
        'statusCode': 200,
        'body': json.dumps(results_obj)
    }

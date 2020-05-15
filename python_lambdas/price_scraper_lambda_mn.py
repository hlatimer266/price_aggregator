import requests
from bs4 import BeautifulSoup
import time
import json


def lambda_handler(event, context):
    
    results_obj = {"results":[]}
    
    for reqs in event['request']:

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'From' : 'latimerh@oregonstate.edu'}
        response = requests.get(reqs['url'], headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
    
        if reqs['vendor'] == "walmart":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "office_depot":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.span.get_text().strip()
        elif reqs['vendor'] == "monoprice":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "ebay":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "bh":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "cdw":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price['content']
            
        results_obj["results"].append({"vendor": str(reqs["vendor"]), "price": str(formatted_price)})
        
 
    return {
        'statusCode': 200,
        'body': json.dumps(results_obj)
    }
import requests
from bs4 import BeautifulSoup
import time
import json


def lambda_handler(event, context):
    
    results_obj = {"results":[]}
    
    for reqs in event['request']:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
            'From': 'jonmoraga9@gmail.com'
        }
        response = requests.get(reqs['url'], headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
    
        if reqs['vendor'] == "walmart":
            try:
                formatted_price = soup.find(class_=reqs['html_tag'])['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "ebay":
            try:
                formatted_price = soup.find(class_=reqs['html_tag']).contents[0]
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "bh":
            try:
                formatted_price = soup.find(class_=reqs['html_tag']).contents[0]
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "cdw":
            try:
                formatted_price = soup.find(class_=reqs['html_tag'])['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "abt":
            try:
                formatted_price = soup.find("span", itemprop=reqs['html_tag'])['content']
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "newegg":
            data = soup.find_all(type='application/ld+json')
            try:
                json_data = json.loads(data[2].contents[0])
                dictionary_data = json_data.get("offers")
                formatted_price = dictionary_data.get('price')
            except:
                formatted_price = "unavailable"

            
        results_obj["results"].append({"vendor": str(reqs["vendor"]), "price": str(formatted_price)})
        
 
    return {
        'statusCode': 200,
        'body': json.dumps(results_obj)
    }
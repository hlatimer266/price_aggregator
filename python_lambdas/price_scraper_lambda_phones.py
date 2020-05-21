import requests
from bs4 import BeautifulSoup 
import time
import json
import re

def lambda_handler(event,context): 

    results_obj = {"results": []}

    for reqs in event['request']: 

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'From': 'escalasa@oregonstate.edu'}
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
        elif reqs['vendor'] == "overseas":
            try:
                price = soup.find(class_="PricesalesPrice")
                formatted_price = price.span.get_text().strip()
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "hsn":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "all":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "macofalltrades":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
        elif reqs['vendor'] == "cellbrokers":
            price = soup.find(class_=reqs['html_tag'])
            formatted_price = price.get_text().strip()
<<<<<<< HEAD
        results_obj['results'].append({'vendor': str(reqs['vendor']), 'price': str(formatted_price)})
=======
            
        if formatted_price.find("$") == -1 and formatted_price != "unavailable":
            formatted_price = "$" + formatted_price
            
        results_obj["results"].append({"vendor": str(reqs["vendor"]), "price": str(formatted_price), "url": str(reqs["url"])})
>>>>>>> master
        
    return {
        'statusCode': 200,
        'body': json.dumps(results_obj)
    }
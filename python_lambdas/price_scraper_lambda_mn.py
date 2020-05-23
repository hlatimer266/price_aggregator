import requests
from bs4 import BeautifulSoup
import time
import json
from lowest_price import find_lowest_price

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
            try:
                formatted_price = price.span.get_text().strip()
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "monoprice":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price.get_text().strip()
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "ebay":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price.get_text().strip()
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "bh":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price.get_text().strip()
            except:
                formatted_price = "unavailable"
        elif reqs['vendor'] == "cdw":
            price = soup.find(class_=reqs['html_tag'])
            try:
                formatted_price = price['content']
            except:
                formatted_price = "unavailable"
        
        if formatted_price.find("$") == -1 and formatted_price != "unavailable":
            formatted_price = "$" + formatted_price
            
        results_obj["results"].append({"vendor": str(reqs["vendor"]), "price": str(formatted_price), "url": str(reqs["url"])})
        
    find_lowest_price(results_obj, float(event['MSRP']))
    
    return {
        'statusCode': 200,
        'body': json.dumps(results_obj)
    }
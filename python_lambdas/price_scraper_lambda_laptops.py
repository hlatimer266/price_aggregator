import requests
import re
from bs4 import BeautifulSoup
import time
import json

def lambda_handler(event, context):

	results_obj = {"results":[]}

	for reqs in event['request']:

	   if reqs['vendor'] == "walmart":
	      #THIS WORKS 
	      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	      response = requests.get(reqs['url'], headers=headers)
	      soup = BeautifulSoup(response.text, 'html.parser')
	      price = soup.find("span", {"class": "price-characteristic", "content": True})['content']
	      print(price)
	      time.sleep(2)
	   elif reqs['vendor'] == "amazon":
	      #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	      headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
	      page = requests.get(reqs['url'], headers=headers)
	      soup = BeautifulSoup(page.content, 'lxml')
	      price = soup.find(id="priceblock_ourprice").get_text()
	      print(price)
	      time.sleep(2)
	   elif reqs['vendor'] == "bestbuy":
	      headers = {'User-Agent':'Mozilla/5.0'}
	      r = requests.get(reqs['url'], headers = headers)
	      p = re.compile(r'regularPrice\\":([\d.]+),')
	      price = p.findall(r.text)[0]
	      print(price)
	      time.sleep(2)
	   elif reqs['vendor'] == "newegg":
	      headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
	      page = requests.get(reqs['url'], headers = headers)
	      soup = BeautifulSoup(page.text, 'html.parser')
	      data = soup.find_all(type = 'application/ld+json')
	      json_data=json.loads(data[2].contents[0])
	      dictionary_data = json_data.get("offers")
	      print(dictionary_data.get('price'))
	      time.sleep(2)


	   results_obj['results'].append({'vendor': str(reqs['vendor']), 'price': str(formatted_price)})

	return {
        'statusCode': 200,
        'body': str(results_obj)
    }







import requests
import re
from bs4 import BeautifulSoup
import json


def lambda_handler(event, context):

	results_obj = {"results":[]}

	for reqs in event['request']:

		if reqs['vendor'] == "walmart":
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
			response = requests.get(reqs['url'], headers=headers)
			soup = BeautifulSoup(response.text, 'html.parser')
			formatted_price = soup.find("span", {"class": "price-characteristic", "content": True})['content']
		elif reqs['vendor'] == "amazon":
			headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
			page = requests.get(reqs['url'], headers=headers)
			# soup = BeautifulSoup(page.content, 'lxml')
			# formatted_price = soup.find(id="priceblock_ourprice").get_text()
			soup = BeautifulSoup(page.content, 'html.parser')
			try:
				formatted_price = soup.find(class_="priceblock_ourprice").get_text()
			except:
				formatted_price = "unavailable"
		elif reqs['vendor'] == "bestbuy":
			headers = {'User-Agent':'Mozilla/5.0'}
			r = requests.get(reqs['url'], headers = headers)
			p = re.compile(r'regularPrice\\":([\d.]+),')
			formatted_price = p.findall(r.text)[0]
		elif reqs['vendor'] == "newegg":
			headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
			page = requests.get(reqs['url'], headers = headers)
			soup = BeautifulSoup(page.text, 'html.parser')
			data = soup.find_all(type = 'application/ld+json')
			try:
				json_data=json.loads(data[2].contents[0])
				dictionary_data = json_data.get("offers")
				formatted_price = dictionary_data.get('price')
			except:
				formatted_price = "unavailable"
		
		results_obj['results'].append({'vendor': str(reqs['vendor']), 'price': str(formatted_price)})
	
	return {
		'statusCode' : 200,
		'body': json.dumps(results_obj)
	}
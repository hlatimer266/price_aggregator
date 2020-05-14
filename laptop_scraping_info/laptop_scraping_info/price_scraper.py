import requests
import re
from bs4 import BeautifulSoup
import time
import json

def scrape_laptops(url,vendor):
   
   if vendor == "walmart":
      
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
      response = requests.get(url, headers=headers)
      soup = BeautifulSoup(response.text, 'html.parser')
      price = soup.find("span", {"class": "price-characteristic", "content": True})['content']
      print(price)
      time.sleep(2)
   elif vendor == "newegg":
      headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
      page = requests.get(url, headers = headers)
      soup = BeautifulSoup(page.text, 'html.parser')
      data = soup.find_all(type = 'application/ld+json')
      json_data=json.loads(data[2].contents[0])
      dictionary_data = json_data.get("offers")
      print(dictionary_data.get('price'))
      time.sleep(2)
   elif vendor == "ebay":
      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
      response = requests.get(url, headers=headers)
      soup = BeautifulSoup(response.text, 'html.parser')
      price = soup.find(id='prcIsum')
      print(price.get_text())
      time.sleep(2)
   elif vendor == "bhphotovideo": 
      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
      response = requests.get(url, headers=headers)
      soup = BeautifulSoup(response.text, 'html.parser')
      price = soup.find(class_ = 'price_1DPoToKrLP8uWvruGqgtaY')
      print(price.get_text())
      time.sleep(2)
   elif vendor == "shopdevicesnow": 
      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
      response = requests.get(url, headers=headers)
      soup = BeautifulSoup(response.text, 'html.parser')
      price = soup.find(class_= 'current_price')
      print(price.get_text())
      time.sleep(2)
   elif vendor == "overseas": 
      headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
      response = requests.get(url, headers=headers)
      soup = BeautifulSoup(response.text, 'html.parser')
      price = soup.find(class_ = 'PricesalesPrice')
      print(price.get_text())

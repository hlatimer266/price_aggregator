import requests
import re
from bs4 import BeautifulSoup
import json



headers = { 'User-Agent': 'Adam Mercado', 'From': 'mercadoa@oregonstate.edu'}
page = requests.get('https://www.amazon.com/Acer-Nitro-i5-9300H-Windows-Renewed/dp/B07VZXHF3D/ref=sr_1_2?dchild=1&keywords=AN515-54-51M5&qid=1586845258&sr=8-2', headers=headers)
# soup = BeautifulSoup(page.content, 'lxml')
# formatted_price = soup.find(id="priceblock_ourprice").get_text()
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
formatted_price = soup.find(class_="priceInsideBuyBox_feature_div")
print(formatted_price)



# headers = {'User-Agent':'Mozilla/5.0'}
# r = requests.get(reqs['url'], headers = headers)
# p = re.compile(r'regularPrice\\":([\d.]+),')
# formatted_price = p.findall(r.text)[0]

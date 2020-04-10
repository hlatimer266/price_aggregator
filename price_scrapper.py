import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = 'https://www.amazon.com/FEICE-Stainless-Leathers-Waterproof-Business/dp/B074MWWTVL'

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, features="lxml")

price = soup.find_all("span")

print(price)

#price = soup.select("priceblock_saleprice")[0].get_text()

print(price)
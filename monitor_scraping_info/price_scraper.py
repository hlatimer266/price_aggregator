import requests
from bs4 import BeautifulSoup
import time


def scrape_monitors(url,html_tag,vendor):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'From' : 'latimerh@oregonstate.edu'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())

    if vendor == "walmart":
        price = soup.find(class_=html_tag)
        try:
            print(price['content'])
        except Exception as e:
            print(e)
            print("in exception block")
            time.sleep(20)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
            price = soup.find(class_=html_tag)
            print(price['content'])

    elif vendor == "office_depot":
        price = soup.find(class_=html_tag)
        print(price.span.get_text().strip())
    elif vendor == "monoprice":
        price = soup.find(class_=html_tag)
        print(price.get_text().strip())
    elif vendor == "ebay":
        price = soup.find(class_=html_tag)
        print(price.get_text().strip())
    elif vendor == "bh":
        price = soup.find(class_=html_tag)
        try:
            print(price.get_text().strip())
        except Exception as e:
            print("in exception block")
            time.sleep(20)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find(class_=html_tag)
            print(price.get_text().strip())
    elif vendor == "cdw":
        price = soup.find(class_=html_tag)
        print(price['content'])

    






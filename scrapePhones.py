
#################################################################

import requests
from bs4 import BeautifulSoup
import time
import re
import json

def scrape_phones(url, vendor):
    #url = 'https://www.ebay.com/itm/LG-Stylo-5-LM-Q720QM-32GB-Factory-Unlocked-CDMA-GSM-6-2-TFT-Aurora-Black/323982534657?epid=21034673794&hash=item4b6edd2801:g:r-kAAOSwOYZdrrd9'
    #headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    #response = requests.get(url, headers=headers)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())

    #walmart
    if vendor == "walmart":
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find("span", {"class": "price-characteristic", "content": True})['content']
        print(price) 
        
    
    #bhphotovideo 
    elif vendor == "bhphotovideo": 
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find(class_ = 'price_1DPoToKrLP8uWvruGqgtaY')
        print(price.get_text())
    
    #ebay 
    elif vendor == "ebay": 
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find(id='prcIsum')
        print(price.get_text())

    # newegg
    elif vendor == "newegg": 
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        data = soup.find_all(type = 'application/ld+json')
        json_data=json.loads(data[2].contents[0])
        dictionary_data = json_data.get("offers")
        print(dictionary_data.get('price'))
    

    #shopdevicesnow
    elif vendor == "shopdevicesnow": 
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find(class_= 'current_price')
        print(price.get_text())
   
    #overseas electronics
    elif vendor == "overseas": 
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find(class_ = 'PricesalesPrice')
        print(price.get_text())
    
    #bestbuy
    elif vendor == "bestbuy": 
        headers = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url, headers = headers)
        p = re.compile(r'regularPrice\\":([\d.]+),')
        price = p.findall(r.text)[0]
        print(price)
        
        '''
        headers = { 'User-Agent': 'Jimmy Escalante', 'From': 'escalasa@oregonstate.edu'}
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        item_container = soup.find(class_="priceView-hero-price priceView-customer-price")
        item = item_container.find_next('span')
        price = item.contents[2]
        print(price)
        '''
'''
if __name__ == "__main__":
    scrape_phones()
'''
##################################################################################################################################

## Brand: Apple ##

##################################################################################################################################
print("Brand: Apple")
## Model: Apple iPhone11 Pro 64 GB
###############################
print("Apple iPhone11 Pro 64 GB")
 # Ebay URL #verified
print("Ebay: ")
ebay_iphone11pro_url = 'https://www.ebay.com/itm/Apple-iPhone-11-Pro-Smartphone-AT-T-Sprint-T-Mobile-Verizon-or-Unlocked-LTE/293463314986?epid=18034218115&_trkparms=ispr%3D1&hash=item4453c6d22a:m:mVew2CUru7-AZhEMOfF2VWg&enc=AQAEAAACcIQvEcHUrT7nmUC3yY5qbPyaBN1nJEDYW8MyypsJPgXKMy1HQ5tqr4SizEZhU4A6p3HiRfJe50YX3%2FDnTFWaELS28SG87IDw%2FbOtOBroy6A7s9nkLmsFbBGV%2FkxxRkrin5ryYRLEdtLpawpURmEWmDPFtlGO1F1IoiSjkqognkryQV4DniAItDIzfxZo%2BRjOx29oBOqy6lOGxqYYg7zzov5ogqqD%2FtER1UjCNdPQOE7SH3ZramxpWVjMi064XYIU6D9eJE1haYc05DyucEwDmTGNJC0ZzIKVEo4NCTIW5NCr1v%2Bz7VLkXaA01Ntmr7if3k5LETh2D%2BQe2g3ULExsuTexxSqmy9gN1aSm3bxYZVolrfoCa2fCdJ0UeXMEAp%2FUfliBkCTMfCUFV%2FCnMfN8aq%2BymPLYCZAaTnGoMQ08Nif0Y7p7o12zM7z%2Bt4xgMMG%2FSyfn4Ozey9knQ8Jb2FbHGRCSyaNGE3S1SxUIy4N2rf815Vb3391GAX%2B5MLKMV46YDUE%2BcLSpYbxlTcAhKkj150%2B6IoqvlsuTxSVS24BFWMG87ZbiArF2JcN4XtiQ42yWFxqJ5qetgKokGQyjsNTZqhqyP8K4ZMZPTAGAyoPVyfrX4D5k5JIGykTbn3iO9Ltj2o6D%2BSER%2BKWLtzoeB9W1kxeXmb5LkTrIM1dgTLmjjH5aTsaITD0UqiKf%2BBSXVgRsELjRSsAqAQfuuiFMR59bLY0lPXB754K2LWaKi9%2Fzl7ToQkLyG7HTMoecV47hpSDsV3AneNnWab6gFH6nZMyYtFKbHUCdTsTpi%2BiEDqI%2BX57RCm1EvisVnSzOIgQACvPUbg%3D%3D&checksum=293463314986aa9f8ff7cdea4255a097f28137f49d5d'
scrape_phones(ebay_iphone11pro_url, "ebay")
 # ebay_iphone_tag = 'prcIsum'
 # tag is an id, not a class

# Shop DevicesNow URL #verified
print("Shop Devices Now: ")
shopdevices_iphone11pro_url = 'https://www.shopdevicesnow.com/collections/apple-iphones/products/apple-iphone-11-pro-max-64-256-512gb?variant=33723255259269'
scrape_phones(shopdevices_iphone11pro_url, "shopdevicesnow")
# shopdevices_iphone11pro_tag = 'current_price' 

# WalMart URL #verified
print("Walmart: ")
walmart_iphone11pro_url = 'https://www.walmart.com/ip/Straight-Talk-Apple-iPhone-11-Pro-Prepaid-with-64G-Space-Gray/778935868'
scrape_phones(walmart_iphone11pro_url, "walmart")
# walmart_iphone11pro_tag = 'price-characteristic'

# BestBuy URL #verified
print("BestBuy: ")
bestbuy_iphone11pro_url = 'https://www.bestbuy.com/site/apple-iphone-11-pro-with-64gb-memory-cell-phone-unlocked-space-gray/6223200.p?skuId=6223200'
scrape_phones(bestbuy_iphone11pro_url, "bestbuy")
# bestbuy_iphone11pro_tag = 'priceView-hero-price priceView-customer-price'

# NewEgg URL #verified
print("NewEgg: ")
newegg_iphone11pro_url = 'https://www.newegg.com/apple-iphone-11-pro-5-8-4g-lte/p/23B-000A-00AW6'
scrape_phones(newegg_iphone11pro_url, "newegg")


## Model: Apple iPhone11 128 GB
###############################
print("Apple iPhone 11")
# Ebay URL #verified
print("Ebay: ")
ebay_iphone11_url = 'https://www.ebay.com/itm/Apple-iPhone-11-128GB-Black-Verizon-T-Mobile-AT-T-Fully-Unlocked-Smartphone/233538968728?epid=13034214281&hash=item366001dc98:g:iQwAAOSw~yJee9NX'
scrape_phones(ebay_iphone11_url, "ebay")

 # Shop Devices Now URL  #verified
print("Shop Devices Now: ")
shopdevices_iphone11_url = 'https://www.shopdevicesnow.com/products/apple-iphone-11-128gb-black-verizon-t-mobile?_pos=2&_sid=708e622c1&_ss=r'
scrape_phones(shopdevices_iphone11_url, "shopdevicesnow")
 # class is 'current_price
 
 # WalMart URL #verified
print("Walmart: ")
walmart_iphone11_url = 'https://www.walmart.com/ip/Refurbished-Apple-iPhone-11-128GB-Black-LTE-Cellular-AT-T-MWJ02LL-A/734504118'
scrape_phones(walmart_iphone11_url, "walmart")

 # BestBuy URL #verified 
print("BestBuy: ")
bestbuy_iphone11_url = 'https://www.bestbuy.com/site/apple-iphone-11-with-128gb-memory-cell-phone-unlocked-black/6223315.p?skuId=6223315'
scrape_phones(bestbuy_iphone11_url, "bestbuy")

 # NewEgg URL #verified
print("NewEgg: ")
newegg_iphone11_url = 'https://www.newegg.com/apple-iphone-11-6-1-4g-lte/p/23B-000A-00AW5?Description=iphone11&cm_re=iphone11-_-23B-000A-00AW5-_-Product'
scrape_phones(newegg_iphone11_url, "newegg")



 ## Model: Apple iPhone XS MAX 64GB
###############################
print("Apple iPhone XS MAX 64GB")
# Ebay URL #verified
print("Ebay: ")
ebay_iphonexsmax_url = 'https://www.ebay.com/itm/Apple-iPhone-XS-Max-64GB-256GB-512GB-Unlocked-Verizon-AT-T-T-Mobile-Sprint/193224103053?epid=21023707461&var=493632710935&_trkparms=ispr%3D1&hash=item2cfd0dd48d:g:NT0AAOSwmWxd1Hnr&enc=AQAEAAACcIQvEcHUrT7nmUC3yY5qbPyaBN1nJEDYW8MyypsJPgXK4PLYVaIgu9w9Os2XtDHJetmys1prgg6Qs6%2BfnrRPHsw02EkGKdkCO%2Bqwht50FsmCDmyYbs8nPffX3xOlu2LcaD%2BDdW%2FGTv%2BDkJTKlOHixxZOaMyEWwFERW6lbsv98crshpmadWntA2X6UbeUXmn6VcbGmUz1NwbTVeDzXoIf0P94u12YTwcAwG3FuGr%2B0R1Nig2WhEQovG%2FZFbaWHymivvrAyWsN%2FUOlpidPTMXITNYm6X8Xz5BXWACoZ5rmgJeqjPZGxKhWiU4%2B5wvNlmNB%2FxmMBlDd8IQt9p918rstSVm05n0NWihefisslokrB3VwFjXu32gMANJGpw73fSjbH%2BPsmMe2ZzV%2B4wEpCV1xoS6m%2BL11voyKKW6fOydur7yLcw0bcWpo5vXCP20W9tAOGnsf7zbw2QaqZl9D2%2FYzBexeTCpgC5Dg2GI7Jv67eW7Rzk0UwwNHLZbKAwmaFbvXVzUMHBRgDnIJVkKFli9qE%2BHynZVlwK1%2FU1cFDJ3TaZCVymr6chg2piMBvPcK4o3xRl%2BEwKUgPsNJ0Ei2HSy5dkWhxNAGbBaotXIL0PHpZNUlFVxIDhxNm1RMnzdHjJ62nysW1A3kNW5nxRap9lDgJRw8v%2BZ%2B7CUDWYtA623Yz5HFhlgUBzuGBVG%2BCjEBrFcSWGqy7aPZao22i0gAZQPzU3hs0F%2Fv4JZD5FkqtaiascE2nxoXnbAm3ujRr0Z2yLZ3lkKn13DqjNAmoowXonHCVlgIMAgNMoMVBU3YlJyPo8IHqQrRL3Q3vB9Shn9Q3wpPQQ%3D%3D&checksum=1932241030533b2b594f6ea64edd9d8571506fa2a6ef'
scrape_phones(ebay_iphonexsmax_url, "ebay")

 # Shop Devices Now URL #verified
print("Shop Devices Now: ")
shopdevices_iphonexsmax_url = 'https://www.shopdevicesnow.com/products/apple-iphone-xs-max-a1921-64gb-space-gray-fully-unlocked-gsm-cdma-smartphone?_pos=2&_sid=ff76db471&_ss=r'
scrape_phones(shopdevices_iphonexsmax_url, "shopdevicesnow")
 # class is 'current_price

 # WalMart URL #verified
print("Walmart: ")
walmart_iphonexsmax_url = 'https://www.walmart.com/ip/Straight-Talk-Apple-iPhone-XS-MAX-w-64GB-Gray/702494549'
scrape_phones(walmart_iphonexsmax_url, "walmart")

 # BestBuy URL #verified
print("BestBuy: ")
bestbuy_iphonexsmax_url = 'https://www.bestbuy.com/site/apple-iphone-xs-max-with-64gb-memory-cell-phone-unlocked-space-gray/7639067.p?skuId=7639067'
scrape_phones(bestbuy_iphonexsmax_url, "bestbuy")

# NewEgg URL #verified
print("NewEgg: ")
newegg_iphonexsmax_url = 'https://www.newegg.com/grey-apple-6-gsm-hspa-lte/p/23B-000A-00802'
scrape_phones(newegg_iphonexsmax_url, "newegg")

## Model: Apple iPhone XR 64GB
###############################
print("Apple iPhone XR 64 GB")
 # Ebay URL #verified
print("Ebay: ")
ebay_iphonexr_url = 'https://www.ebay.com/itm/Apple-iPhone-XR-64GB-Factory-Unlocked-Smartphone-4G-LTE-iOS-Smartphone/254187678666?epid=13023706562&hash=item3b2ec42bca:m:mxcsaipOrUeYbznT5gw1ibA#viTabs_0'
scrape_phones(ebay_iphonexr_url, "ebay")
 # ebay_iphonexr_tag = 'notranslate'

# Shop Devices Now URL #verified
print("Shop Devices Now: ")
shopdevices_iphonexr_url = 'https://www.shopdevicesnow.com/products/apple-iphone-xr-64gb-factory-unlocked-smartphone-4g-lte-ios-smartphone-1?_pos=1&_sid=cb973e9d7&_ss=r'
scrape_phones(shopdevices_iphonexr_url, "shopdevicesnow")
 # class is 'current_price'

 # WalMart URL #verified
print("Walmart: ")
walmart_iphonexr_url = 'https://www.walmart.com/ip/Apple-iPhone-XR-64GB-Fully-Unlocked-Verizon-Sprint-GSM-Unlocked-Black/783476112'
scrape_phones(walmart_iphonexr_url, "walmart")
 # walmart_iphonexr_tag = 'price-characteristic'

 # BestBuy URL #verified
print("BestBuy: ")
bestbuy_iphonexr_url = 'https://www.bestbuy.com/site/apple-iphone-xr-with-64gb-memory-cell-phone-unlocked-black/1724437.p?skuId=1724437'
scrape_phones(bestbuy_iphonexr_url, "bestbuy")
 # bestbuy_iphonexr_tag = 'priceView-hero-price priceView-customer-price'

 # NewEgg URL #verified
print("NewEgg: ")
newegg_iphonexr_url = 'https://www.newegg.com/apple-iphone-xr-6-1-4g-lte-black/p/0V4-0011-00P67?Item=0V4-0011-00P67'
scrape_phones(newegg_iphonexr_url, "newegg")
##################################################################################################################################

## Brand: Google  ##

##################################################################################################################################
print("Brand: Google")

## Model: Google Pixel 4 64GB
###############################
print("\nGoogle Pixel 4 64GB")
'''
 # ebay #verified
ebay_pixel4_url = 'https://www.ebay.com/itm/NEW-SEALED-Google-Pixel-4-64GB-Factory-Unlocked-Just-Black/293551293959?epid=18006492702&hash=item4459054607:g:m6MAAOSwO5BeYU23'
scrape_phones(ebay_pixel4_url, "ebay")
'''

 # bhphotovideo #verified
print("B&H Photo Video: ")
bh_pixel4_url = 'https://www.bhphotovideo.com/c/product/1507474-REG/google_ga01187_us_pixel_4_64gb_smartphone.html'
scrape_phones(bh_pixel4_url, "bhphotovideo")
 # bh_pixel4_tag = 'price_1DPoToKrLP8uWvruGqgtaY'

 # newegg  #verified
print("Newegg: ")
newegg_pixel4_url = 'https://www.newegg.com/black-google-pixel-5-7-gsm-hspa-lte/p/23B-001E-00195?Description=google%20pixel&cm_re=google_pixel-_-9SIABPXANY4159-_-Product&quicklink=true'
scrape_phones(newegg_pixel4_url, "newegg")

 # walmart #verified
walmart_pixel4_url = 'https://www.walmart.com/ip/Google-Pixel-4-Black-64-GB-Unlocked/925508836'
print("Walmart")
scrape_phones(walmart_pixel4_url, "walmart")

 # bestbuy #verified
print("Best Buy")
bestbuy_pixel4_url = 'https://www.bestbuy.com/site/google-pixel-4-with-64gb-cell-phone-unlocked-just-black/6382490.p?skuId=6382490'
scrape_phones(bestbuy_pixel4_url, "bestbuy")

 # overseas electronics #verified 
print("Overseas: ")
overseas_pixel4_url = 'https://welectronics.com/index.php?option=com_virtuemart&view=productdetails&virtuemart_product_id=9782&virtuemart_category_id=145&Itemid=1&gclid=EAIaIQobChMI3LHRurP46AIVB8DICh2q1QJGEAkYDyABEgJOT_D_BwE'
scrape_phones(overseas_pixel4_url, "overseas")
 # class is 'PricesalesPrice'
 ###############################

## Model: Google Pixel 4 XL
###############################
print("Google Pixel 4 XL")

 # ebay #verified
print("Ebay: ")
ebay_pixel4xl_url = 'https://www.ebay.com/itm/Google-Pixel-4XL-64-or-128-GB-Verizon-Black-White-Orange/392691261623?hash=item5b6e3920b7:m:mQI141ySrihNbizoo9bRYKA'
scrape_phones(ebay_pixel4xl_url, "ebay")

 # bhphotovideo #verified
print("B&H Photo Video")
bh_pixel4xl_url = 'https://www.bhphotovideo.com/c/product/1507481-REG/google_ga01180_us_pixel_4_xl_64gb.html'
scrape_phones(bh_pixel4xl_url, "bhphotovideo")
 # bh_tag = 'price_1DPoToKrLP8uWvruGqgtaY'

 # newegg #verified
print("Newegg: ")
newegg_pixel4xl_url = 'https://www.newegg.com/p/23B-001E-001E0?Description=google%20pixel&cm_re=google_pixel-_-9SIAJNJB7U6146-_-Product'
scrape_phones(newegg_pixel4xl_url, "newegg")

 # walmart #verified
print("Walmart: ")
 # WalMart URL
walmart_pixel4xl_url = 'https://www.walmart.com/ip/Google-Pixel-4-XL-Black-64-GB-Unlocked/419637576'
scrape_phones(walmart_pixel4xl_url, "walmart")

 # BestBuy URL #verified
print("Best Buy: ")
bestbuy_pixel4xl_url = 'https://www.bestbuy.com/site/google-pixel-4-xl-with-64gb-cell-phone-unlocked-just-black/6382531.p?skuId=6382531'
scrape_phones(bestbuy_pixel4xl_url, "bestbuy")

 # overseas electronics #verified 
print("Overseas: ")
overseas_pixel4XL_url = 'https://welectronics.com/shopping/gsm-phones/google-pixel-4-xl-unlocked-gsm-phone-detail'
scrape_phones(overseas_pixel4XL_url, "overseas")
 # class is 'PricesalesPrice'
###############################


## Model: Google Pixel 3a
###############################
print("Google Pixel 3a")
 # Ebay URL #verified
'''
print("Ebay: ")
ebay_pixel3a_url = 'https://www.ebay.com/itm/Google-Pixel-3a-Smartphone-64GB-Unlocked-Just-Black-Brand-New/114017156941?epid=5031779894'
scrape_phones(ebay_pixel3a_url, "ebay")
'''

# bhphotovideo URL #verified
print("B&H Photo Video")
bh_pixel3a_url = 'https://www.bhphotovideo.com/c/product/1475547-REG/google_ga00655_us_pixel_3a_smartphone_unlocked.html'
scrape_phones(bh_pixel3a_url, "bhphotovideo")

# newegg #verified
print("Newegg: ")
newegg_pixel3a_url = 'https://www.newegg.com/black-google-5-6-gsm-hspa-lte/p/23B-001E-000W1?Description=google%20pixel&cm_re=google_pixel-_-23B-001E-000W1-_-Product'
scrape_phones(newegg_pixel3a_url, "newegg")

# walmart #verified
print("Walmart: ")
# WalMart URL
walmart_pixel3a_url = 'https://www.walmart.com/ip/Google-Pixel-3a-Black/663614013'
scrape_phones(walmart_pixel3a_url, "walmart")

 # BestBuy URL #verified
print("Best Buy: ")
bestbuy_pixel3a_url = 'https://www.bestbuy.com/site/google-pixel-3a-64gb-unlocked-just-black/6347785.p?skuId=6347785'
scrape_phones(bestbuy_pixel3a_url, "bestbuy")

# overseas electronics #verified 
print("Overseas: ")
overseas_pixel3a_url = 'https://welectronics.com/shopping/gsm-phones/google-pixel-3a-unlocked-dual-sim-phone-detail'
scrape_phones(overseas_pixel3a_url, "overseas")
 # class is 'PricesalesPrice'

###############################


## Model: Google Pixel 3aXL
###############################
print("\nGoogle Pixel 3aXL")
 # Ebay URL #verified
print("Ebay:")
ebay_pixel3axl_url = 'https://www.ebay.com/itm/Unlocked-Google-Pixel-3A-XL-64GB-CDMA-GSM-Black-White-Purple-Smartphone/202757052183?_trkparms=aid%3D1110001%26algo%3DSPLICE.SIM%26ao%3D1%26asc%3D20160323102634%26meid%3D6e98a5bdfeb7423abb998995f916a42c%26pid%3D100623%26rk%3D1%26rkt%3D5%26mehot%3Dpp%26sd%3D202721618157%26itm%3D202757052183%26pmt%3D0%26noa%3D1%26pg%3D2047675&_trksid=p2047675.c100623.m-1https://www.ebay.com/itm/Unlocked-Google-Pixel-3A-XL-64GB-CDMA-GSM-Black-White-Purple-Smartphone/202757052183?_trkparms=aid%3D1110001%26algo%3DSPLICE.SIM%26ao%3D1%26asc%3D20160323102634%26meid%3D6e98a5bdfeb7423abb998995f916a42c%26pid%3D100623%26rk%3D1%26rkt%3D5%26mehot%3Dpp%26sd%3D202721618157%26itm%3D202757052183%26pmt%3D0%26noa%3D1%26pg%3D2047675&_trksid=p2047675.c100623.m-1'
scrape_phones(ebay_pixel3axl_url, "ebay")

# bhphotovideo URL #verified
print("B&H Photo Video: ")
bh_pixel3axl_url = 'https://www.bhphotovideo.com/c/product/1475550-REG/google_ga00664_us_pixel_3a_xl_smartphone.html'
scrape_phones(bh_pixel3axl_url, "bhphotovideo")

 # newegg #verified
print("Newegg: ")
newegg_pixel3axl_url = 'https://www.newegg.com/black-google-pixel-3a-6-4g-lte/p/23B-001E-00124?Description=google%20pixel%203a%20Xl&cm_re=google_pixel_3a_Xl-_-9SIAFVD9R64004-_-Product&quicklink=true'
scrape_phones(newegg_pixel3axl_url, "newegg")

 # walmart #verified
print("Walmart: ")
 # WalMart URL
walmart_pixel3axl_url = 'https://www.walmart.com/ip/Google-Pixel-XL-3a-Black-Factory-Unlocked/767183825?selected=true'
scrape_phones(walmart_pixel3axl_url, "walmart")

 # BestBuy URL #verified
print("Bestbuy: ")
bestbuy_pixel3axl_url = 'https://www.bestbuy.com/site/google-pixel-3a-xl-64gb-unlocked-just-black/6347790.p?skuId=6347790'
scrape_phones(bestbuy_pixel3axl_url, "bestbuy")

# overseas electronics #verified 
print("Overseas: ")
overseas_pixel3aXL_url = 'https://welectronics.com/shopping/gsm-phones/google-pixel-3a-xl-unlocked-dual-sim-phone-detail'
scrape_phones(overseas_pixel3aXL_url, "overseas")
 # class is 'PricesalesPrice'
###############################


##################################################################################################################################

## Brand: Samsung ##

##################################################################################################################################

print("Brand: Samsung: \n")

## Model: Galaxy S20 Ultra 5G 128GB 
############################
print("Galaxy S20 Ultra") 

# Overseas electronics #verified
print("Overseas: ")
overseas_s20ultra_url = 'https://www.welectronics.com/shopping/gsm-phones/samsung-galaxy-s20-ultra-5g-g988b-ds-unlocked-gsm-phone-detail'
scrape_phones(overseas_s20ultra_url, "samsung")

# bh photo video #verified
print("B&H Photo Video: ")
bh_s20ultra_url = 'https://www.bhphotovideo.com/c/product/1543097-REG/samsung_sm_g988uzkaxaa_galaxy_s20_ultra_sm_g988u.html'
scrape_phones(bh_s20ultra_url, "bhphotovideo")

# walmart #verified
print("Walmart: ")
walmart_s20ultra_url = 'https://www.walmart.com/ip/SAMSUNG-Unlocked-Galaxy-S20-Ultra-128GB-Gray-Smartphone/325765146'
scrape_phones(walmart_s20ultra_url, "walmart")

# best buy #verified
print("Best Buy: ")
bestbuy_s20ultra_url = 'https://www.bestbuy.com/site/samsung-galaxy-s20-ultra-5g-enabled-128gb-unlocked-cosmic-black/6395758.p?skuId=6395758'
scrape_phones(bestbuy_s20ultra_url, "bestbuy")

# ebay #verified
print("Ebay: ")
ebay_s20ultra_url = 'https://www.ebay.com/itm/Samsung-Galaxy-S20-Ultra-SM-G988B-DS-128GB-12GB-RAM-FACTORY-UNLOCKED-6-9-108MP/202906112669?epid=16036969474'
scrape_phones(ebay_s20ultra_url, "ebay")

#newegg #verified 
print("Newegg: ")
newegg_s20ulta_url = 'https://www.newegg.com/samsung-galaxy-s20-ultra-5g-6-9-cosmic-black/p/N82E16875169858?Description=galaxy%20ultra&cm_re=galaxy_ultra-_-75-169-858-_-Product'
scrape_phones(newegg_s20ulta_url, "newegg")

###############################


## Model: Galaxy S20 Plus 5G 128GB 
print("Galaxy S20 Plus 5G")
###############################
# Overseas electronics #verified
print("Overseas: ")
overseas_s20plus_url = 'https://www.welectronics.com/shopping/gsm-phones/samsung-galaxy-s20-plus-g985fds-unlocked-gsm-phone-9865-9866-detail'
scrape_phones(overseas_s20plus_url, "overseas")

# bh photo video  #verified
print("B&H Photo Video: ")
bh_s20plus_url = 'https://www.bhphotovideo.com/c/product/1543094-REG/samsung_sm_g986uzkaxaa_galaxy_s20_sm_g986u_128gb.html'
scrape_phones(bh_s20ultra_url, "bhphotovideo")

# walmart #verified
print("Walmart: ")
walmart_s20plus_url = 'https://www.walmart.com/ip/SAMSUNG-Unlocked-Galaxy-S20-Plus-128GB-Black-Smartphone/639071082'
scrape_phones(walmart_s20plus_url, "walmart")

# best buy #verified
print("Best Buy: ")
bestbuy_s20plus_url = 'https://www.bestbuy.com/site/samsung-galaxy-s20-5g-enabled-128gb-unlocked-cosmic-black/6395756.p?skuId=6395756'
scrape_phones(bestbuy_s20ultra_url, "bestbuy")

# ebay #verified
print("Ebay: ")
ebay_s20plus_url = 'https://www.ebay.com/itm/Samsung-Galaxy-S20-Plus-SM-G985F-DS-128GB-8GB-RAM-FACTORY-UNLOCKED-6-7-64MP/202905303442?epid=27037171664'
scrape_phones(ebay_s20plus_url, "ebay")

#  newegg #verified 
print("Newegg: ")
newegg_s20plus_url = 'https://www.newegg.com/samsung-galaxy-s20-5g-6-7-cosmic-black/p/N82E16875169855'
scrape_phones(newegg_s20plus_url, "newegg")
###############################


## Model: Galaxy S20 5G 128 GB
print("Galaxy S20 5G ")
###############################

# Overseas electronics #verified
print("Overseas: ")
overseas_s20_url = 'https://www.welectronics.com/shopping/gsm-phones/samsung-galaxy-s20-unlocked-gsm-phone-9860-detail'
scrape_phones(overseas_s20_url, "overseas")

# bh photo video #verified
print("B&G Photo Video: ")
bh_s20_url = 'https://www.bhphotovideo.com/c/product/1543089-REG/samsung_sm_g981uzaaxaa_galaxy_s20_sm_g981u_128gb.html'
scrape_phones(bh_s20_url, "bhphotovideo")


# walmart #verified
print("Walmart: ")
walmart_s20_url =  'https://www.walmart.com/ip/SAMSUNG-Unlocked-Galaxy-S20-128GB-Gray-Smartphone/556470530'
scrape_phones(walmart_s20_url, "walmart")

# best buy #verified
print("Best Buy: ")
bestbuy_s20_url = 'https://www.bestbuy.com/site/samsung-galaxy-s20-5g-enabled-128gb-unlocked-cloud-blue/6395747.p?skuId=6395747'
scrape_phones(bestbuy_s20_url, "bestbuy")

# ebay #verified
print("Ebay: ")
ebay_s20_url = 'https://www.ebay.com/itm/Samsung-Galaxy-S20-128GB-8GB-SM-G980F-DS-Dual-Sim-FACTORY-UNLOCKED-6-2-64-MP/372949785456?_trkparms=ispr%3D1'
scrape_phones(ebay_s20_url, "ebay")

# newegg #verified 
print("Newegg: ")
newegg_s20_url = 'https://www.newegg.com/samsung-galaxy-s20-5g-6-2-cosmic-gray/p/N82E16875169850?Description=s20%205g&cm_re=s20_5g-_-75-169-850-_-Product'
scrape_phones(newegg_s20_url, "newegg")
###############################

## Model: Galaxy S10 Plus 128GB
###############################

# Overseas electronics #verified
print("Overseas: ")
overseas_s10plus_url = 'https://www.welectronics.com/shopping/gsm-phones/samsung-galaxy-s10-plus-unlocked-gsm-phone-7521-detail'
scrape_phones(overseas_s10plus_url, "overseas")

print("B&G Photo Video: ")
# bh photo video #verified
bh_s10plus_url = 'https://www.bhphotovideo.com/c/product/1456416-REG/samsung_sm_g975uzkaxaa_galaxy_s10_sm_g975u_128gb.html'
scrape_phones(bh_s10plus_url, "bhphotovideo")

print("Walmart: ")
# walmart #verified
walmart_s10plus_url =  'https://www.walmart.com/ip/SAMSUNG-Unlocked-Galaxy-S10-Plus-128GB-Black-Smartphone/480000580'
scrape_phones(walmart_s10plus_url, "walmart")

print("Best Buy: ")
# best buy #verified
bestbuy_s10plus_url = 'https://www.bestbuy.com/site/samsung-galaxy-s10-with-128gb-memory-cell-phone-unlocked-prism-black/6323863.p?skuId=6323863'
scrape_phones(bestbuy_s10plus_url, "bestbuy")

# ebay #verified
print("Ebay: ")
ebay_s10plus_url = 'https://www.ebay.com/itm/NEW-Samsung-Galaxy-S10-Plus-128-512GB-1TB-SM-G975U1-Unlocked-All-Colors/163793825474'
scrape_phones(ebay_s10plus_url, "ebay")

# newegg #verified 
print("Newegg: ")
newegg_s10plus_url = 'https://www.newegg.com/p/23B-0002-00BD0?Description=Samsung%20Galaxy%20S10plus&cm_re=Samsung_Galaxy_S10plus-_-9SIAJ3AA3S7785-_-Product'
scrape_phones(newegg_s10plus_url, "newegg")

###############################

##################################################################################################################################

## Brand: LG ##
print("\nBrand: LG\n")

##################################################################################################################################

## Model: LG V40 ThinQ 64GB Unlocked
###############################
print("LG V40 ThinQ")
#best buy #verified
print("Best Buy: ")
bestbuy_v40thinq_url = 'https://www.bestbuy.com/site/lg-v40-thinq-with-64gb-memory-cell-phone-unlocked-aurora-black/6305718.p?skuId=6305718'
scrape_phones(bestbuy_v40thinq_url, "bestbuy")

# newegg #verified 
print("Newegg: ")
newegg_v40thinq_url = 'https://www.newegg.com/lg-v40-thinq-6-4-4g-lte-aurora-black/p/23B-000F-001J9?Description=phones&cm_re=phones-_-23B-000F-001J9-_-Product' 
scrape_phones(newegg_v40thinq_url, "newegg")

# bh photo vid #verified
print("B&G Photo Video: ")
bh_v40thinq_url = 'https://www.bhphotovideo.com/c/product/1436639-REG/lg_lmv405qa7_ausabk_v40_thinq_64gb_smartphone.html'
scrape_phones(bh_v40thinq_url, "bhphotovideo")

# ebay #verified
print("Ebay:")
ebay_v40thinq_url = 'https://www.ebay.com/itm/LG-V40-ThinQ-64GB-Black-Unlocked-Smartphone-LM-V405QA7USABK-QHD-OLED-Screen/362882303051?epid=8024885378'
scrape_phones(ebay_v40thinq_url, "ebay")

# walmart #verified
print("WalMart: ")
walmart_v40thinq_url = 'https://www.walmart.com/ip/LG-V40-ThinQ-Smartphone-Black-LGV40/771963221'
scrape_phones(walmart_v40thinq_url, "walmart")

###############################

## Model: LG G8X ThinQ 128GB Unlocked
###############################
print("LG G8X ThinQ\n")
# best buy #verified
print("Best Buy: ")
bestbuy_g8x_url = 'https://www.bestbuy.com/site/lg-g8-thinq-with-128gb-memory-cell-phone-unlocked-aurora-black/6337607.p?skuId=6337607'
scrape_phones(bestbuy_g8x_url, "bestbuy")

# newegg #verified also dual screen
#print("Newegg: ")
#newegg_g8x_url = 'https://www.newegg.com/lg-g8x-thinq-6-4-gsm-hspa-lte-aurora-black/p/23B-000F-001J6?Description=phones&cm_re=phones-_-9SIABPXB5J9800-_-Product'
#scrape_phones(newegg_g8x_url, "newegg")

# bh photo vid #verified
#print("B&G Photo Video: ")
# This is a dual screen version, worthless
# bh_g8x_url = 'https://www.bhphotovideo.com/c/product/1512988-REG/lg_lmg850qm7x_ausabk_g8x_thinq_128gb_smartphone.html'

#overseas electronics verified
print("Overseas: ")
overseas_g8x_url = "https://www.welectronics.com/shopping/gsm-phones/lg-g8x-thinq-unlocked-dual-sim-phone-128gb-detail"
scrape_phones(overseas_g8x_url, "overseas")

# ebay #verified
print("Ebay: ")
ebay_g8x_url = 'https://www.ebay.com/itm/LG-G8X-ThinQ-LMG850UM-Latest-128GB-Black-AT-T-GSM-Unlocked-T-Mobile-Smartphone/131840731869'
scrape_phones(ebay_g8x_url, "ebay")

# walmart #verified
print("Walmart: ")
walmart_g8x_url = 'https://www.walmart.com/ip/LG-G8-ThinQ-128GB-Unlocked-Smartphone-Black/724389745'
scrape_phones(walmart_g8x_url, "walmart")
###############################

## Model: LG K30 16 GB
###############################
print("LG K30")
#best buy #verified
print("Best Buy: ")
bestbuy_k30_url = 'https://www.bestbuy.com/site/lg-k30-2019-lm-x320qmg-with-16gb-memory-cell-phone-unlocked-black/6363047.p?skuId=6363047'
scrape_phones(bestbuy_k30_url, "bestbuy")

# newegg #verified 
print("Newegg: ")
newegg_k30_url = 'https://www.newegg.com/black-lg-k30-5-3-4g-lte/p/N82E16875136496?Description=phones&cm_re=phones-_-9SIA25VA0U3274-_-Product'
scrape_phones(newegg_k30_url, "newegg")

# bh photo vid #verified
print("B&G Photo Video: ")
bh_k30_url = 'https://www.bhphotovideo.com/c/product/1501306-REG/lg_lmx320qmg_ausabky_k30_16gb_smartphone_unlocked.html?sts=pi&pim=Y'
scrape_phones(bh_k30_url, "bhphotovideo")

# ebay #verified
print("Ebay: ")
ebay_k30_url = 'https://www.ebay.com/itm/LG-K30-2019-LM-X320QMG-16GB-4G-LTE-Factory-Unlocked-CDMA-GSM-5-4-HD-Android8/223746024286?epid=10034673698&'
scrape_phones(ebay_k30_url, "ebay")

# walmart #verified
print("Walmart: ")
walmart_k30_url = 'https://www.walmart.com/ip/LG-K30-LM-X410AS-16GB-AT-T-GSM-Unlocked-Smartphone-Black/504200346'
scrape_phones(walmart_k30_url, "walmart")
###############################

## Model:  LG Stylo 5
###############################
print("LG Stylo 5\n")

#best buy #verified
print("Best Buy: ")
bestbuy_stylo5_url = 'https://www.bestbuy.com/site/lg-stylo-5-aurora-black-unlocked/6363050.p?skuId=6363050'
scrape_phones(bestbuy_stylo5_url, "bestbuy")

# model not found on newegg
# newegg_stylo5_url = 

# ebay #verified
print("Ebay: ")
ebay_stylo5_url = 'https://www.ebay.com/itm/LG-Stylo-5-LM-Q720QM-32GB-Factory-Unlocked-CDMA-GSM-6-2-TFT-Aurora-Black/323982534657?epid=21034673794&hash=item4b6edd2801:g:r-kAAOSwOYZdrrd9'
scrape_phones(ebay_stylo5_url, "ebay")

# bh photo vid #verified
print("B&G Photo Video: ")
bh_stylo5_url = 'https://www.bhphotovideo.com/c/product/1500980-REG/lg_lmq720qm_ausabk_stylo_5_32gb_smartphone.html'
scrape_phones(bh_stylo5_url, "bhphotovideo")

# walmart #verified
print("Walmart: ")
walmart_stylo5_url = 'https://walmart.com/ip/Straight-Talk-LG-Stylo-5-Smartphone/220381286'
scrape_phones(walmart_stylo5_url, "walmart")
###############################
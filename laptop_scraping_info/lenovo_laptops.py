import price_scraper as ps 

if __name__ == "__main__":

	####################### Lenovo Model 1 #######################
	#Lenovo Ideapad 1 A6 Series; Model:81VS0001US - Best Buy
	lenovo_bestbuyURL = 'https://www.bestbuy.com/site/lenovo-ideapad-1-14-laptop-amd-a6-series-4gb-memory-amd-radeon-r4-64gb-emmc-flash-memory-platinum-gray/6359222.p?skuId=6359222'
	ps.scrape_laptops(lenovo_bestbuyURL,"bestbuy")

	#Lenovo Ideapad 1 A6 Series; Model:81VS0001US - Walmart
	lenovo_walmartURL = 'https://www.walmart.com/ip/Lenovo-IdeaPad-1-A6-9220e-14-AMD-A6-9220e-64GB-4GB-RAM-Gray-81VS0001US/711787502'
	ps.scrape_laptops(lenovo_walmartURL, "walmart")

	#Lenovo Ideapad 1 A6 Series; Model:81VS0001US - Newegg
	lenovo_neweggURL = 'https://www.newegg.com/gray-lenovo-ideapad-1-81vs0001us/p/1TS-000E-0FC04?Description=81VS0001US&cm_re=81VS0001US-_-9SIAEYJAKK0926-_-Product&quicklink=true'
	ps.scrape_laptops(lenovo_neweggURL, "newegg")

	#Lenovo Ideapad 1 A6 Series; Model:81VS0001US - Amazon
	lenovo_amazonURL = 'https://www.amazon.com/Lenovo-S150-81VS0001US-A6-9220e-Bluetooth/dp/B081ZGN8JQ/ref=sr_1_2?dchild=1&m=A3EMUGYCY87GQ1&marketplaceID=ATVPDKIKX0DER&qid=1587466504&refinements=p_4%3ALenovo&s=merchant-items&sr=1-2'
	ps.scrape_laptops(lenovo_amazonURL, "amazon")

	####################### Lenovo Model 2 #######################
	#Lenovo - Yoga C940 2-in-1 14" Touch-Screen Laptop - Intel Core i7 - 12GB Memory - 512GB Solid State Drive - Iron Gray; - Best Buy
	lenovo_bestbuyURL2 = 'https://www.bestbuy.com/site/lenovo-yoga-c940-2-in-1-14-touch-screen-laptop-intel-core-i7-12gb-memory-512gb-solid-state-drive-iron-gray/6367799.p?skuId=6367799'
	ps.scrape_laptops(lenovo_bestbuyURL2,"bestbuy")

	#Lenovo - Yoga C940 2-in-1 14" Touch-Screen Laptop - Intel Core i7 - 12GB Memory - 512GB Solid State Drive - Iron Gray; - Walmart
	lenovo_walmartURL2 = 'https://www.walmart.com/ip/Laptop-Touch-Screen-Memory-Iron-C940-Intel-Solid-Computer-Drive-Tablet-14-Core-Lenovo-Gray-Notebook-81Q9002GUS-12GB-i7-512GB-PC-State-2-in-1-Yoga/683743162'
	ps.scrape_laptops(lenovo_walmartURL2, "walmart")

	#Lenovo - Yoga C940 2-in-1 14" Touch-Screen Laptop - Intel Core i7 - 12GB Memory - 512GB Solid State Drive - Iron Gray; - Newegg
	lenovo_neweggURL2 = 'https://www.newegg.com/p/1TS-000E-0F8Z3?Description=81Q9002GUS&cm_re=81Q9002GUS-_-1TS-000E-0F8Z3-_-Product'
	ps.scrape_laptops(lenovo_neweggURL2, "newegg")

	#Lenovo - Yoga C940 2-in-1 14" Touch-Screen Laptop - Intel Core i7 - 12GB Memory - 512GB Solid State Drive - Iron Gray; - Amazon
	lenovo_amazonURL2 = 'https://www.amazon.com/Lenovo-Yoga-C940-14-Touch-i7-1065G7-12GB/dp/B0811ZZMP9/ref=sr_1_1?dchild=1&keywords=81Q9002GUS&qid=1586840791&sr=8-1'
	ps.scrape_laptops(lenovo_amazonURL2, "amazon")

	####################### Lenovo Model 3 #######################
	#Lenovo - Yoga C940 2-in-1 14" 4K Ultra HD Touch-Screen Laptop - Intel Core i7 - 16GB Memory - 512GB SSD + 32GB Optane - Best Buy
	lenovo_bestbuyURL3 = 'https://www.bestbuy.com/site/lenovo-yoga-c940-2-in-1-14-4k-ultra-hd-touch-screen-laptop-intel-core-i7-16gb-memory-512gb-ssd-32gb-optane-mica/6369421.p?skuId=6369421'
	ps.scrape_laptops(lenovo_bestbuyURL3, "bestbuy")

	#Lenovo - Yoga C940 2-in-1 14" 4K Ultra HD Touch-Screen Laptop - Intel Core i7 - 16GB Memory - 512GB SSD + 32GB Optane - Walmart 
	lenovo_walmartURL3 = 'https://www.walmart.com/ip/Lenovo-Yoga-C940-2-in-1-14-4K-Ultra-HD-Touch-Screen-Laptop-Intel-Core-i7-16GB-Memory-512GB-SSD-Mica-81Q90041US-Tablet-PC-Computer/176404113'
	ps.scrape_laptops(lenovo_walmartURL3, "walmart")

	#Lenovo - Yoga C940 2-in-1 14" 4K Ultra HD Touch-Screen Laptop - Intel Core i7 - 16GB Memory - 512GB SSD + 32GB Optane - Newegg
	lenovo_neweggURL3 = 'https://www.newegg.com/p/1TS-000E-0F9D6?Description=81Q90041US&cm_re=81Q90041US-_-9SIA8X5AGB9160-_-Product&quicklink=true'
	ps.scrape_laptops(lenovo_neweggURL3, "newegg")

	#Lenovo - Yoga C940 2-in-1 14" 4K Ultra HD Touch-Screen Laptop - Intel Core i7 - 16GB Memory - 512GB SSD + 32GB Optane - Amazon
	lenovo_amazonURL3 = 'https://www.amazon.com/Lenovo-Yoga-C940-14-Touch-i7-1065G7-12GB/dp/B08121VSGZ/ref=sr_1_1?crid=282QAW572V8YS&dchild=1&keywords=lenovo+81q90041us&qid=1586922449&sprefix=81q900%2Caps%2C162&sr=8-1'
	ps.scrape_laptops(lenovo_amazonURL3, "amazon")

	####################### Lenovo Model 4 #######################
	#Lenovo - Yoga C740 2-in-1 14" Touch-Screen Laptop - Intel Core i5 - 8GB Memory - 256GB Solid State Drive - Best Buy
	lenovo_bestbuyURL4 = 'https://www.bestbuy.com/site/lenovo-yoga-c740-2-in-1-14-touch-screen-laptop-intel-core-i5-8gb-memory-256gb-solid-state-drive-mica/6367805.p?skuId=6367805'
	ps.scrape_laptops(lenovo_bestbuyURL4, "bestbuy")

	#Lenovo - Yoga C740 2-in-1 14" Touch-Screen Laptop - Intel Core i5 - 8GB Memory - 256GB Solid State Drive - Walmart
	lenovo_walmartURL4 = 'https://www.walmart.com/ip/Lenovo-Yoga-C740-2-in-1-14-Touch-Screen-Laptop-Intel-Core-i5-8GB-Memory-256GB-Solid-State-Drive-Mica-81TC000JUS-Tablet-Notebook/526394392'
	ps.scrape_laptops(lenovo_walmartURL4, "walmart")

	#Lenovo - Yoga C740 2-in-1 14" Touch-Screen Laptop - Intel Core i5 - 8GB Memory - 256GB Solid State Drive - Newegg
	lenovo_neweggURL4 = 'https://www.newegg.com/p/1TS-000E-0FNN8?Description=81TC000JUS&cm_re=81TC000JUS-_-9SIA8X5APT2293-_-Product'
	ps.scrape_laptops(lenovo_neweggURL4, "newegg")

	#Lenovo - Yoga C740 2-in-1 14" Touch-Screen Laptop - Intel Core i5 - 8GB Memory - 256GB Solid State Drive - Amazon
	lenovo_amazonURL4 = 'https://www.amazon.com/Lenovo-Yoga-C740-14-FHD-Touch/dp/B08122HHX9/ref=sr_1_4?dchild=1&m=AD7Y6TQ6313D1&marketplaceID=ATVPDKIKX0DER&qid=1586923041&refinements=p_4%3ALenovo&s=merchant-items&sr=1-4'
	ps.scrape_laptops(lenovo_amazonURL4, "amazon")


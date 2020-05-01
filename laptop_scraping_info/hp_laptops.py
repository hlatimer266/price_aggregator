import price_scraper as ps 

if __name__ == "__main__":

	####################### HP Model 1 #######################
	#HP - 15.6" Gaming Laptop - AMD Ryzen 5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Best Buy
	hp_bestbuyURL = 'https://www.bestbuy.com/site/hp-15-6-gaming-laptop-amd-ryzen-5-8gb-memory-nvidia-geforce-gtx-1050-256gb-solid-state-drive-shadow-black/6364574.p?skuId=6364574'
	ps.scrape_laptops(hp_bestbuyURL, "bestbuy")

	#HP - 15.6" Gaming Laptop - AMD Ryzen 5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Walmart
	hp_walmartURL = 'https://www.walmart.com/ip/Laptop-NVIDIA-15-EC0013DX-Memory-HP-Shadow-GTX-Solid-GeForce-Black-8GB-AMD-Drive-Chrome-Finish-Ryzen-Notebook-Paint-1050-Green-5-State-256GB-15-6-Gam/846313398'
	ps.scrape_laptops(hp_walmartURL, "walmart")

	#HP - 15.6" Gaming Laptop - AMD Ryzen 5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Newegg
	hp_neweggURL = 'https://www.newegg.com/p/N82E16834271325?Description=hp%20gaming%20laptop&cm_re=hp_gaming_laptop-_-34-271-325-_-Product'
	ps.scrape_laptops(hp_neweggURL, "newegg")

	#HP - 15.6" Gaming Laptop - AMD Ryzen 5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Amazon
	hp_amazonURL = 'https://www.amazon.com/HP-Gaming-15-EC0013DX-NVIDIA-1050-8GB/dp/B08121CLYZ/ref=sr_1_5?dchild=1&m=A281V1RURT86E2&marketplaceID=ATVPDKIKX0DER&qid=1587467020&refinements=p_4%3AHP&s=merchant-items&sr=1-5'
	ps.scrape_laptops(hp_amazonURL, "amazon")

	####################### HP Model 2 #######################
	#HP - Pavilion x360 2-in-1 11.6" Touch-Screen Laptop - Intel Pentium - 4GB Memory - 128GB Solid State Drive - Best Buy
	hp_bestbuyURL2 = 'https://www.bestbuy.com/site/hp-pavilion-x360-2-in-1-11-6-touch-screen-laptop-intel-pentium-4gb-memory-128gb-solid-state-drive-ash-silver/6339311.p?skuId=6339311'
	ps.scrape_laptops(hp_bestbuyURL2, "bestbuy")

	#HP - Pavilion x360 2-in-1 11.6" Touch-Screen Laptop - Intel Pentium - 4GB Memory - 128GB Solid State Drive - Walmart 
	hp_walmartURL2 = 'https://www.walmart.com/ip/Laptop-x360-Touch-Screen-Memory-HP-Natural-Intel-Solid-4GB-Pavilion-Pentium-Ash-128GB-Frame-Computer-Drive-Tablet-Notebook-Keyboard-11M-AP0013DX-Silv/972520836'
	ps.scrape_laptops(hp_walmartURL2, "walmart")

	#HP - Pavilion x360 2-in-1 11.6" Touch-Screen Laptop - Intel Pentium - 4GB Memory - 128GB Solid State Drive - Newegg
	hp_neweggURL2 = 'https://www.newegg.com/p/1TS-006W-00078?Description=11M-AP0013DX&cm_re=11M-AP0013DX-_-9SIA8X59XB1269-_-Product&quicklink=true'
	ps.scrape_laptops(hp_neweggURL2, "newegg")

	#HP - Pavilion x360 2-in-1 11.6" Touch-Screen Laptop - Intel Pentium - 4GB Memory - 128GB Solid State Drive - Amazon
	hp_amazonURL2 = 'https://www.amazon.com/HP-Pavilion-2-1-Touch-Screen/dp/B07QRZJRKK/ref=sr_1_18?dchild=1&m=A29KLQP7IUULC5&marketplaceID=ATVPDKIKX0DER&qid=1586923893&refinements=p_4%3AHP&s=merchant-items&sr=1-18'
	ps.scrape_laptops(hp_amazonURL2, "amazon")

	####################### HP Model 3 #######################
	#HP - 14" Laptop - AMD A9-Series - 4GB Memory - AMD Radeon R5 Graphics - 128GB Solid State Drive - Best Buy
	hp_bestbuyURL3 = 'https://www.bestbuy.com/site/hp-14-laptop-amd-a9-series-4gb-memory-amd-radeon-r5-graphics-128gb-solid-state-drive-ash-silver/6352587.p?skuId=6352587'
	ps.scrape_laptops(hp_bestbuyURL3, "bestbuy")

	#HP - 14" Laptop - AMD A9-Series - 4GB Memory - AMD Radeon R5 Graphics - 128GB Solid State Drive - Walmart
	hp_walmartURL3 = 'https://www.walmart.com/ip/HP-14-Laptop-AMD-A9-Series-4GB-Memory-AMD-Radeon-R5-128GB-Solid-State-Drive-Ash-Silver-Keyboard-Frame-Natural-Silver/453344142'
	ps.scrape_laptops(hp_walmartURL3, "walmart")

	#HP - 14" Laptop - AMD A9-Series - 4GB Memory - AMD Radeon R5 Graphics - 128GB Solid State Drive - Newegg
	hp_neweggURL3 = 'https://www.newegg.com/p/1TS-000D-09DD4?Description=14-DK0002DX&cm_re=14-DK0002DX-_-1TS-000D-09DD4-_-Product&quicklink=true'
	ps.scrape_laptops(hp_neweggURL3, "newegg")

	#HP - 14" Laptop - AMD A9-Series - 4GB Memory - AMD Radeon R5 Graphics - 128GB Solid State Drive - Amazon
	hp_amazonURL3 = 'https://www.amazon.com/HP-14-14-dk0002dx-Display-Bluetooth/dp/B086BSVVBD/ref=sr_1_12?dchild=1&m=A1OH90MA4UKR9I&marketplaceID=ATVPDKIKX0DER&qid=1587467121&s=merchant-items&sr=1-12'
	ps.scrape_laptops(hp_amazonURL3, "amazon")

	####################### HP Model 4 #######################
	#HP - 2-in-1 14" Touch-Screen Chromebook - Intel Core i3 - 8GB Memory - 64GB eMMC Flash Memory - Best Buy
	hp_bestbuyURL4 = 'https://www.bestbuy.com/site/hp-2-in-1-14-touch-screen-chromebook-intel-core-i3-8gb-memory-64gb-emmc-flash-memory-white/6365772.p?skuId=6365772'
	ps.scrape_laptops(hp_bestbuyURL4, "bestbuy")

	#HP - 2-in-1 14" Touch-Screen Chromebook - Intel Core i3 - 8GB Memory - 64GB eMMC Flash Memory - Walmart
	hp_walmartURL4 = 'https://www.walmart.com/ip/HP-2-in-1-14-Full-HD-Touchscreen-Chromebook-x360-Core-i3-8130U-8GB-RAM-64GB-eMMC/814497767'
	ps.scrape_laptops(hp_walmartURL4, "walmart")

	#HP - 2-in-1 14" Touch-Screen Chromebook - Intel Core i3 - 8GB Memory - 64GB eMMC Flash Memory - Newegg
	hp_neweggURL4 = 'https://www.newegg.com/hp-chromebook-x360/p/2S3-0002-001U7?Description=14-DA0012DX&cm_re=14-DA0012DX-_-2S3-0002-001U7-_-Product'
	ps.scrape_laptops(hp_neweggURL4, "newegg")

	#HP - 2-in-1 14" Touch-Screen Chromebook - Intel Core i3 - 8GB Memory - 64GB eMMC Flash Memory - Amazon
	hp_amazonURL4 = 'https://www.amazon.com/HP-Chromebook-14-db0023dx-A4-9120C-R4-32GB/dp/B07NCN1S21/ref=sr_1_6?dchild=1&m=A18RSW2ZEV166G&marketplaceID=ATVPDKIKX0DER&qid=1587467333&refinements=p_4%3AHP&s=merchant-items&sr=1-6'
	ps.scrape_laptops(hp_amazonURL4, "amazon")




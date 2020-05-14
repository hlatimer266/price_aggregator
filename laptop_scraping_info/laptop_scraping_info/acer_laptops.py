import price_scraper as ps 

if __name__ == "__main__":
	
	####################### Acer Model 1: AN515-54-54W2 #######################
	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Ebay
	acer_ebayURL = 'https://www.ebay.com/itm/Acer-Nitro-5-AN515-54-54W2-15-6-FHD-i5-9300H-NVIDIA-GTX-1050-8GB-256GB/324069933663?epid=5034604525&hash=item4b7412c25f:g:~RsAAOSwOiReleF8'
	ps.scrape_laptops(acer_ebayURL, "ebay")

	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Walmart
	acer_walmartURL = 'https://www.walmart.com/ip/Acer-Nitro-5-15-6-Gaming-Laptop-Intel-Core-i5-8GB-Memory-NVIDIA-GeForce-GTX-1050-256GB-Solid-State-Drive-Black/720273480'
	ps.scrape_laptops(acer_walmartURL,"walmart")

	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - Newegg
	acer_neweggURL = 'https://www.newegg.com/p/1TS-000X-01DF5?Description=AN515-54-54W2&cm_re=AN515-54-54W2-_-1TS-000X-01DF5-_-Product'
	ps.scrape_laptops(acer_neweggURL,"newegg")


	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1050 - 256GB Solid State Drive - BHPhoto
	acer_BHPhotoURL = 'https://www.bhphotovideo.com/c/product/1485583-REG/acer_nh_q5faa_003_nitro_7_i7_9750h_8gb.html'
	ps.scrape_laptops(acer_BHPhotoURL, "bhphotovideo")
	
	####################### Acer Model 2 CP315-1H-P8QY #######################
	#Acer - Spin 15 2-in-1 15.6" Touch-Screen Chromebook - Intel Pentium - 4GB Memory - 32GB eMMC Flash Memory - Ebay
	acer_ebayURL2 = 'https://www.ebay.com/itm/Acer-Chromebook-Spin-15-Cp315-1h-p8qy-15-6-Touchscreen-Lcd-2-In-1-Chromebook/233550998121?epid=23024821936&hash=item3660b96a69:g:f3cAAOSwK05el5Ov'
	ps.scrape_laptops(acer_ebayURL2, "ebay")

	#Acer - Spin 15 2-in-1 15.6" Touch-Screen Chromebook - Intel Pentium - 4GB Memory - 32GB eMMC Flash Memory - Walmart
	acer_walmartURL2 = 'https://www.walmart.com/ip/1080-Spin-Memory-In-p-Intel-Pentium-CP315-1H-P8QY-Chrome-Sparkly-GB-Flash-Chromebook-32-Touchscreen-15-OS-N4200-Acer-Graphics-1-1920-Silver-2-4-x-505/992776713'
	ps.scrape_laptops(acer_walmartURL2, "walmart")

	#Acer - Spin 15 2-in-1 15.6" Touch-Screen Chromebook - Intel Pentium - 4GB Memory - 32GB eMMC Flash Memory - Newegg
	acer_neweggURL2 = 'https://www.newegg.com/p/1TS-000X-01ZM4?Description=CP315-1H-P8QY&cm_re=CP315-1H-P8QY-_-1TS-000X-01ZM4-_-Product&quicklink=true'
	ps.scrape_laptops(acer_neweggURL2, "newegg")

	#Acer - Spin 15 2-in-1 15.6" Touch-Screen Chromebook - Intel Pentium - 4GB Memory - 32GB eMMC Flash Memory - BHPhoto
	acer_BHPhotoURL2 = "https://www.bhphotovideo.com/c/product/1513058-REG/acer_nx_gzraa_011_spin_3_2_in_1_i3_8130u.html"
	ps.scrape_laptops(acer_BHPhotoURL2, "bhphotovideo")
	

	####################### Acer Model 3 AN515-54-51M5 #######################
	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 1TB Hard Drive + 128GB SSD - Ebay
	acer_ebayURL3 = 'https://www.ebay.com/itm/NEW-Acer-Gaming-Laptop-AN515-54-51M5-GTX-1650-1TB-HD-128GB-SSD-i5-8GB-Notebook/373026210498?epid=2306090875&hash=item56da1842c2:g:y1EAAOSwXwtc9BPQ'
	ps.scrape_laptops(acer_ebayURL3, "ebay")
	

	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 1TB Hard Drive + 128GB SSD - Walmart
	acer_walmartURL3 = 'https://www.walmart.com/ip/Laptop-NVIDIA-Memory-GTX-Black-Intel-Solid-GeForce-8GB-AN515-54-51M5-1650-128GB-Computer-Drive-Core-1TB-Obs-Notebook-Hard-i5-Acer-PC-State-Gaming/198385755'
	ps.scrape_laptops(acer_walmartURL3, "walmart")

	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 1TB Hard Drive + 128GB SSD - Newegg
	acer_neweggURL3 = 'https://www.newegg.com/obsidian-black-acer-nitro-7-an715-51-73bu-gaming-entertainment/p/N82E16834316724?Description=acer%20nitro&cm_re=acer_nitro-_-34-316-724-_-Product&quicklink=true'
	ps.scrape_laptops(acer_neweggURL3, "newegg")

	#Acer - Nitro 5 15.6" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 1TB Hard Drive + 128GB SSD - ShopDevicesNow
	acer_sdnURL = 'https://www.shopdevicesnow.com/products/acer-nitro-5-15-6-gaming-laptop-intel-i5?_pos=5&_sid=89adee782&_ss=r'
	ps.scrape_laptops(acer_sdnURL, "shopdevicesnow")
	
	
	####################### Acer Model 4 AN517-51-56YW #######################
	#Acer - Nitro 5 17.3" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 512GB Solid State Drive - Ebay
	acer_ebayURL4 = 'https://www.ebay.com/itm/Nitro-5-17-3-HD-Full-17-3-inches-8GB-GTX-1650-Black-1920-x-1080-Full-HD-W10H/303559001579?hash=item46ad86c5eb:g:ragAAOSwwW9etEJf'
	ps.scrape_laptops(acer_ebayURL4, "ebay")

	#Acer - Nitro 5 17.3" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 512GB Solid State Drive - Walmart
	acer_walmartURL4 = 'https://www.walmart.com/ip/Laptop-NVIDIA-Memory-Nitro-GTX-Black-Intel-Solid-GeForce-8GB-1650-Computer-Drive-17-3-Core-AN517-51-56YW-Notebook-Obsidian-i5-Acer-512GB-PC-5-State-G/409426147'
	ps.scrape_laptops(acer_walmartURL4, "walmart")

	#Acer - Nitro 5 17.3" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 512GB Solid State Drive - Newegg
	acer_neweggURL4 = 'https://www.newegg.com/p/1TS-000X-00ZJ4?Description=AN517-51-56YW&cm_re=AN517-51-56YW-_-1TS-000X-00ZJ4-_-Product'
	ps.scrape_laptops(acer_neweggURL4, "newegg")

	#Acer - Nitro 5 17.3" Gaming Laptop - Intel Core i5 - 8GB Memory - NVIDIA GeForce GTX 1650 - 512GB Solid State Drive - ShopDevicesNow
	acer_sdnURL2 = 'https://www.shopdevicesnow.com/products/acer-nitro-5-gaming-laptop?_pos=4&_sid=89adee782&_ss=r'
	ps.scrape_laptops(acer_sdnURL2, "shopdevicesnow")
	




import price_scraper as ps

if __name__ == "__main__":
    
    ####################### Acer Model 1 #######################
    # Acer® V206HQL 19.5" LED Monitor - Office Depot
    office_depot_html = 'unified_price_row unified_sale_price red_price'
    office_depot_url = 'https://www.officedepot.com/a/products/375238/Acer-V206HQL-195-LED-Monitor/?cm_mmc=PLA-_-Google-_-Monitors-_-375238&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHhO1cFldQuxELmmmDsBp3QKLHfTFUZ3GaOw5WfXeInB3GepUSy7nKRoCT1kQAvD_BwE&gclsrc=aw.ds'
    # ps.scrape_monitors(office_depot_url,office_depot_html,"office_depot")

    # Acer® V206HQL 19.5" LED Monitor - Walmart
    walmart_html_tag_acer = 'price-characteristic'
    walmart_url_acer = 'https://www.walmart.com/ip/TCO-Black-II-MPR-Monitor-W-Million-19-5-ms-V206HQL-LED-LCD-16-20-Adjustable-HD-Acer-VGA-1600-200-16-9-Colors-Angle-5-DVI-x-Nit-900-16-7-Display/954645118?wmlspartner=wlpa&selectedSellerId=1198&adid=22222222227089383363&wl0=&wl1=g&wl2=c&wl3=202825840059&wl4=aud-430887228898:pla-328333851253&wl5=9032917&wl6=&wl7=&wl8=&wl9=pla&wl10=112561793&wl11=online&wl12=954645118&veh=sem&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHgNz1O8YkvfJYMdF0KwNTdLwSiCuzGJJgR2j-6UIXwQT1QqjE7Bq5hoCxeoQAvD_BwE'
    # ps.scrape_monitors(walmart_url_acer,walmart_html_tag_acer,"walmart")

    # Acer® V206HQL 19.5" LED Monitor - Monoprice
    monoprice_url_acer = 'https://www.monoprice.com/product?p_id=18020&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHl-LysFrdKwjBOBAa0AC5Pgj40jtDf6aD-WAM8WZInEnJI86FRe29RoCpBcQAvD_BwE'
    monoprice_tag_acer = 'sale-price'
    # ps.scrape_monitors(monoprice_url_acer,monoprice_tag_acer,"monoprice")

    # Acer® V206HQL 19.5" LED Monitor - ebay
    ebay_url_acer = 'https://www.ebay.com/p/691182356?iid=274006906214&chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=274006906214&targetid=884108885999&device=c&mktype=pla&googleloc=9032917&poi=&campaignid=9423618396&mkgroupid=95235844226&rlsatarget=pla-884108885999&abcId=1141016&merchantid=6296724&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHoJMPFE8zHTwgaPC1SYMtwVfrphPD0qF9ZqZ-zRhd26tw36KZY1PqRoC7vUQAvD_BwE'
    ebay_tag = 'display-price'
    # ps.scrape_monitors(ebay_url_acer,ebay_tag,"ebay")
    ############################################################

    ####################### Acer Model 2 #######################
    #Acer V226HQL 21.5" LED LCD Monitor - Walmart
    walmart_url_acer2 = "https://www.walmart.com/ip/1080-V226HQL-18-10-21-5-Black-Full-MPR-Monitor-W-EPEAT-Million-II-ms-LED-LCD-Adjustable-Acer-Gold-1920-VGA-200-16-9-Colors-Angle-5-DVI-x-Nit-16-7-HD-/186710983?wmlspartner=wlpa&selectedSellerId=3937&adid=22222222227040758114&wl0=&wl1=g&wl2=c&wl3=100279120234&wl4=aud-430887228898:pla-238137513874&wl5=9032917&wl6=&wl7=&wl8=&wl9=pla&wl10=113537325&wl11=online&wl12=186710983&veh=sem&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHoMd_sIKHjme1zxkgKhVPq1gE64HYht-E1rX7sLiTqPgWdkJ5baEtBoC034QAvD_BwE"
    # ps.scrape_monitors(walmart_url_acer2,walmart_html_tag_acer,"walmart")
    # time.sleep(2)

    #Acer V226HQL 21.5" LED LCD Monitor - Office Depot
    office_depot_url2 = "https://www.officedepot.com/a/products/956021/Acer-V226HQL-215-FHD-LED-Monitor/?cm_mmc=PLA-_-Google-_-Monitors-_-956021&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHn9pAacx6-zicQRgKqU22QtVhRMSHphqfJd69eAh3XLOAjePXHjyvBoClocQAvD_BwE&gclsrc=aw.ds"
    # ps.scrape_monitors(office_depot_url2, office_depot_html, "office_depot")
    # time.sleep(2)

    #Acer V226HQL 21.5" LED LCD Monitor - Monoprice
    monoprice_url_acer2 = "https://www.monoprice.com/product?p_id=18037&gclid=CjwKCAjw1cX0BRBmEiwAy9tKHoX-Rmk4FG1PNgMgSXJiEmy8SC0_Y99vABCv5yQvisCRWpW9aPiYXhoCscgQAvD_BwE"
    # ps.scrape_monitors(monoprice_url_acer2,monoprice_tag_acer,"monoprice")
    # time.sleep(2)

    #Acer V226HQL 21.5" LED LCD Monitor - ebay
    ebay_url_acer2 = "https://www.ebay.com/p/168468671?iid=323924539140&chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=323924539140&targetid=884108885999&device=c&mktype=pla&googleloc=9032917&poi=&campaignid=9423618396&mkgroupid=95235844226&rlsatarget=pla-884108885999&abcId=1141016&merchantid=6296724&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbedBnw19txgXETV8xeuz_ZVVVZ3aHZp3EJ7AtzBACmutueX_Z0zSCmEaAt3EEALw_wcB&thm=1000"
    # ps.scrape_monitors(ebay_url_acer2, ebay_tag, "ebay")
    ############################################################

    ####################### Acer Model 3 #######################
    #Acer® V246HQL 23.6" FHD LED Monitor - Office Depot
    office_depot_url3 = "https://www.officedepot.com/a/products/956109/Acer-V246HQL-236-FHD-LED-Monitor/?cm_mmc=PLA-_-Google-_-Monitors-_-956109&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbeeFM4Rv-Rqvv4fJxc4aDenpt9H7DX-RoF2SvKsXFqPFoQrhptzTjG8aAoiJEALw_wcB&gclsrc=aw.ds"
    # ps.scrape_monitors(office_depot_url3,office_depot_html,"office_depot")
    # time.sleep(2)

    #Acer® V246HQL 23.6" FHD LED Monitor - Walmart
    walmart_url_acer3 = "https://www.walmart.com/ip/Acer-23-6-V246HQL-bi-16-9-VA-Monitor/525967764?wmlspartner=wlpa&selectedSellerId=638&adid=22222222227342227663&wl0=&wl1=g&wl2=c&wl3=431038832366&wl4=aud-430887228898:pla-897919119011&wl5=9032917&wl6=&wl7=&wl8=&wl9=pla&wl10=112343685&wl11=online&wl12=525967764&veh=sem&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbeeADzl5wC-zSrYQd6SfeIQIN18jbh71ZZViHnakzruEFvCI22hjOFAaAtcREALw_wcB"
    # ps.scrape_monitors(walmart_url_acer3,walmart_html_tag_acer,"walmart")
    # time.sleep(2)

    #Acer® V246HQL 23.6" FHD LED Monitor - monoprice
    monoprice_url_acer3 = "https://www.monoprice.com/product?p_id=22031&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbeeTwhrv_4i-n4f1sX2cl2gbJKleiyU0c68jAxNnI1ln6_ePujam8uwaAvdwEALw_wcB"
    # ps.scrape_monitors(monoprice_url_acer3, monoprice_tag_acer, "monoprice")
    # time.sleep(2)

    #Acer® V246HQL 23.6" FHD LED Monitor - ebay
    ebay_url_acer3 = "https://www.ebay.com/p/2164330904?iid=143552941629&chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=143552941629&targetid=884131384999&device=c&mktype=pla&googleloc=9032917&poi=&campaignid=9421872431&mkgroupid=95112701945&rlsatarget=pla-884131384999&abcId=1140476&merchantid=6303084&gclid=Cj0KCQjw-Mr0BRDyARIsAKEFbedIsH7WWb9s2ArM4A1MgQDFQ56VYB-Oy8bN1jlymgC3a3xlVwBhB0kaAlN2EALw_wcB&thm=1000"
    # ps.scrape_monitors(ebay_url_acer3, ebay_tag, "ebay")
    ############################################################

    ####################### Acer Model 4 #######################
    #Acer B206HQL - Office Depot
    office_depot_url4 = "https://www.officedepot.com/a/products/688125/Acer-B6-195-Widescreen-LED-LCD/"
    # ps.scrape_monitors(office_depot_url4, office_depot_html, "office_depot")

    #Acer B206HQL - Walmart
    walmart_url_acer4 = "https://www.walmart.com/ip/Refurbished-Acer-19-5-Widescreen-LCD-Monitor-Display-Full-HD-1920-x-1080-8-ms-60-Hz-B206HQL/691509306"
    # ps.scrape_monitors(walmart_url_acer4, walmart_html_tag_acer, "walmart")

    #Acer B206HQL - monoprice
    monoprice_url_acer4 = "https://www.monoprice.com/product?p_id=20193"
    # ps.scrape_monitors(monoprice_url_acer4, monoprice_tag_acer, "monoprice")

    #Acer B206HQL - ebay
    ebay_url_acer4 = "https://www.ebay.com/p/1951179521"
    # ps.scrape_monitors(ebay_url_acer4, ebay_tag, "ebay")
    ############################################################

    ####################### Acer Model 5 #######################
    # Acer Acer® B226WL - Office Depot
    office_depot_url5 = "https://www.officedepot.com/a/products/179614/Acer-B226WL-22-LED-LCD-Monitor/"
    ps.scrape_monitors(office_depot_url5, office_depot_html, "office_depot")

    # Acer Acer® B226WL - Walmart
    walmart_url_acer5 = "https://www.walmart.com/ip/1680-Black-250-Monitor-W-100-000-000-1-Million-16-10-22-WSXGA-ms-LED-Speakers-LCD-Adjustable-1050-Acer-B226WL-VGA-24-20-Colors-Angle-5-DVI-x-Nit-16-7/104495078"
    ps.scrape_monitors(walmart_url_acer5, walmart_html_tag_acer, "walmart")

    # Acer Acer® B226WL - monoprice
    monoprice_url_acer5 = "https://www.monoprice.com/product?p_id=17996"
    ps.scrape_monitors(monoprice_url_acer5, monoprice_tag_acer, "monoprice")

    # Acer Acer® B226WL - ebay
    ebay_url_acer5 = "https://www.ebay.com/p/168538047"
    ps.scrape_monitors(ebay_url_acer5, ebay_tag, "ebay")

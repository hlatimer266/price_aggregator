import price_scraper as ps

if __name__ == "__main__":
    ####################### Asus Model 1 #######################
    # ASUS VE278Q 27" in - Office Depot
    od_asus_url_1 = "https://www.officedepot.com/a/products/860316/Asus-VE278Q-27-HD-LED-LCD/"
    od_asus_html_tag = "unified_price_row unified_sale_price red_price"
    # ps.scrape_monitors(od_asus_url_1,od_asus_html_tag,"office_depot")

    # ASUS VE278Q 27" in - Walmart
    wl_asus_url_1 = "https://www.walmart.com/ip/Asus-VE278QB-VE278Q-27-Full-HD-LED-Monitor-w-Integrated-Speakers/15421269?wmlspartner=wlpa&selectedSellerId=1912&adid=22222222227000000000&wl0=&wl1=g&wl2=c&wl3=42423897272&wl4=aud-430887228898:pla-51320962143&wl5=9032917&wl6=&wl7=&wl8=&wl9=pla&wl10=112549731&wl11=online&wl12=15421269&veh=sem&gclid=Cj0KCQjwm9D0BRCMARIsAIfvfIZYGqKndmAeviEdTC-PqLDWvSDPxvcn4_kd8kGaRBux4Jv7t5C4-hUaAjKAEALw_wcB"
    wl_asus_html_tag = "price-characteristic"
    # ps.scrape_monitors(wl_asus_url_1, wl_asus_html_tag, "walmart")

    # ASUS VE278Q 27" in - Monoprice
    mn_asus_url_1 = "https://www.monoprice.com/product?p_id=17124"
    mn_asus_html_tag = "sale-price"
    # ps.scrape_monitors(mn_asus_url_1, mn_asus_html_tag, "monoprice")

    # ASUS VE278Q 27" in - ebay
    eb_asus_url_1 = "https://www.ebay.com/p/108868668"
    eb_asus_html_tag = "display-price"
    # ps.scrape_monitors(eb_asus_url_1, eb_asus_html_tag, "ebay")

    ############################################################

    ####################### Asus Model 2 #######################

    # Asus VW22AT-CSM 22" - Office Depot
    od_asus_url_2 = "https://www.officedepot.com/a/products/376552/Asus-VW22AT-22-LED-LCD-Monitor/"
    # ps.scrape_monitors(od_asus_url_2,od_asus_html_tag,"office_depot")

    # Asus VW22AT-CSM 22" - Walmart
    wl_asus_url_2 = "https://www.walmart.com/ip/VW22AT-CSM-ErP-1680-50-000-000-1-Black-250-Monitor-W-Million-16-10-33-J-Moss-22-WSXGA-ms-LED-Speakers-LCD-Adjustable-1050-Asus-VGA-Colors-Angle-5-DVI/150810923"
    # ps.scrape_monitors(wl_asus_url_2, wl_asus_html_tag, "walmart")

    # Asus VW22AT-CSM 22" - monoprice
    mn_asus_url_2 = "https://www.monoprice.com/product?p_id=17155"
    # ps.scrape_monitors(mn_asus_url_2, mn_asus_html_tag, "monoprice")

    # Asus VW22AT-CSM 22" - ebay
    eb_asus_url_2 = "https://www.ebay.com/i/173874066392?chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&itemid=173874066392&targetid=884131384999&device=c&mktype=pla&googleloc=9032917&poi=&campaignid=9421872431&mkgroupid=95112701945&rlsatarget=pla-884131384999&abcId=1140476&merchantid=8543194&gclid=Cj0KCQjwm9D0BRCMARIsAIfvfIYo1JD9LLDgyt2V8dp5fJaIBUIsrAsRejHEBjP7CiYSJqAMxb0ewloaAgyAEALw_wcB"
    # ps.scrape_monitors(eb_asus_url_2, eb_asus_html_tag, "ebay")

    ############################################################

    ####################### Asus Model 3 #######################
    # Asus PB238Q 23" FHD LED Monitor - Office Depot
    od_asus_url_3 = "https://www.officedepot.com/a/products/771172/Asus-PB238Q-23-FHD-LED-Monitor/"
    # ps.scrape_monitors(od_asus_url_3, od_asus_html_tag, "office_depot")

    # Asus PB238Q 23" FHD LED Monitor - Walmart
    wl_asus_url_3 = "https://www.walmart.com/ip/1080-23-250-Full-80-000-000-1-Monitor-Blac-DisplayPort-Million-USB-ms-LED-Speakers-LCD-Adjustable-Asus-PB238Q-1920-VGA-16-9-Colors-Angle-6-DVI-x-Nit-/134083436"
    # ps.scrape_monitors(wl_asus_url_3, wl_asus_html_tag, "walmart")

    # Asus PB238Q 23" FHD LED Monitor - monoprice
    mn_asus_url_3 = "https://www.monoprice.com/product?p_id=17131"
    # ps.scrape_monitors(mn_asus_url_3, mn_asus_html_tag, "monoprice")

    # Asus PB238Q 23" FHD LED Monitor - ebay
    eb_asus_url_3 = "https://www.ebay.com/p/141640981"
    # ps.scrape_monitors(eb_asus_url_3, eb_asus_html_tag, "ebay")

    ############################################################

    ####################### Asus Model 4 #######################

    # Asus ASUS VP228HE - walmart
    wl_asus_url_4 = "https://www.walmart.com/ip/ASUS-21-5-Eye-Care-Gaming-Monitor-Black/325413799"
    # ps.scrape_monitors(wl_asus_url_4, wl_asus_html_tag, "walmart")

    # Asus ASUS VP228HE - cdw
    cdw_asus_url_1 = "https://www.cdw.com/product/asus-vp228he-led-monitor-full-hd-1080p-21.5/5570696?enkwrd=asus+vp228he+-"
    cdw_asus_html_tag = "price-type-selected"
    # ps.scrape_monitors(cdw_asus_url_1, cdw_asus_html_tag, "cdw")

    # Asus ASUS VP228HE - b&h
    bh_asus_url_1 = "https://www.bhphotovideo.com/c/product/1501079-REG/asus_vp228he_21_5_full_hd.html?sts=pi&pim=Y"
    bh_asus_html_tag = "price_1DPoToKrLP8uWvruGqgtaY"
    # ps.scrape_monitors(bh_asus_url_1, bh_asus_html_tag, "bh")

    # Asus ASUS VP228HE - ebay
    eb_asus_url_4 = "https://www.ebay.com/p/18026119240"
    # ps.scrape_monitors(eb_asus_url_4, eb_asus_html_tag, "ebay")

    ############################################################

    ####################### Asus Model 5 #######################
    # ASUS VG275Q - walmart
    wl_asus_url_5 = "https://www.walmart.com/ip/ASUS-27-Eye-Care-Console-Gaming-Monitor-Black/676634760"
    ps.scrape_monitors(wl_asus_url_5, wl_asus_html_tag, "walmart")

    # ASUS VG275Q - cdw
    cdw_asus_url_2 = "https://www.cdw.com/product/asus-vg275q-led-monitor-full-hd-1080p-27/4685353?enkwrd=asus+vg275q+-"
    ps.scrape_monitors(cdw_asus_url_2, cdw_asus_html_tag, "cdw")

    # ASUS VG275Q - B&H
    bh_asus_url_2 = "https://www.bhphotovideo.com/c/product/1345675-REG/asus_vg275q_27_full_hd.html"
    ps.scrape_monitors(bh_asus_url_2, bh_asus_html_tag, "bh")

    # ASUS VG275Q - ebay
    eb_asus_url_5 = "https://www.ebay.com/p/18004877746"
    ps.scrape_monitors(eb_asus_url_5, eb_asus_html_tag, "ebay")
    ############################################################



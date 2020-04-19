import price_scraper as ps

if __name__ == "__main__":
    ####################### HP Model 1 #######################
    # HP Z27 - walmart
    wl_url_1 = "https://www.walmart.com/ip/HP-Z27-27-inch-4K-UHD-Display/834276976"
    wl_html_tag = "price-characteristic"
    ps.scrape_monitors(wl_url_1, wl_html_tag, "walmart")

    # HP Z27 - cdw
    cdw_url_1 = "https://www.cdw.com/product/hp-z27-led-monitor-27-smart-buy/5066186"
    cdw_html_tag = "price-type-selected"
    ps.scrape_monitors(cdw_url_1, cdw_html_tag, "cdw")

    # HP Z27 - b&h
    bh_url_1 = "https://www.bhphotovideo.com/c/product/1410166-REG/hp_2tb68a8_aba_hp_z27_27_4k.html?sts=pi&pim=Y"
    bh_html_tag = "price_1DPoToKrLP8uWvruGqgtaY"
    ps.scrape_monitors(bh_url_1, bh_html_tag, "bh")

    # HP Z27 - ebay 
    eb_url_1 = "https://www.ebay.com/p/28019412809"
    eb_html_tag = "display-price"
    ps.scrape_monitors(eb_url_1, eb_html_tag, "ebay")
    ##########################################################

    ####################### HP Model 2 #######################

    # # HP N223 - walmart
    # wl_url_2 = "https://www.walmart.com/ip/HP-22-1920x1080-DVI-HDMI-VGA-USB-60hz-5ms-HD-LED-LCD-Monitor-N223/762585034"
    # ps.scrape_monitors(wl_url_2, wl_html_tag, "walmart")

    # # HP N223 - cdw
    # cdw_url_2 = "https://www.cdw.com/product/hp-n223-led-monitor-full-hd-1080p-21.5/5022228"
    # ps.scrape_monitors(cdw_url_2, cdw_html_tag, "cdw")

    # # HP N223 - b&h
    # bh_url_2 = "https://www.bhphotovideo.com/c/product/1418778-REG/hp_3ml60a6_aba_n223_21_5_fhd_lcd.html?sts=pi&pim=Y"
    # ps.scrape_monitors(bh_url_2, bh_html_tag, "bh")

    # # HP N223 - ebay
    # eb_url_2 = "https://www.ebay.com/p/12020938322?iid=274162473698"
    # ps.scrape_monitors(eb_url_2, eb_html_tag, "ebay")
    # ##########################################################

    # ####################### HP Model 3 #######################
    # # HP P204 - walmart
    # wl_url_3 = "https://www.walmart.com/ip/HP-P204-19-5-inch-Monitor/967327819"
    # ps.scrape_monitors(wl_url_3, wl_html_tag, "walmart")

    # # HP P204 - cdw
    # cdw_url_3 = "https://www.cdw.com/product/hp-smartbuy-p204-19.5-hd-250cd-m-tn-led-backlight-monitor/5557207"
    # ps.scrape_monitors(cdw_url_3, cdw_html_tag, "cdw")

    # # HP P204 - b&h
    # bh_url_3 = "https://www.bhphotovideo.com/c/product/1482154-REG/hp_5rd65a8_aba_p204_19_5_16_9_tn.html"
    # ps.scrape_monitors(bh_url_3, bh_html_tag, "bh")

    # # HP P204 - ebay
    # eb_url_3 = "https://www.ebay.com/p/11032148806"
    # ps.scrape_monitors(eb_url_3, eb_html_tag, "ebay")

    # ##########################################################

    # ####################### HP Model 4 #######################
    # # HP P274 - walmart
    # wl_url_4 = "https://www.walmart.com/ip/HP-P274-27-inch-Monitor/860642099"
    # ps.scrape_monitors(wl_url_4, wl_html_tag, "walmart")

    # # HP P274 - cdw
    # cdw_url_4 = "https://www.cdw.com/product/hp-smartbuy-p274-27-250cd-m-ips-led-backlight-fhd-monitor/5557234?pfm=srh"
    # ps.scrape_monitors(cdw_url_4, cdw_html_tag, "cdw")

    # # HP P274 - b&h
    # bh_url_4 = "https://www.bhphotovideo.com/c/product/1482150-REG/hp_5qg36a8_aba_p274_27_16_9_ips.html?sts=pi&pim=Y"
    # ps.scrape_monitors(bh_url_4, bh_html_tag, "bh")

    # # HP P274 - ebay
    # eb_url_4 = "https://www.ebay.com/p/27032373269"
    # ps.scrape_monitors(eb_url_4, eb_html_tag, "ebay")

    ##########################################################

    ####################### HP Model 5 #######################
    # HP K5A38AA - walmart
    wl_url_5 = "https://www.walmart.com/ip/HP-24uh-LED-Backlit-Monitor-24-1-VGA-1-DVI-Basic-Gaming-K5A38AA-ABA/42807950"
    ps.scrape_monitors(wl_url_5, wl_html_tag, "walmart")

    # HP K5A38AA - cdw
    cdw_url_5 = "https://www.cdw.com/product/hp-24uh-24-led-backlit-lcd-black/3623331?enkwrd=HP+K5A38AA"
    ps.scrape_monitors(cdw_url_5, cdw_html_tag, "cdw")

    # HP K5A38AA - b&h
    bh_url_5 = "https://www.bhphotovideo.com/c/product/1124309-REG/hp_k5a38aa_aba_24uh_24_inch_led_backlit.html?sts=pi&pim=Y"
    ps.scrape_monitors(bh_url_5, bh_html_tag, "bh")

    # HP K5A38AA - ebay
    eb_url_5 = "https://www.ebay.com/p/220359861"
    ps.scrape_monitors(eb_url_5, eb_html_tag, "ebay")


    ##########################################################

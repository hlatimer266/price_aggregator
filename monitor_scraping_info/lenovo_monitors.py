import price_scraper as ps

if __name__ == "__main__":

    ####################### Lenovo Model 1 #######################
    # lenovo-thinkvision-t2224d - cdw
    cdw_url_1 = "https://www.cdw.com/product/lenovo-thinkvision-t2224d-led-monitor-full-hd-1080p-21.5/4503932"
    cdw_html_tag = "price-type-selected"
    ps.scrape_monitors(cdw_url_1, cdw_html_tag, "cdw")

    # lenovo-thinkvision-t2224d - bh
    bh_url_1 = "https://www.bhphotovideo.com/c/product/1464826-REG/lenovo_61b1jar1us_21_5_thinkvision_t2224d_led.html"
    bh_html_tag = "price_1DPoToKrLP8uWvruGqgtaY"
    ps.scrape_monitors(bh_url_1, bh_html_tag, "bh")

    # lenovo-thinkvision-t2224d - walmart
    wl_url_1 = "https://www.walmart.com/ip/Lenovo-ThinkVision-T2224d-21-5-inch-LED-Backlit-LCD-Monitor/306351777"
    wl_html_tag = "price-characteristic"
    ps.scrape_monitors(wl_url_1, wl_html_tag, "walmart")

    # lenovo-thinkvision-t2224d - eb
    eb_url_1 = "https://www.ebay.com/p/568422266"
    eb_html_tag = "display-price"
    ps.scrape_monitors(eb_url_1, eb_html_tag, "ebay")
    ###############################################################

    ####################### Lenovo Model 2 #######################
    # Lenovo ThinkVision E2054 - monoprice
    mn_url_1 = "https://www.monoprice.com/product?p_id=20534"
    mn_html_tag = "sale-price"
    ps.scrape_monitors(mn_url_1, mn_html_tag, "monoprice")

    # Lenovo ThinkVision E2054 - walmart
    wl_url_1 = "https://www.walmart.com/ip/LENOVO-ThinkVision-E2054-19-5-Monitor/114165638"
    ps.scrape_monitors(wl_url_1, wl_html_tag, "walmart")

    # Lenovo ThinkVision E2054 - office depot
    od_url_1 = "https://www.officedepot.com/a/products/829283/Lenovo-ThinkVision-E2054-195-LED-Monitor/"
    od_html_tag = "unified_price_row unified_sale_price red_price"
    ps.scrape_monitors(od_url_1, od_html_tag, "office_depot")

    # Lenovo ThinkVision E2054 - ebay
    eb_url_1 = "https://www.ebay.com/p/1060882873"
    ps.scrape_monitors(eb_url_1, eb_html_tag, "ebay")

    ##############################################################

    ####################### Lenovo Model 3 #######################
    # Lenovo ThinkVision s22e-19 - Walmart
    wl_url_2 = "https://www.walmart.com/ip/Lenovo-ThinkVision-S22e-19-21-5-inch-LED-Backlit-LCD-Monitor/368006422"
    ps.scrape_monitors(wl_url_2, wl_html_tag, "walmart")

    # Lenovo ThinkVision s22e-19 - cdw
    cdw_url_2 = "https://www.cdw.com/product/lenovo-thinkvision-s22e-19-21.5-fhd-led-backlit-lcd-monitor-black/5442887"
    ps.scrape_monitors(cdw_url_2, cdw_html_tag, "cdw")

    # Lenovo ThinkVision s22e-19 - b&h photo 
    bh_url_2 = "https://www.bhphotovideo.com/c/product/1464833-REG/lenovo_61c9kcr1us_21_5_thinkvision_s22e_19_led.html"
    ps.scrape_monitors(bh_url_2, bh_html_tag, "bh")

    # Lenovo ThinkVision s22e-19 - ebay
    eb_url_2 = "https://www.ebay.com/c/6027687973"
    ps.scrape_monitors(eb_url_2, "vi-bin-primary-price__main-price", "ebay")

    ##############################################################

    ####################### Lenovo Model 4 #######################
    # Lenovo ThinkVision P24q - Walmart
    # wl_url_3 = "https://www.walmart.com/ip/Lenovo-ThinkVision-P24q-23-8-inch-QHD-Monitor/822547947"
    # ps.scrape_monitors(wl_url_3, wl_html_tag, "walmart")

    # # Lenovo ThinkVision P24q - cdw
    # cdw_url_3 = "https://www.cdw.com/product/lenovo-thinkvision-p24q-led-monitor-23.8/4468844?pfm=srh"
    # ps.scrape_monitors(cdw_url_3, cdw_html_tag, "cdw")

    # # Lenovo ThinkVision P24q - bh
    # bh_url_3 = "https://www.bhphotovideo.com/c/product/1464824-REG/lenovo_61aegar3us_23_8_thinkvision_p24h_10_wide.html?sts=pi&pim=Y"
    # ps.scrape_monitors(bh_url_3, bh_html_tag, "bh")

    # # Lenovo ThinkVision P24q - ebay
    # eb_url_3 = "https://www.ebay.com/p/744285593"
    # ps.scrape_monitors(eb_url_3, eb_html_tag, "ebay")

    ##############################################################

    ####################### Lenovo Model 5 #######################

    # Lenovo ThinkVision T23d - walmart
    wl_url_4 = "https://www.walmart.com/ip/Lenovo-ThinkVision-T23d-22-5-1920x1200-6-ms-WLED-LCD-Monitor/449012204"
    ps.scrape_monitors(wl_url_4, wl_html_tag, "walmart")

    # Lenovo ThinkVision T23d - cdw
    cdw_url_4 = "https://www.cdw.com/product/lenovo-thinkvision-t23d-led-monitor-22.5/5229610?pfm=srh"
    ps.scrape_monitors(cdw_url_4, cdw_html_tag, "cdw")

    # Lenovo ThinkVision T23 - b&h
    bh_url_4 = "https://www.bhphotovideo.com/c/product/1464823-REG/lenovo_61abmar1us_23_thinkvision_t23i_10_wide.html?sts=pi&pim=Y"
    ps.scrape_monitors(bh_url_4, bh_html_tag, "bh")

    # Lenovo ThinkVision T23 - ebay
    eb_url_4 = "https://www.ebay.com/p/13024435610"
    ps.scrape_monitors(eb_url_4, eb_html_tag, "ebay")


    ##############################################################
import price_scraper as ps

if __name__ == "__main__":
    ####################### Dell Model 1 #######################
    # Dell P2319H - Walmart
    wl_url_1 = "https://www.walmart.com/ip/Dell-23-Ultrathin-Bundle-Surge-Screen-Cleaning-Essentials-LCD-IPS-Bezel-P2319H-16-9-Monitor-1-Pack-Cable-Kit-Computer-HDMI-Protector/285518626"
    wl_html_tag = "price-characteristic"
    ps.scrape_monitors(wl_url_1, wl_html_tag, "walmart")

    # Dell P2319H - cdw
    cdw_url_1 = "https://www.cdw.com/product/dell-p2319h-23-1920-x-1080-ips-lcd-monitor/5878515?pfm=srh"
    cdw_html_tag = "price-type-selected"
    ps.scrape_monitors(cdw_url_1, cdw_html_tag, "cdw")

    # Dell P2319H - b&h
    bh_url_1 = "https://www.bhphotovideo.com/c/product/1438207-REG/dell_23_p2319h_full_hd.html"
    bh_html_tag = "price_1DPoToKrLP8uWvruGqgtaY"
    ps.scrape_monitors(bh_url_1, bh_html_tag, "bh")

    # Dell P2319H - ebay
    eb_url_1 = "https://www.ebay.com/p/21031090139"
    eb_html_tag = "display-price"
    ps.scrape_monitors(eb_url_1, eb_html_tag, "ebay")

    ############################################################

    ####################### Dell Model 2 #######################

    # # Dell P2419H - walmart
    # wl_url_2 = "https://www.walmart.com/ip/Dell-24-P2419H-Ultrathin-IPS-LCD-Computer-Monitor-Deluxe-Bundle/878483161"
    # ps.scrape_monitors(wl_url_2, wl_html_tag, "walmart")

    # # Dell P2419H - cdw
    # cdw_url_2 = "https://www.cdw.com/product/dellp2419h-ledmonitor-fullhd1080p-24/5850945"
    # ps.scrape_monitors(cdw_url_2, cdw_html_tag, "cdw")

    # # Dell P2419H - b&h
    # bh_url_2 = "https://www.bhphotovideo.com/c/product/1430184-REG/dell_24_p2419h_full_hd.html"
    # ps.scrape_monitors(bh_url_2, bh_html_tag, "bh")

    # # Dell P2419H - ebay
    # eb_url_2 = "https://www.ebay.com/p/17030521662"
    # ps.scrape_monitors(eb_url_2, eb_html_tag, "ebay")

    # ############################################################

    # ####################### Dell Model 3 #######################
    # # Dell UltraSharp U2419H - walmart
    # wl_url_3 = "https://www.walmart.com/ip/Dell-UltraSharp-U2419H-24/421133198"
    # ps.scrape_monitors(wl_url_3, wl_html_tag, "walmart")

    # # Dell UltraSharp U2419H - cdw 
    # cdw_url_3 = "https://www.cdw.com/product/dell-ultrasharp-u2419h-led-monitor-full-hd-1080p-24/5298925?pfm=srh"
    # ps.scrape_monitors(cdw_url_3, cdw_html_tag, "cdw")

    # # Dell UltraSharp U2419H - b&h
    # bh_url_3 = "https://www.bhphotovideo.com/c/product/1485490-REG/dell_24_u2419hx_ultrasharp_wqhd.html"
    # ps.scrape_monitors(bh_url_3, bh_html_tag, "bh")

    # # Dell UltraSharp U2419H - ebay
    # eb_url_3 = "https://www.ebay.com/p/5025784139"
    # ps.scrape_monitors(eb_url_3, eb_html_tag, "ebay")

    # ############################################################

    # ####################### Dell Model 4 #######################
    # # Dell Ultrasharp U2717D - walmart
    # wl_url_4 = "https://www.walmart.com/ip/Dell-Ultrasharp-27-2560x1440-HDMI-DP-USB-60hz-8ms-QHD-LED-Monitor-U2717D-3-years-advanced-exchange-warranty/127268211"
    # ps.scrape_monitors(wl_url_4, wl_html_tag, "walmart")

    # # Dell Ultrasharp U2717D - cdw
    # cdw_url_4 = "https://www.cdw.com/product/dell-ultrasharp-u2419h-led-monitor-full-hd-1080p-24/5298925?pfm=srh"
    # ps.scrape_monitors(cdw_url_4, cdw_html_tag, "cdw")

    # # Dell Ultrasharp U2717D - b&h
    # bh_url_4 = "https://www.bhphotovideo.com/c/product/1254756-REG/dell_u2717d_27_ultrasharp_27.html?sts=pi&pim=Y"
    # ps.scrape_monitors(bh_url_4, bh_html_tag, "bh")

    # # Dell Ultrasharp U2717D - ebay
    # eb_url_4 = "https://www.ebay.com/p/5032173611"
    # ps.scrape_monitors(eb_url_4, eb_html_tag, "ebay")

    # ############################################################

    # ####################### Dell Model 5 #######################
    # # Dell UltraSharp U2412M - walmart
    # wl_url_5 = "https://www.walmart.com/ip/Dell-UltraSharp-U2412M-LED-monitor-24/21281827"
    # ps.scrape_monitors(wl_url_5, wl_html_tag, "walmart")

    # # Dell UltraSharp U2412M - cdw
    # cdw_url_5 = "https://www.cdw.com/product/dell-ultrasharp-24-u2412m-24-led-backlit-lcd-monitor-black/3848457?pfm=srh"
    # ps.scrape_monitors(cdw_url_5, cdw_html_tag, "cdw")

    # # Dell UltraSharp U2412M - b&h
    # bh_url_5 = "https://www.bhphotovideo.com/c/product/829236-REG/Dell_469_1137_U2412M_UltraSharp_24_LED.html"
    # ps.scrape_monitors(bh_url_5, bh_html_tag, "bh")

    # # Dell UltraSharp U2412M - ebay
    # eb_url_5 = "https://www.ebay.com/p/108867251"
    # ps.scrape_monitors(eb_url_5, eb_html_tag, "ebay")

    ############################################################
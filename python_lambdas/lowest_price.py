
def find_lowest_price(results_obj, MSRP):
    min = 10000
    curr_index = 0
    for sale_price in results_obj['results']:
        if sale_price['price'] != 'unavailable':
            price_flt = float(sale_price['price'].replace("$",""))
            if price_flt < min:
                min = price_flt
                min_index = curr_index
        curr_index += 1
    
    formatted_price = "{:.2f}".format(round(MSRP - float(min),2))
    results_obj['results'][min_index].update({"best_price":"lowest price! ($" + str(formatted_price) + " off MSRP)"})
            
    return results_obj

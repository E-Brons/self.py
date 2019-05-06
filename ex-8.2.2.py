import random

def get_item_price(x):
    return x[1]

def sort_item_prices(list_of_tuples):
    ''' Sort tuples of ('item', price) from lowest price to highest price
        :param arg1: list of tuple items (;item name', item_price)
        :type arg1:  list of tuples (str, float)
    '''
    list_of_tuples.sort(key=get_item_price)
    
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_item_prices(products)
print(products)
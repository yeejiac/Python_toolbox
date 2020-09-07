import numpy as np
import requests
import pandas as pd
import datetime
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
from lib.logwriter import *

def get_stock_history(date, stock_no):
    quotes = []
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' % ( date, stock_no)
    r = requests.get(url)
    data = r.json()
    if data['stat'] == 'OK':
        field = data['fields']
        data = data['data']
        df = pd.DataFrame (data,columns=field)
        print(df)
        logger.debug("stock_backtrace: get data success")
    else:
        logger.error("stock_backtrace: data error")

    

if __name__ == '__main__':
    get_stock_history(20201010, 2885)
import numpy as np
import requests
import pandas as pd
import datetime
import os
import sys
parent_dir = os.path.dirname(sys.path[0])
sys.path.insert(0, parent_dir)
from lib.logwriter import *
from lib.connDB_base import *
from lib.iniparser import *
import time

def dateTransfer_VidToRc(date):
    # 轉換成民國or西元日期(rc , vids)
    date = str(date)
    if len(date) != 8:
        return
    year = int(date[0:4])-1911
    return str(year)+'/'+ date[4:6] + '/' + date[6:8]


def get_stock_history(date, stock_no, mode):
    quotes = []
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' % ( date, stock_no)
    r = requests.get(url)
    data = r.json()
    field = data['fields']
    if data['stat'] == 'OK':
        if mode == 'd':
            data = data['data']
            data = [a for a in data if a[0] == dateTransfer_VidToRc(date)]
            logger.debug("stock_backtrace: get day data")
        elif mode == 'm':
            data = data['data']
            logger.debug("stock_backtrace: get month data")
            time.sleep(5)
        else: 
            logger.error("stock_backtrace: mode chosen error")
        df = pd.DataFrame(data,columns=field)
        print(df)
        return df
        logger.debug("stock_backtrace: get data success")
    else:
        logger.error("stock_backtrace: data error")

    
if __name__ == '__main__':
    data = get_stock_history(20200901, 2885, 'm')
    db = ConnDB_base(db_url)
    db.insertFrame(data, "stockInfo_2885")


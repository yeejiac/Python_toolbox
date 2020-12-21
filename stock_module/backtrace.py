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
from enum import Enum
import statistics

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
        db = ConnDB_base(db_url)
        db.insertFrame(df, "stockInfo_2885")
        logger.debug("stock_backtrace: get data success")
    else:
        logger.error("stock_backtrace: data error")

def readFromDB(stock_num, day):
    db = ConnDB_base(db_url)
    df = db.showTable("select 收盤價,日期 from `stockinfo_{}`".format(stock_num))
    if not df.empty:
        df = df.astype(str)
        df['收盤價'] = pd.to_numeric(df['收盤價'], errors='coerce')
        for d in day:
            ma = [0 for a in range(0, d)]
            rownum = len(df)
            a = 0
            for i in range(d+1, rownum+1):
                maval = round(statistics.mean(df['收盤價'][a:i]), 2)
                ma.append(maval)
                a+=1
            df['MA{}'.format(d)] = ma
        print(df)
        return df

class Inventory:
    def __init__(self, stock_vol, stock_price, nid):
        self.stock_vol = stock_vol
        self.stock_price = stock_price
        self.stock_sellprice = 0
        self.sellFlag = False
        self.nid = nid

    def setSellInfor(self, price):
        self.sellFlag = True
        self.stock_sellprice = price

class Account:
    def __init__(self):
        self.originMoney = 1000000
        self.money = 1000000
        self.inventoryList = []
        self.nid = 0
        self.price_now = 0
        
    def buy(self, stock_vol, deduct_price, price, date):
        self.money = self.money - deduct_price
        inv = Inventory(stock_vol, price, self.nid)
        self.inventoryList.append(inv)
        self.nid+=1
        print("買進股票 : {} 時間 : {}".format(price, date))

    def sell(self, stock_vol, increase_price, date, nid):
        self.money = self.money + increase_price
        [i.setSellInfor(increase_price/(stock_vol*1000)) for i in self.inventoryList if i.nid == nid ]
        print("賣出股票 : {} 時間 : {}".format(increase_price/(stock_vol*1000), date))

    def getProfit(self): #已實現損益
        return [i.stock_sellprice - i.stock_price for i in self.inventoryList if i.sellFlag == True]

    def getProfit_N(self): #未實現損益
        return [i.stock_sellprice - i.stock_price for i in self.inventoryList if i.sellFlag != True]

    def printInfo(self):
        print("帳戶餘額 : {}".format(self.money + sum(self.getProfit_N())*1000))
        print("已實現損益 : {}".format(sum(self.getProfit())*1000))
        print("未實現損益 : {}".format(sum(self.getProfit_N())*1000))
        print("帳戶總額 : {}".format(self.money + sum(self.getProfit_N())*1000 - self.originMoney))
        


def main():
    # for i in range(1,12):
    #     datestring = "2020" + str(i).zfill(2) + "01"
    #     get_stock_history(datestring, 2885, 'm')
    readFromDB(2885, [3,5])
    # acc = Acount()








    
if __name__ == '__main__':
    main()


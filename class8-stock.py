# -*- coding: utf-8 -*-
"""
Created on Sun May 15 06:07:25 2022

@author: user
"""
def convertDate(date):
    str1 = str(date)
    yearstr = str1[ :3]
    realyear = str(int(yearstr) + 1911)
    realdate = realyear + str1[4:6] + str1[7:9]
    return realdate

import requests, json, csv, os
import pandas as pd
import matplotlib.pyplot as plt
                   
plt.rcParams['font.sans-serif'] = 'mingliu'
plt.rcParams['axes.unicode_minus'] = False

pd.options.mode.chained_assignment = None   #取消顯示 pandas資料重設警告

filepath = 'stockmonth01.csv'

if not os.path.isfile(filepath):
    url_twse = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220501&stockNo=2317&_=1652568553440'
    res = requests.get(url_twse)
    jdata = json.loads(res.text)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as outputfile:
        outputwriter = csv.writer(outputfile)
        outputwriter.writerow(jdata['fields'])
        for dataline in (jdata['data']):
            outputwriter.writerow(dataline)
    
pdstock = pd.read_csv(filepath, encoding='utf-8')
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])
pdstock.plot(kind='line', figsize=(12, 6), x= '日期', y=['收盤價','最低價', '最高價'])














# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:20:10 2022

@author: user
"""
import requests, json
import pandas as pd

url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
html = requests.get(url)
info = json.loads(html.text)
df = pd.DataFrame.from_dict(info["retVal"], orient='index')
#print(df)
#ubike_df = pd.DataFrame(columns=('sna', 'mday', 'tot', 'sbi', 'bemp'))


for rowID in range(1, 382):
    sna = df.iloc[rowID-1, 1]
    print("站點名稱 : ", sna)
    mday = df.iloc[rowID-1, 5]
    print("更新時間 : ", mday)
    tot = df.iloc[rowID-1, 2]
    print("停車格數 : ", tot)
    sbi = df.iloc[rowID-1, 3]
    print("車輛數量 : ", sbi)
    bemp = df.iloc[rowID-1, 12]
    print("空位格數 : ", bemp)
    print('------'*5)






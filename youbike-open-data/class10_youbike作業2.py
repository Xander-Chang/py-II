# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:22:37 2022

@author: user
"""
import requests, json
import pandas as pd
# Sample 1 - 資料來源
html = requests.get("https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json")
info = json.loads(html.text)

df = pd.DataFrame.from_dict(info,orient='columns')     #value 是字典 可以用 index

df.to_csv('ubike.csv', encoding='utf-8-sig')

# Sample 2 - 資料取得

print(len(df))
for i in range(1, 1227):                             # 字典順序
    sna = df.iloc[i-1, 1]                            # iloc[key, value] 定位 dataframe
    print("站點名稱 : ", sna)
    mday = df.iloc[i-1, 5]
    print("更新時間 : ", mday)
    tot = df.iloc[i-1, 2]
    print("停車格數 : ", tot)
    sbi = df.iloc[i-1, 3]
    print("車輛數量 : ", sbi)
    bemp= df.iloc[i-1, 12]
    print("空位格數 : ", bemp)
    print('*'*20)



# Sample 3 - 使用效率
df = pd.read_csv('ubike.csv')
df_info = df[['sna', 'sbi', 'bemp']]
print(df_info)

print('*'*80)

df['use_ratio'] = 1 - df['sbi'] / df['bemp']
eficient = df[['sna', 'use_ratio']]
print(eficient)



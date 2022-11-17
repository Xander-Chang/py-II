# -*- coding: utf-8 -*-
"""
Created on Tue May 17 07:57:47 2022

@author: user
"""
import csv
import pandas as pd
#sample 5.   
with open('sample5_tw_rate.csv', encoding='utf-8-sig') as f:
    f_csv = csv.reader(f)
    f_list = list(f_csv)

for row in f_list:
    while '-' in row:
        i = row.index('-')
        row[i] = '0'

head = f_list[0]  # 表頭
f_list2 = f_list[1:]
tags = head[1:]   #各類利率標題
bank_name = []
figures = []

for row in f_list2:
    bank_name.append(row[0])
    figures.append(row[1:])

    
df = pd.DataFrame(figures, index=bank_name,columns=tags)
print(df, '\n最大值: ', df.max())
    
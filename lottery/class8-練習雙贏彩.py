# -*- coding: utf-8 -*-
"""
Created on Sun May 15 04:53:17 2022

@author: user
"""

import requests, csv
from bs4 import BeautifulSoup as bs

url = 'https://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = bs(html.text, 'lxml')
datas = sp.find('div', class_= 'contents_box06')
date = datas.find('span', class_='font_black15')         # 開獎期數
print(date.text)
nums = datas.find_all('div', class_='ball_tx ball_blue') # 開獎號碼
print('開出順序: ')  
print(*nums,'\n')                                     # 開出順序            
for i in range(12):
    print(nums[i], end='')
print('\n大小順序: ')                                     # 大小順序
for j in range(len(nums)-12, len(nums)):
    print(nums[j].text, end='')
# 存檔
with open('class8-練習雙贏彩.csv', 'w', encoding='UTF-8-sig', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['開獎期數', date.text])
    f_csv.writerow(['開獎順序'])
    for i in range(12):
        f_csv.writerow(['', nums[i].text])
    f_csv.writerow(['大小順序'])
    for j in range(len(nums)-12, len(nums)):
        f_csv.writerow(['', nums[j].text])
    
    
    




















   
    
    
    
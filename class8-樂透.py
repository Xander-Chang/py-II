# -*- coding: utf-8 -*-
"""
Created on Sun May 15 01:48:19 2022

@author: user
"""

import requests, csv
from bs4 import BeautifulSoup as bs

url = 'https://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = bs(html.text, 'lxml')
# 找到威力彩區塊
datas = sp.find('div', class_='contents_box02')
#print(datas)
# 開獎期數
# find() 找到第一個

### &nbsp = 空格/空白

date = datas.find('span', class_= 'font_black15')
print('威力彩期數', date.text)
# 開獎號碼
numbers = datas.find_all('div', class_='ball_tx ball_green')
#print(numbers)
# 開出順序
print('開出順序: ', end='')
for i in range(6):
    print(numbers[i].text, end=' ')
# 大小順序
print()
print('大小順序: ', end='')
for j in range(len(numbers)-6, len(numbers)):
    print(numbers[j].text, end=' ')
# 第二區(特別號)
print()
special = datas.find('div', class_= 'ball_red')
print('特別號: ', special.text)



# 存檔
with open('lottery.csv', 'w', encoding='utf-8-sig', newline= '') as f:
    csv_f = csv.writer(f)
    csv_f.writerow(['威力彩期數', date.text])
    csv_f.writerow(['開出順序'])
    for i in range(6):
        csv_f.writerow([' ', numbers[i].text])
    csv_f.writerow(['大小順序'])
    for j in range(len(numbers)-6, len(numbers)):   
        csv_f.writerow([' ', numbers[j].text])
        
    csv_f.writerow(['特別號', special.text])
















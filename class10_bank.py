# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:42:48 2022

@author: user
"""
import requests, csv
from bs4 import BeautifulSoup as bs
import pandas as pd

# Sample 1 - 網頁內容
'''
url = 'http://www.taiwanrate.com/'
html = requests.get(url)
print('html 編碼方式: ', html.encoding)
print('列印網頁內容: \n', html.text)
'''

# Sample 2 - 網頁與編碼
'''
url = 'http://www.taiwanrate.com/'
html = requests.get(url)
print('html 編碼方式: ', html.encoding)
html.encoding = 'utf-8'
print('更改編碼')
print('html 編碼方式: ', html.encoding)
print('列印網頁內容: \n', html.text)
'''

# Sample 3 - 取得 Table 內容
'''
url = 'http://www.taiwanrate.com/'
html = requests.get(url)
html.encoding = 'utf-8'                            
objSoup = bs(html.text, 'lxml')
#print(objSoup)

# rate_table = objSoup.find_all('table')
rate_table = objSoup.find('table', id= 'table1')
#print(rate_table)

# 列印表格欄位 - 先找 標題
# 左上角內容
# lefttop = rate_table[4].find('tr').find('tr').find('td')
lefttop = rate_table.find('tr').find('td')
#print(lefttop.text)
#列出 其他 標題欄位 名稱
rate_head = rate_table.find('tr').find_all('a', class_='bodytablehead')
#print(rate_head)
for head in rate_head:
    print(head.text, end=', ')
print()
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
rated = rate_table.find('tr', class_= 'bodytabletr1')
#print(rated.text)
# 找出其他   

# 方法一 : 
# find_next_sibling() 找下一個
#while rated.find_next_sibling('tr'):
#    rated = rated.find_next_sibling('tr')
#    print(rated.text)
    
# 方法二
# find_all() 做兩次
rated = rate_table.find_all('tr', class_= 'bodytabletr1')
rated2 = rate_table.find_all('tr', class_= 'bodytabletr2')
for i in rated:
    print(i.text, end=' ')
for j in rated2:
    print(j.text, end=' ')
'''


# Sample 4 - 取得內容與存檔 - 存檔csv 要注意格式
'''
# Step 1   存取網址 / head1
html = requests.get('http://www.taiwanrate.com/')
soup = bs(html.text, 'lxml')
head1 = soup.find('table', id='table1').find('tr').find('td')
headlist = []
headlist.append(head1.text)
#print(headlist)

# Step 2   headall
tablelist = []
headall = soup.find('table',id='table1').find('tr').find_all('a', class_='bodytablehead')
for item in headall:
    headlist.append(item.text)
tablelist.append(headlist)
#print(headlist)
#print(tablelist)

# Step 3   rate1
ratelist = []
rate1 = soup.find('table',id='table1').find('tr', class_='bodytabletr1')#.find_all('td')
#print(rate1)
for num in rate1:
    ratelist.append(num.text)
#print(ratelist)
tablelist.append(ratelist)
#print(tablelist)

# Step 3 - rateall   
# print(rate1.find_next_siblings('tr'), '\n')       # 為了給每個tag 都上list, 所以不用此涵式
#print(rate1.find_next_sibling('tr'))

while rate1.find_next_sibling('tr'):         
    rate1 = rate1.find_next_sibling('tr')
    ratelist = []
    for row in rate1:
        ratelist.append(row.text)
    tablelist.append(ratelist)
#print(tablelist)

with open('class10_bank_sample4範例 1.csv','w', newline='', encoding='utf-8-sig') as f:
    f_csv = csv.writer(f)
    for row in tablelist:                       # 一次寫一筆
        f_csv.writerow(row)


# 練習1 # Sample 4 - 取得內容與存檔

rate1 = soup.find('table',id='table1').find_all('tr', class_='bodytabletr1')
#print(rate1)
for i in rate1:
    ratelist = []
    for j in i:
        ratelist.append(j.text)
    tablelist.append(ratelist)
#print(ratelist)
#print(tablelist)

with open('class10_bank_sample4練習 1-0.5.csv','w', encoding='utf-8-sig', newline='') as f:
    f_csv = csv.writer(f)
    for row in tablelist:
        f_csv.writerow(row)
    #print('done!')
# 不同 class, 再做一次, 合在一起才是完整一份
rate1 = soup.find('table',id='table1').find_all('tr', class_='bodytabletr2')
#print(rate1)
for i in rate1:
    ratelist = []
    for j in i:
        ratelist.append(j.text)
    
#print(tablelist)

with open('class10_bank_sample4練習 1-1.csv','w', encoding='utf-8-sig', newline='') as f:
    f_csv = csv.writer(f)
    for row in tablelist:
        f_csv.writerow(row)
    #print('done!')
'''















'''
# Sample 5 - 開啟檔案與求最大值

# Step 1.   開檔
fn = 'class10_bank_sample4範例 1.csv'
with open(fn, encoding='utf-8-sig') as f:
    f_csv = csv.reader(f)                  # 讀檔案建立Reader物件
    list_f = list(f_csv)                   # 將資料轉成串列 ??? 為何要轉 
#print(list_f)


# Step 2.   資料清洗   
for row in list_f:                  # 將'-'改為'0'
    while '-' in row:               #為什麼只能用 while???
        i = row.index('-')          #index() / find()
        row[i] = '0'   
#print(list_f)

# Step 3.   資料切割   
head_tag = list_f[0]
list_f = list_f[1:]

tag = head_tag[1:]

bank_name = []
rate_datas = []
for row in list_f:
    bank_name.append(row[0])
    rate_datas.append(row[1:])
    
# Step 4.   資料分析 / 製成表格、求最大值
df = pd.DataFrame(rate_datas, columns=tag, index=bank_name)
#print(df)
print('最大值: ', df.max())


# Sample 5 - 練習

# 開檔
with open('class10_bank_sample4範例 1.csv', encoding='utf-8-sig') as f:
    f_csv = csv.reader(f)
    f_list = list(f_csv)   #資料轉成 list
# 資料清洗
for row in f_list:
    while '-' in row:
        i = row.index('-')
        row[i] = '0'

# 資料切割
headtag = f_list[0]  #銀行/各種利率標題
bank = headtag[0]   #銀行標題
tags = headtag[1:]   #各種利率標題
f_list2 = f_list[1:]  #去頭後的所有資料

bank_name = []      #各家銀行名稱
rate_figure = []    #各種利率參數

for datas in f_list2:
    bank_name.append(datas[0])
    rate_figure.append(datas[1:])

# 分析
df = pd.DataFrame(rate_figure, index=bank_name, columns=tags)
print(df)
print('\n最大值: ', df.max())
'''


















# Sample 6 - 基金網頁
# 抓標題
# Sample 7 - 基金數據
# 抓標題
# 抓基金表格資料

# Sample 8 - 讀檔與取得績效

html = requests.get('https://www.moneydj.com/funddj/ya/YP401000.djhtm')
soup = bs(html.text,'lxml')
# 抓標題
tablelist = []
headlist = []
titles= soup.find('tr', id='oScrollMenu').find_all('th')
for row in titles:
    headlist.append(row.text.strip())
#print(headlist)
tablelist.append(headlist)
#print(tablelist)                # \r\n ???
# 抓基金表格資料
dataslist = []
datas = soup.find('tbody').find_all('tr')
for row in datas:
    print(row.text)
    tablelist.append(row.text.strip().split())
#print(tablelist)  
# 寫入csv
with open('class10_bank_sample8練習.csv','w',encoding='utf-8-sig', newline='') as f:
    f_csv = csv.writer(f)
    for row in tablelist:
        f_csv.writerow(row)













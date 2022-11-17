# -*- coding: utf-8 -*-
"""
Spyder Editor
Python 資料分析應用課程 - C010
網站資料擷取與分析
"""
import requests, bs4, csv
import pandas as pd


'''
# Sample 1 - 網頁內容
url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)


# Sample 2 - 網頁與編碼
url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
htmlfile.encoding = 'utf-8'         # 編碼改為utf-8
print("更改編碼")
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)

'''
# Sample 3 - 取得 Table 內容
'''
url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
htmlfile.encoding = 'utf-8'                                 # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
ratetable = objSoup.find_all('table')
# 列印表格欄位名稱
lefttop = ratetable[4].find('tr').find('tr').find('td')     # 第4個表格
print(lefttop.text,end=' ')                                 # 左上角內容                  

ratehead = ratetable[4].find('tr').find_all('a', 'bodytablehead')
for head in ratehead:
    print(head.text, end=' ')                               # 列出其它欄位名稱
# 以上是列印表格欄位名稱
print()
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
ratetd = ratetable[4].find('tr', 'bodytabletr1')            
print(ratetd.text)                                          # 列出第一家銀行
while ratetd.find_next_sibling('tr'):
    ratetd = ratetd.find_next_sibling('tr')
    print(ratetd.text)                                      # 列出其它家銀行
'''

# Sample 4 - 取得內容與存檔
'''
fn = "out13_4.csv"
tablelist = []                                              # 利率表串列
headlist = []
ratelist = []
url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
htmlfile.encoding = 'utf-8'                                 # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
ratetable = objSoup.find_all('table')
print(ratetable[4])
# 列印表格欄位名稱
lefttop = ratetable[4].find('tr').find('tr').find('td')     # 第4個表格
headlist.append(lefttop.text)                               # 加入欄位名稱串列                
ratehead = ratetable[4].find('tr').find_all('a', 'bodytablehead')
for head in ratehead:
    headlist.append(head.text)                              # 加入欄位名稱串列
tablelist.append(headlist)  
'''
                            # 
# 以上是列印表格欄位名稱
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
'''
ratetd = ratetable[4].find('tr', 'bodytabletr1')            # 找出第一筆利率   
for row in ratetd:
    ratelist.append(row.text)
tablelist.append(ratelist)                                  # 將第一筆銀行利率加入
while ratetd.find_next_sibling('tr'):                       # 找出其他銀行利率
    ratetd = ratetd.find_next_sibling('tr')
    ratelist = []
    for row in ratetd:
        ratelist.append(row.text)
    tablelist.append(ratelist)                              # 加入其它家銀行利率

with open(fn, 'w', newline = '') as csvFile:                # 寫入out13_4.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)                             # 一次寫一筆
'''
'''
# Sample 5 - 開啟檔案與求最大值
fn = 'out13_4.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列    

for row in listReport:                  # 將'-'改為'0'
    while '-' in row:
        i = row.index('-')
        row[i] = '0'    

time_period = listReport[0]             # 將第一個串列改為columns
time_period = time_period[1:]

listReport = listReport[1:]             # 切片

bank = []
newReport = []
for row in listReport:                  # 取得index
    bank.append(row[0])
    newReport.append(row[1:])           # 建立新利率串列

df = pd.DataFrame(newReport,columns=time_period,index=bank)
print(df)

mymax = df.max()
print(mymax)


'''
'''
# Sample 6 - 基金網頁

url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:
    print(head.text.strip())
'''

'''
# Sample 7 - 基金數據
url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')      # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:                                      # 輸出基金表格標題
    print(head.text.strip(), ' ', end='')
print()
# 抓基金表格資料
objtable = fundtable.find('tbody')
tables = objtable.find_all('tr')
for table in tables:                                    # 輸出各基金績效
    rowtext = table.text.strip()
    txt = rowtext.split('\n')                           # 將字串轉成串列
    print(txt)
'''

# Sample 8 - 讀檔與取得績效
fn = 'out13_8.csv'
tablelist = []
headlist = []
url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')      # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:                                      # 輸出基金表格標題
    headlist.append(head.text)
tablelist.append(headlist)
# 抓基金表格資料
objtable = fundtable.find('tbody')
tables = objtable.find_all('tr')
for table in tables:                                    # 輸出各基金績效
    #print(table)
    rowtext = table.text
    #print(rowtext)
    rowtext = rowtext.strip()
    #print(rowtext)
    txt = rowtext.split('\n')
    #print(txt)                           # 將字串轉成串列
    tablelist.append(txt)
print(tablelist)
# 寫入csv    
with open(fn, 'w', newline = '') as csvFile:            # 寫入out13_8.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)                         # 一次寫一筆
  

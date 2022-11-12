# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:45:47 2022

@author: user
"""

import requests, json
# 一、 requests運用介紹
#1. 
#使用 get 方式下載普通網頁 其他:
'''
r = requests.get('https://www.google.com.tw/')
print(r)                  #Response [200] 代表 ok
print(type(r))
'''
#伺服器回應的狀態碼   status_code
'''
print(r.status_code)
print(type(r.status_code))
'''

#檢查狀態碼是否 ok
'''
if r.status_code == requests.codes.ok:
    print('ok')
'''    
    
#2. 
#輸出網頁 HTML 原始碼
'''
r = requests.get('https://www.google.com.tw/')
print(r.text, '\n')  

r1 = requests.get('http://httpbin.org/get')
print(r1.text, '\n')
r2 = requests.post('http://httpbin.org/post')
print(r2.text, '\n')
'''

#3. 
#增加 URL 查詢參數
#查詢參數
#將查詢參數加入 GET 請求中
'''
my_params = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.get('http://httpbin.org/get', params = my_params)

#觀察 URL / HTML 原始碼   (增加查詢參數後的不同)
r1 = requests.get('http://httpbin.org/get')
r2 = requests.get('http://httpbin.org/get', params = my_params)
print(r1.url, '\n')
print(r1.text, '\n')
print('-'*50)
print(r2.text, '\n')
print(r2.url, '\n')
'''



#二、  requests運用操作

#1. 取得Google Trend的趨勢值
url = 'https://trends.google.com.tw/trends/trendingsearches/daily?geo=TW'

#2. 以payload 設定params，ed 可以設定日期
payload = {
    'hl': 'zh-TW',         # zh 繁中, TW國別
    'tz': '-480',          #timezone , 台灣第八時區, 減八小時
                           #如果要指定日期可以加上 ed 參數, 'ed': '20220423',
    'geo': 'TW',           # 
    'ns': '15',
    }

html = requests.get(url, params = payload)
html.encoding= 'utf-8'
print(html.text)

#資料清洗
'''
_, datas = html.text.split(',', 1)
#print(_)                   #底線'_', 代表不重要的變數
#print(datas)
'''


#3. 取資料
'''
jsondata = json.loads(datas)                             

for trendingSearchesDay in jsondata['default']['trendingSearchesDays']:
                                   #大括號為物件型態,可以直接取
    print('日期: ' + trendingSearchesDay['formattedDate'])
    
    for data in trendingSearchesDay['trendingSearches']:
        print('主題關鍵字: ' + data['title']['query'])
                                   #大括號為物件型態,可以直接取
        print('搜尋次數: ' + data['formattedTraffic'])                          
        for content in data['articles']:
            print('標題: ', content['title'])
            print('發佈時間: ', content['timeAgo'])
            print('來源: ', content['source'])
            print('網址: ', content['url'])
            print('內容: ', content['snippet'])
        print('-'*50)
'''

#4. 存檔
'''
jsondata = json.loads(datas)       
for trendingSD in jsondata['default']['trendingSearchesDays']:
    news = ''
    news += '日期:' + trendingSD['formattedDate'] + '\n\n'
    
    for data in trendingSD['trendingSearches']:
        news += '主題關鍵字: ' + data['title']['query'] + '\n\n'
        for content in data['articles']:
            news += '標題: '+ content['title']+ '\n\n'
            news += '發佈時間: '+ content['timeAgo']+ '\n\n'
            news += '來源: '+ content['source']+ '\n\n'
            news += '網址: '+ content['url']+ '\n\n'
            news += '內容: '+ content['snippet']+ '\n\n'

    filename = trendingSD['date'] + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(news)
    print(filename + '已存檔')
    
'''




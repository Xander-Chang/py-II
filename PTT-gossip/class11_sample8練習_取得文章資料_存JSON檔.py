# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:31:39 2022

@author: user
"""
import requests, os
import json
from bs4 import BeautifulSoup as bs

# Sample 1 - 加入 cookie 的內容來連線
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
html = requests.get(url, cookies={'over18':'1'})
soup = bs(html.text, 'lxml')
print(type(soup))
#print(soup.text.strip().split())



# Sample 2 - 取得此頁的文章數量
titles = soup.find_all('div', class_='r-ent')
#print(titles)
num = 0
for p in titles:
    if p.find('a'):
        num += 1        
print('筆數: ', num)
print('筆數: ', len(titles))


# Sample 3 - 列出文章編號/標題/作者/連結/ # Sample 4 - 取得推文數量

    #方式一、
info = soup.find_all('div', class_='r-ent')

count = 0 
for p in info:
    if p.find('a'):
        number = p.find('div', class_='nrec').text
        title = p.find('a').text
        author = p.find('div', class_='author').text
        link = p.find('a')['href']
        count += 1
        print('文章編號 : ', count)
        print('推文數量 : ', number)
        print('文章標題 : ', title)
        print('文章作者 : ', author)
        print('文章連結 : ', link,'\n')
print('本頁文章數: ', count)

print('\n', '*'*100)

    #方式二、 
info = soup.find_all('div', class_='r-ent')

articles = []
for p in info:
    if p.find('a'):
        number = p.find('div', class_='nrec').text
        title = p.find('a').text
        author = p.find('div', class_='author').text
        link = p.find('a')['href']
        
        articles.append({'推文數量': number,         # 在列表加入字典 
                         '文章標題': title,
                         '文章作者': author,
                         '文章連結': link})

count = 0
for article in articles:                            # 取字典的 value
    count += 1
    print('文章編號 : ', count)
    print('推文數量 : ', article['推文數量'])
    print('文章標題 : ', article['文章標題'])
    print('文章作者 : ', article['文章作者'])
    print('文章連結 : ', article['文章連結'],'\n')
print('本頁文章數: ', len(articles))

print('\n', '='*100)


# Sample 5 - 推文數大於某定值   /   # Sample 6 - 推噓文

info = soup.find_all('div', class_='r-ent')

articles = [] 
for p in info:
    if p.find('a'):
        title = p.find('a').text
        publish_time = p.find('div', class_='date').text
        author = p.find('div', class_='author').text
        link = p.find('a')['href']
        
        push_num = p.find('div', class_='nrec').text
        if push_num.startswith('X'):                    # 表示推文被噓超過10次
                push_num = '0'
        if push_num == '爆':                            # 表示推文超過100次
                push_num = '100'
        
        articles.append({'文章標題': title,
                         '發表時間': publish_time,
                         '文章作者': author,
                         '文章連結': link,
                         '推文數量': push_num})

count = 0
pushcounts = 20 
for article in articles:
    count += 1
    if push_num != '':
        push_min =  int(push_num)
    else:
        push_min = 0                                # 如果是空的 給 0
    
    if push_min > pushcounts:              
        print('文章編號 : ', count)
        print('文章標題 : ', article['文章標題'])
        print('發表時間 : ', article['發表時間'])
        print('文章作者 : ', article['文章作者'])
        print('文章連結 : ', article['文章連結'])
        print('推文數量 : ', article['推文數量'],'\n')
print('本頁文章數: ', len(articles))








# Sample 7 - 存成 Json

info = soup.find_all('div', class_='r-ent')

articles = [] 
for p in info:
    if p.find('a'):
        title = p.find('a').text
        publish_time = p.find('div', 'date').text
        author = p.find('div', class_='author').text
        link = p.find('a')['href']
        
        push_num = p.find('div', 'nrec').text
        if push_num.startswith('X'):                    # 表示推文被噓超過10次
                push_num = '0'
        if push_num == '爆':                            # 表示推文超過100次
                push_num = '100'
        
        articles.append({'文章標題': title,
                         '發表時間': publish_time,
                         '文章作者': author,
                         '文章連結': link,
                         '推文數量': push_num})

with open('class11_sample7範例_opendata.json', 'w') as fjson:
    json.dump(articles, fjson, indent=2, ensure_ascii=False)








# Sample 8 - 下載表特版中的圖片
# ptt
'''
ptt_url = 'https://www.ptt.cc'
beauty = '/bbs/beauty/index.html'

ptthtml = requests.get(ptt_url + beauty, cookies={'over18':'1'})
pttsoup = bs(ptthtml.text, 'lxml')
ptt_div = pttsoup.find_all('div', class_= 'r-ent')
ptt_href = ptt_div[0].find('a')['href']

print('目前連線: ', ptt_url + ptt_href)
beauty_html = requests.get(ptt_url + ptt_href, cookies={'over18':'1'})
beauty_soup = bs(beauty_html.text, 'lxml')
beauty_div = beauty_soup.find('div', id='main-content').find_all('a')

photos = []
for photo in beauty_div:
    photo_href = photo['href']
    if photo_href.startswith('https://i.imgur'):
        photos.append(photo_href)


# 建立文件夾
if not os.path.exists('class11_sample8練習-2'):
    os.mkdir('class11_sample8練習-2')
    

for photo in photos:                                                # 列印圖片網址
    print(photo)
print("搜尋到的圖片數量 = ", len(photos))        


for photo in photos:                                    # 迴圈下載圖片與儲存
    picture = requests.get(photo)                       # 下載圖片
    print("%s 圖片下載成功" % photo)
    
    full_path = os.path.join('class11_sample8練習-2', os.path.basename(photo))
    with open(full_path, 'wb') as f_jpg:
        for item in picture.iter_content(10240):
            f_jpg.write(item)
print('done')


'''





















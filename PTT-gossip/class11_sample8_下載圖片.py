# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:17:47 2022

@author: user
"""

import os, requests
from bs4 import BeautifulSoup as bs

# ptt
ptt_url = 'https://www.ptt.cc'
beauty = '/bbs/Beauty/index.html'

ptt_html = requests.get(ptt_url+beauty, cookies={'over18': '1'})
ptt_soup = bs(ptt_html.text, 'lxml')
ptt_div = ptt_soup.find_all('div', class_='r-ent')
ptt_href = ptt_div[0].find('a')['href']
#ptt_href1 = ptt_div[0].find('a')
#print(type(ptt_href1))
print(type(ptt_href))


# beauty
beauty_url = ptt_url + ptt_href
beauty_html = requests.get(beauty_url, cookies={'over18': '1'})
beauty_soup = bs(beauty_html.text, 'lxml')
beauty_div = beauty_soup.find('div',id='main-content')
beauty_href = beauty_div.find_all('a')



# photo 網址
photos = []
for photo in beauty_href:
    photo_href = photo['href']
    if photo_href.startswith('https://i.imgur'):  
        photos.append(photo_href)
        


# 建立文件夾       
if not os.path.exists('class11_sample8練習-1'):
    os.mkdir('class11_sample8練習-1')
    

# download  
n = 0  
for photo in photos:
    print(photo)
print('搜尋到的圖片數量: ', len(photos))


for photo in photos:
    picture = requests.get(photo)
    print('%s 下載成功' % photo)
    
    fullpath = os.path.join('class11_sample8練習-1', os.path.basename(photo))
    with open(fullpath, 'wb') as f_jpg:
        for item in picture.iter_content(10240):
            f_jpg.write(item)
print('done')




























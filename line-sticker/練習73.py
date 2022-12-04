# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:29:56 2022

@author: user
"""

import requests, os, json, bs4

html = requests.get('https://store.line.me/stickershop/product/570/zh-Hant')
soup = bs4.BeautifulSoup(html.text, 'html.parser')
datas = soup.find_all('li', {'class': 'mdCMN09Li FnStickerPreviewItem'})

if not os.path.exists('line表情包73'):
    os.mkdir('line表情包73')
    
s = 0   
for pic in datas:
    pic_json = pic.get('data-preview')
    pic_info = json.loads(pic_json)
    pic_url = pic_info['fallbackStaticUrl']
    png = requests.get(pic_url)
    
    
    full_path = os.path.join('line表情包73', str(s))
    s += 1
    with open(full_path + '.png', 'wb') as f:
        f.write(png.content)
        print(full_path, 'check')
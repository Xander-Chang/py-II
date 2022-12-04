# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:21:27 2022

@author: user
"""

import os, json, bs4, requests

html = requests.get('https://store.line.me/stickershop/product/18079/zh-Hant')
# 1. 為什麼要分析器??? 課堂4 並未用到, 作用是甚麼呢???
soup = bs4.BeautifulSoup(html.text, 'html.parser')
# 2. 為什麼可以直接找 'li', 而不是從'ul'或其他???
datas = soup.find_all('li', {'class': 'mdCMN09Li FnStickerPreviewItem'})
# 3. 為什麼通常都要給變數, 不能直接用檔名???
# 4. 檔名用點斜線的用意???
if not os.path.exists('line貼圖包 練習72'):
    os.mkdir('line貼圖包')
s = 0
for pic in  datas:
    pic_json = pic.get('data-preview')
    pic_info = json.loads(pic_json)
    pic_url = pic_info['fallbackStaticUrl']
    #5. 貼圖為動畫怎麼下載???只能把圖跟聲音載下來嗎???
    png = requests.get(pic_url)
    
    s += 1
    full_path = os.path.join('line貼圖包', str(s))
    with open (full_path + '.png', 'wb') as f:
        #7. content 的作用是什麼???
        f.write(png.content)
        print(s ,'.png', '已存檔' )
        
        
        
        
        
        
        
        
        
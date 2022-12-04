# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:12:01 2022

@author: user
"""
import requests, os, json, bs4

#1. 載入網址檔案
html = requests.get('https://store.line.me/stickershop/product/11817/zh-Hant')

#2. 用html 分析器
soup = bs4.BeautifulSoup(html.text, 'html.parser')

#3. 下載 擷取字典部分*
stickers = soup.find_all('li', {'class': "mdCMN09Li FnStickerPreviewItem"})
#print(stickers) # list

#4. 建立文件檔
if not os.path.exists('line_stickers/'):
    os.mkdir('line_stickers/')
    
#5. 用迴圈取值
for png in stickers:
    #1. 取得 json 檔
    png_json = png.get('data-preview')
    #2. 用 json 讀取
    png_info = json.loads(png_json)
    #3. 用 key 取值  /  取得圖片檔案
    id = png_info['id']
    stickerrr = requests.get('https://stickershop.line-scdn.net/stickershop/v1/sticker/60923142/iPhone/sticker@2x.png')
    
    
    #4. 儲存完整路徑 、 主檔名*
    fullpath = os.path.join('line_stickers/', id)
    #5. 寫入文件檔 / 附上副檔名
    with open (fullpath + '.png', 'wb') as f:
        f.write(stickerrr.content)
        print(fullpath + '.png')
        
        
        
        
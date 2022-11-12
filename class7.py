# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:02:56 2022

@author: user
"""

import requests, os, json
from bs4 import BeautifulSoup
# 1.   取得網址的檔案
url = 'https://store.line.me/stickershop/product/19306143/zh-Hant'
html = requests.get(url)
#print(type(html.text))
#print(html.text)



# 2. 網頁分析   BeautifulSoup()
# 格式 xml / html 的 parser(分析器)

soup = BeautifulSoup(html.text, 'html.parser')
#print(type(soup))       # 資料型態變不一樣
#print(soup)



#3.   建立目錄儲存圖片
#加上'/' 為固定寫法, 避免被誤認為檔案
#   './line_image/'

images_dir = 'line_image/'
if not os.path.exists(images_dir):
    os.mkdir(images_dir)




#4.   下載貼圖
datas = soup.find_all('li', {'class': 'mdCMN09Li FnStickerPreviewItem'})
#print(type(datas))
#結果是 list
#print(datas)


#5.   1. 用for迴圈 列舉/拿出 list 的值
for data in datas:
    #print(data)
    #print('-----------------')
    
    #2. 將字串資料轉為字典
    ## 使用方法 get() 取得 jason
    imgjson = data.get('data-preview')
    #print(data.get('data-preview'))
    #print('-----------------')
    
    #3. 用 json.loads() 讀取
    imginfo = json.loads(imgjson)
    #print(imginfo)
    #print('-----------------')
    
    #4. 用 key 取值
    # 取得 id / staticUrl 的值
    id = imginfo['id']
    s_url = imginfo['staticUrl']
    #print(id)
    #print(s_url)
    #print('-----------------')
    
    #5. 取得網址的檔案 (載入圖片檔)
    imgfile = requests.get(s_url)
    
    #6. 儲存完整路徑 、 主檔名
    full_path = os.path.join(images_dir, id)
    #print(full_path)
    #print('-----------------')
    
    #7. 
    #給副檔名
    #儲存圖片
    
    with open(full_path + '.png', 'wb') as f:
        f.write(imgfile.content)
        print(full_path + '.png')
    
























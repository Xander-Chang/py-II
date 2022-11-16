# -*- coding: utf-8 -*-
"""
Spyder Editor
Python 資料分析應用課程 - C009
股票資訊即時取得與通知
"""
import requests

msg = '這是 LINE Notify 發送的訊息。'
token = '權杖'
# token = '你的 LINE ifNoty 權杖'  #權杖
headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}
payload = {'message': msg}
notify = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
if notify.status_code == 200:
    print('發送 LINE Notify 成功！')
else:
    print('發送 LINE Notify 失敗！')
    
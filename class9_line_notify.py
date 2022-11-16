# -*- coding: utf-8 -*-
"""
Created on Mon May 16 02:48:34 2022

@author: user
"""

import requests
from datetime import datetime

nowtime = datetime.now()

msg = 'LINE NOTIFY 的訊息。 ' + str(nowtime)
token = '權杖'
# token = '你的 LINE ifNoty 權杖'
headers = {
    "Authorization": "Bearer " + token, 
    "Content-Type" : "application/x-www-form-urlencoded"}

payload = {'message': msg}
notify = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)

if notify.status_code == 200:
    print('發送 LINE NOTIFY 成功! ')
else:
    print('發送 LINE NOTIFY 失敗! ')
    
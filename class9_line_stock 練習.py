# -*- coding: utf-8 -*-
"""
Created on Mon May 16 06:20:46 2022

@author: user
"""

import time, requests, twstock
token = 'ZbX2bTyO7tO4hCBuWvUrX3HtnGiN3wVatR6xttsJvlP'
def authorize (token, msg):                                       # step5
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    response = requests.post('https://notify-api.line.me/api/notify', headers=headers, params=payload)
    return response.status_code

sent_success = 0
sent_fail = 0
while True :
    realdata = twstock.realtime.get('2317')                       # step1
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']
        print('當前股價: ', realprice)
        if float(realprice) > 100:                                 # step2
            message = '2317 價格超過100, 可賣出'
            print('2317 價格超過100, 可賣出')
        elif float(realprice) < 60:
            message = '2317 價格低於60, 可購入'
            print('2317 價格低於60, 可購入')
        sent_success +=1                                           # step3
        code = authorize (token, message)                          # step4
        if code == 200:                                            # step6
            print('第 ' + str(sent_success) + ' 次發送 LINE 訊息。')
        else:
            print('發送 LINE 訊息失敗！')
        if sent_success >= 3:                                      # step7
                print('程式結束！')
                break
    else:                                                         # step8
        print('錯誤：' + realdata['rtmessage'])
        sent_fail += 1
        if sent_fail >= 3:
            print('程式結束！')
            break
    for i in range(10):                                           # step9
            time.sleep(1)
            
            
            
            
            
            
            
            
            
            
            
            
            
        
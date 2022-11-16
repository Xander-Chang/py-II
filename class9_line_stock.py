# -*- coding: utf-8 -*-
"""
Created on Mon May 16 03:18:54 2022

@author: user
"""
import requests, time, twstock

def requests_line(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    response = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return  response.status_code
    


token = '權杖'
sent_success = 1
sent_fail = 1

def Message (mode, sent_success):
    
    if mode == 1:
        message = '2317 目前股價偏高,可以賣出'
    else:
        message = '2317 目前股價偏低,可以買入'
    
    responce_code = requests_line(token, message)
    if responce_code == 200:
        print('第 ' + str(sent_success) + ' 次發送 LINE 訊息。')
    else:
        print('發送 LINE 訊息失敗！')
    return sent_success
    

    
print('程式開始執行！')

  
while True:
    realdata = twstock.realtime.get('2317')
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']
        print('鴻海目前股價：' + str(realprice))
        if float(realprice) > 100:
            sent_success =  Message(1, sent_success)
        elif float(realprice) < 60:
            sent_success =  Message(2, sent_success)
        
        sent_success += 1    
        if sent_success >= 3:
            print('程式結束！')
            break
    else:
        print('錯誤：' + realdata['rtmessage'])
        sent_fail += 1
        if sent_fail >= 3:
            print('程式結束！')
            break
    
    for i in range(10):
        time.sleep(1)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
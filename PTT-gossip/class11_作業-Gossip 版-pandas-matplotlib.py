# -*- coding: utf-8 -*-
"""
Created on Fri May 20 14:56:39 2022

@author: user
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt

gossip_url = 'https://www.ptt.cc'
stock_url = 'https://www.ptt.cc/bbs/Stock/index.html'
c_chat_url = 'https://www.ptt.cc/bbs/C_Chat/index.html'
# 取得日期 筆數
gossip_sum521 = 0
gossip_sum520 = 0
gossip_sum519 = 0
for hundreds in range(3,0,-1):
    for tens in range(9,0,-1):
        for digits in range(9,0,-1):
            gossip_url = 'https://www.ptt.cc/bbs/Gossiping/index39' + str(hundreds) + str(tens) + str(digits) + '.html'
            gossip_html = requests.get(gossip_url, cookies={'over18':'1'})
            gossip_soup = bs(gossip_html.text, 'lxml')
            gossip_div = gossip_soup.find_all('div','r-ent')
            
            for i in range(len(gossip_div)):
                gossip_date = gossip_div[i].find('div','date').text
                if gossip_date == ' 5/21':
                    gossip_sum521 += 1
                elif gossip_date == ' 5/20':
                    gossip_sum520 += 1
                elif gossip_date == ' 5/19':
                    gossip_sum519 += 1
print('gossip 5/21: ', gossip_sum521)
print('gossip 5/20: ', gossip_sum520)
print('gossip 5/19: ', gossip_sum519)


gossip_timeslist = [gossip_sum521, gossip_sum520,gossip_sum519]
gossip_datelist = ['5/21', '5/20', '5/19']
print(gossip_timeslist)
print(gossip_datelist)

# 製圖(直條圖) pandas
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(gossip_timeslist,index=gossip_datelist)
gossip_figure = df.plot(kind='bar', title='Gossip 版', xlabel='日期', ylabel='文章數', figsize=[10,5])


# 製圖(直條圖) matplotlib
'''
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
plt.rcParams['axes.unicode_minus'] = False

plt.bar(gossip_datelist, gossip_timeslist)
plt.title('Gossip 版', fontsize=20)
plt.xlabel('日期')
plt.ylabel('文章數')
plt.show()
'''

















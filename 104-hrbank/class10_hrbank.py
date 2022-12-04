# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:13:33 2022

@author: user
"""
import requests
from bs4 import BeautifulSoup as bs
import json
import random
import time

# Sample 1 - 取得職稱
'''
html = requests.get('https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc')
soup = bs(html.text, 'lxml')
info = soup.find_all('article', class_='js-job-item')
#print(info)

for i in info:
    #print(i, '\n')
    print(i.text.strip().split(), '\n')
    print('公司名稱: ', i.get('data-cust-name'))
    print('職務名稱: ', i.get('data-job-name'))
    print('-'*80)
'''


# Sample 2 - 取得職稱與列表
'''
html = requests.get('https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc')
soup = bs(html.text, 'lxml')
info = soup.find_all('article', class_='js-job-item')
#print(info)
joblist = []
for i in info:
    cust_name = i.get('data-cust-name')
    print('公司名稱: ', cust_name)
    job_name = i.get('data-job-name')
    print('職務名稱: ', job_name,'\n')
    
    # 變元組
    d = [('公司名稱: ', cust_name), ('職務名稱: ', job_name)]
    print('變元組\n', d, '\n')
    
    #再變字典
    jdict = dict(d)
    print('再變字典\n', jdict, '\n')
    
    #加入空列表
    joblist.append(jdict)
    print('加入空列表\n', joblist, '\n')
    
    
    # json 格式
    myjob = {'job': joblist}              
    print('json 格式\n', myjob, '\n')
         

    jlist = list(jdict)               #dic 轉 list 取 key
    jvalues = list(jdict.values())    # dic 轉 list 取 values
    print('\n', jlist , jvalues, '\n')         

    print('-'*80)  

with open('class10_hrbank.json', 'w') as jfile:
    json.dump(myjob, jfile, indent=2, ensure_ascii=True)
'''




# Sample 3 - 不同查詢方式分析
'''
def job_info(url):
    html = requests.get(url)
    soup = bs(html.text, 'lxml')
    data = soup.find_all('article', class_='js-job-item')
    for j in data:
        print('公司名稱: ', j.get('data-cust-name'))
        print('職務名稱: ', j.get('data-job-name'))

urls = ['https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=2&mode=s&jobsource=2018indexpoc',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=3&mode=s&jobsource=2018indexpoc'
        ]

for url in urls:
    job_info(url)
    
    num = random.randint(3,5)
    print(num, '秒', '='*80)
    time.sleep(num)
    
'''


# Sample 4 - 限定分頁取得資料
'''
def job_info(url):
    html = requests.get(url)
    soup = bs(html.text, 'lxml')
    data = soup.find_all('article', class_='js-job-item')
    for j in data:
        print('公司名稱: ', j.get('data-cust-name'))
        print('職務名稱: ', j.get('data-job-name'))

url_head = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page='
url_tail = '&mode=s&jobsource=2018indexpoc'



page_total = 5

for i in range(page_total):
    url = url_head + str(i+1) + url_tail
    job_info(url)
    print('='*20)
    ran = random.random()
    time.sleep(ran)
    print(ran)
'''




# 尋找個數
'''
html = requests.get('https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc')
soup = bs(html.text, 'lxml')
info = soup.find_all('article', class_='js-job-item')
article = 0

for n in info:
    if n.find('a'):
        article += 1
print('筆數: ', article)
'''





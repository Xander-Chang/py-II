# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:11:21 2022

@author: user
"""
import requests
from bs4 import BeautifulSoup as bs

#Sample 1: 網頁基本架構與 tag
'''
url = 'http://ehappy.tw/bsdemo1.html'
html = requests.get(url)
html.encoding= 'UTF-8'
sp = bs(html.text, 'lxml')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.h1.text)
print(sp.p)
'''


#Sample 2: find　與　find_all  方法
html = '''
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>網頁標題</title>
    </head>
    <body>
        <p id="p1">第一段</p>
        <p id="p2" class="red">第二段</p>
    </body>
</html> 
'''
sp = bs(html, 'lxml')
# 後面加上'屬性'搜尋
'''
print(sp.find('p'))
print(sp.find_all('p')) #中括號, 類似陣列

print(sp.find('p', {'id':'p2', 'class':'red'}))
print(sp.find('p', id='p2', class_= 'red'))
'''


#Sample 3: select()  方法(陣列型態)
html= '''
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>網頁標題</title>
    </head>
    <body>
        <p id="p1">我是第一段</p>
        <p id="p2" class="red">第二段</p>
    </body>
</html> 
'''
sp = bs(html, 'lxml')
'''
print(sp.select('title'))
print(sp.select('p'))
# 找屬性
#'#' = id(唯一性, 不可以重複)
print(sp.select('#p1'))
# '.' = class 
print(sp.select('.red'))
'''


#Sample 4: select()  方法(陣列型態) 與 tag 屬性
html= '''
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>網頁標題</title>
    </head>
    <body>
        <img src='https://www.ehappy.tw/python.png' />
        <a href='hppts://www.e-happy.com.tw'>超連結</a>
    </body>
</html> 
'''

sp = bs(html, 'lxml')
'''
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
# 更簡單
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])
'''

#Sample 5: 所有方法 之比較
html= '''
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>網頁標題</title>
    </head>
    <body>
        <h1>文件標題</h1>
        <div class="content">
            <div class="item1">
                <a href="http://example.com/one" class="red" id="link1">First</a>
                <a href="http://example.com/two" class="red" id="link2">Second</a>
            </div>
            <a href="http://example.com/three" class="blue" id="link3">
                <img src="http://example.com/three.jpg"/>third
            </a>
        </div>
    </body>
</html> 
'''

sp = bs(html, 'lxml')
'''
print(sp.title)                                    #<title>網頁標題</title>
print(sp.find('h1'))                               #<h1>文件標題</h1>
print(sp.find_all('a'))
print(sp.find_all('a', {'class': 'red'}))
print(sp.find_all('a', class_= 'red'), '\n')

data1 = sp.find('a', href= 'http://example.com/one')
print(data1.text, '\n')                            # First

data2 = sp.select('#link1')
print(data2[0].text)                               # First
print(data2[0]['href'])                            #http://example.com/one
print(data2[0].get('href'), '\n')                  #http://example.com/one

print(sp.find_all(['title', 'h1']), '\n')

print(sp.select('div img')[0]['src'])
print(sp.select('div img')[0].get('src'), '\n')
'''


find_next_sibling('')

















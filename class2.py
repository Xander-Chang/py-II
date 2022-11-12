# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:17:41 2022

@author: user
"""
#1. 用pandas 讀取excel/ csv 檔案
#import pandas as pd

#第一段   用pandas讀取excel/ csv檔案
'''
df = pd.read_excel('208-3.xls')
df = pd.read_csv('111bfh.csv')
'''
#print(df)
#print(type(df))


#第二段   用pandas讀取excel/ csv檔案,或特定的sheet
#sheet_name='',讀取單頁 ; sheet_name=['']讀取多頁
'''
df = pd.read_excel('208-3.xls', sheet_name = '108')
df = pd.read_excel('208-3.xls', sheet_name = ['102','108'])
print(df)
'''
#第三段   用pandas 讀取excel '欄' 資料
#資料黨要先整理,表頭會影響到欄的讀取
# usecols= ['']
 #方法1 :
'''
df = pd.read_excel('208-3.xls', sheet_name=['108_2'], usecols=['縣市別'])
df = pd.read_excel('208-3.xls', sheet_name=['108_2'], usecols= ['縣市別', '男性參賽選手數'])
'''
 #方法2 :
'''
df = pd.read_excel('208-3.xls', sheet_name= ['108_2'], usecols='A, C:D') #字母代表欄,無須括號
print(df)
'''

#第四段   用pandas 讀取excel '列'資料
 # 方法1 : 用nrows, 缺點只能從頭開始讀取
'''
df = pd.read_excel('208-3.xls', sheet_name='108_2', nrows= 10)
print(df)
''' 
 #方法2 : 全部讀取後,再選出範圍
'''
#df = pd.read_excel('208-3.xls', sheet_name=['108_2'])      #無法切片,原因?
df = pd.read_excel('208-3.xls', sheet_name='108_2')
new_df = df[0:10]
print(new_df)
'''

#第五段   用pandas 讀取excel '儲存格'資料
#Datafram.at[position, 'label']
##在label之下第一格為位置'0'
'''
df = pd.read_excel('208-3.xls',sheet_name='108_2')
df_cell = df.at[1,'縣市別']
print(df_cell)
'''





#2. 用json 
import json 

with open('data.json', 'r') as f:     #還不是json格式
    p = json.load(f)                  #變成json格式檔案,讀取
    print(p)
    #資料型態: 字典
    print(type(p))                     
    #取值
    print('name=', p['name'])
    print('age=', p['age'])
    print('skill=', p['skill']) 
    print('married=', p['married'])
    #取得陣列中的內容
    print(type(p['skill'])) 
    print(len(p['skill'])) 
    # 一維陣列的取值方式
    print(p['skill'][0])
    print(p['skill'][1])
















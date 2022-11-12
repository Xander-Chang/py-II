# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:43:57 2022

@author: user
"""

import numpy as np
import time
#類型一
# python 的list
'''
A = 50
x = [100, 200 ,'a', A]  資料形態會一樣,變成字串
print(type(x))
print(x[0])    
print(x[0] * 2)
#list跑兩次
print(x * 2)
# 將list所有值乘2
for i in x:
    j= i*2
    print(j)
# numpy array
y = np.array([1,2])    
print(type(y))
print(y[0])
#所有值乘2       重要!!!
print(y*2)
print(type(y*2))
'''

#類型二   不同的建立方式
#1. 
'''
np1 = np.array([1,2,3,4])   #使用list
np2 = np.array((5,6,7,8))   #使用tuple
print(type(np1))
print(type(np2))
'''

#各種方式:
# 2. arange()
#python range()
'''
b = range(1, 9, 3)
print(b, type(b))
# numpy.arange()
np3 = np.arange(1, 9, 3) 
print(type(np3), np3)
'''
#3. linspace(始值,終值,個數) 
'''
np4 = np.linspace(1, 9, 4)  #用於找平均數字
print(type(np4), np4)
'''
#4. zeros([]) 
'''
np5 = np.zeros(2)           #只有2也可以,但是習慣上不是
np5 = np.zeros([2,])        #有逗號才是矩陣形式
np5 = np.zeros([2, 3])      #二維以上要兩個括號
np5 = np.zeros([2, 3, 5])
print(type(np5), np5)
'''
#5. ones([])
'''
np6 = np.ones(2)
np6 = np.ones([2,])
np6 = np.ones([2, 3, 5])
print(type(np6), np6)
'''
#6. empty(())
'''
np7 = np.empty([2,])       #不懂用法???
np7 = np.empty([2, 2])
print(np7)
'''

#類型三：　NPinfo
'''
list_data = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15]]
na = np.array(list_data)
print(na)
print('維度: ', na.ndim)
print('形狀: ', na.shape)
print('數量: ', na.size)
print('元素型態: ', na.dtype)
'''
#類型四 矩陣變形-reshape   #個數總數必須相同
'''
begin_time = time.time()
adata = np.arange(0, 100)
print(adata)
bdata = adata.reshape(10, 10)
time = time.time() - begin_time
print(bdata, '\n', time)
'''
   #練習
'''
begin = time.time()
a = np.arange(0,100000000)
print(a)
b = a.reshape(10000,10000)
time =  time.time() - begin
print(b, '\n', time)
'''
#類型五   一維矩陣取值 與python一樣
'''
na = np.arange(0,6)
print(na)
print(na[0])
print(na[5])
print(na[1:5])
print(na[1:5:2])
print(na[5:1:-1])
print(na[:])
print(na[:3])
print(na[3:])
'''
#類型六   多維矩陣取值
'''
na = np.arange(1,17).reshape(4,4)

print(na)
print(na[2,3])
print(na[1, 1:3])
print(na[1:3, 2])       #橫豎分開取
print(na[1:3, 1:3])
print(na[::2,::2])
print(na[:,2])
print(na[1, : ])
print(na[:,:])
'''

#類型七   隨機產生陣列內容
'''
print('1. 產生2x3, 0-1之間的隨機浮點數:\n', np.random.rand(2,3),'\n')
print('2. 產生2x3, 常態分布的隨機浮點數:\n', np.random.randn(2,3),'\n')
print('3. 產生0-4(不含5)的隨機整數:\n', np.random.randint(5),'\n')
print('4. 產生2-4(不含5)的5個隨機整數:\n', np.random.randint(2,5,5),'\n')
print('5. 產生3個 0-1之間的隨機浮點數:\n', 
      np.random.random(3),'\n', 
      np.random.random_sample(3),'\n',     #有三種方法
      np.random.sample(3),'\n')
print('6. 產生0-4(不含5)2x3的隨機整數:\n', np.random.choice(5,[2,3]),'\n')
print('7. 產生0-42(不含43)6個不重複的隨機整數:\n', 
      np.random.choice(43,6,replace= False),'\n')
'''
#類型八   從excel檔案內容,產生array
'''
a = np.genfromtxt('scores.csv',delimiter=',', skip_header=1)
print(a.shape)
'''
#類型九   陣列運算(一)-基本運算
'''
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
#1. 陣列內容
print('a 陣列內容: ', a)
print('b 陣列內容: ', b)
print('a 陣列元素都加值: ', a + 1)
print('a 陣列元素都平方: ', a ** 2)    
print('a 陣列元素家判斷: ', a < 5)  
print('a 陣列取第一個row都加 1: ', a[0,:] + 1) 
print('a 陣列取第一個col都加 1: ', a[:,0] + 1) 
print('a 陣列對應元素相加: ', a + b) 
print('a 陣列對應元素相乘: ', a * b) 
'''
#類型十   numpy 計算(二) - 統計函數
'''
a = np.arange(1,10.reshape(3,3)) 
print('陣列的內容: ')
'''
#類型十一   計算(三) - 統計函數
#類型十二   排序(


#類型十三   排序(二)

















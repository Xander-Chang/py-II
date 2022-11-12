# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:33:47 2022

@author: user
"""

#產生一個很大的陣列(10000 x 10000)並隨機給值，
#將陣列每個值都平方，
#並判斷是否大於 50(結果為 true 或 false)。
#查看其所花的時間為何？
import random, time
import numpy as np
begin = time.time()
a = np.random.choice(100000000,100000000,replace= False).reshape(10000, 10000)
b = a**2
print('1. 陣列為: ', a,'\n')
print('2. 每個值都平方: ', b,'\n')
print('3. 是否大於50: ', a>50, '\n',)
print('4. 所花費時間: ', time.time() - begin, '\n')

print('5. 資料型態:\t', type(a), '\n',
      '6. 維度:\t', a.ndim, '\n',
      '7. 陣列形狀:\t', a.shape, '\n',
      '8. 元素數量:\t', a.size, '\n',
      '9. 元素型態:\t', a.dtype)
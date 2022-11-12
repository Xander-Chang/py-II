# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:18:35 2022

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

# Sample 1:   建立 Series 資料
#Series([]) 一維資料
#陣列
'''
se = pd.Series([1,2,3,4])

print(type(se))
print(se)            #顯示 Series
print(se.values)     #顯示值
print(se.index)      #顯示索引
'''

#元組
'''
se = pd.Series((1,2,3,4))

print(type(se))
print(se)            #顯示 Series
print(se.values)     #顯示值
print(se.index)      #顯示索引
'''

#字典
'''
dict1 = {'a': 100, 'b': 200, 'c': 300, 'a': 400}
se = pd.Series(dict1)

print(type(se))
print(se)            
print(se.values)     
print(se.index) 
print(se['a'])            #可以取 key
print(se['a':'c'])
'''

# Sample 2:   建立 Series 資料 / 取值
'''
se = pd.Series([1,2,3,4,5])

print(se[2])            
print('-' * 6)     
print(se[2:5])
'''


# Sample 3:   建立 DataFrame 資料 
#範例一
'''
df = pd.DataFrame([[65,92,78,83,70],
                   [90,72,76,93,56],
                   [81,85,91,89,77],
                   [79,53,47,94,80]])
print(df)
print(df[4][0])      #和 list 相反
'''

#類型一   類似 excel
# pd.DataFrame([[], []], index=[], columns=[])
'''
df = pd.DataFrame([[65,92,78,83,70],
                   [90,72,76,93,56],
                   [81,85,91,89,77],
                   [79,53,47,94,80]],
                   index=['王', '李', '陳', '林'],
                   columns=['國',' 英', '數', '自', '社'])
print(df)
'''
#類型二
# 用字典包含字典
# 字典的key值位置不重要
# pd.DataFrame({'a':{}, 'b':{}})
'''
scores = {'國':{'林':79,'李':90,'陳':81, '王':65},
          '英':{'王':92,'李':72,'陳':85, '林':53},
          '數':{'王':78,'李':76,'陳':91, '林':47},
          '自':{'王':83,'李':93,'陳':89, '林':94},
          '社':{'王':70,'李':56,'陳':94, '林':80}}
df = pd.DataFrame(scores)
print(df)
'''

#類型三
# 用 Series建立, 用DataFrame() 製成二維表格(字典包含字典)
# 字典的key值位置不重要
'''
se1 = pd.Series({'林':79,'李':90,'陳':81, '王':65})
se2 = pd.Series({'王':92,'李':72,'陳':76, '林':56})
se3 = pd.Series({'王':78,'李':76,'陳':91, '林':47})
se4 = pd.Series({'王':83,'李':93,'陳':89, '林':94})
se5 = pd.Series({'王':70,'李':56,'陳':94, '林':80})
df = pd.DataFrame({'國':se1, '英':se2, '數':se3, '自':se4, '社':se5})

print(df)
'''

#類型四
# pd.concat([], axis=0/1 )
#key值位置不重要
'''
se1 = pd.Series({'林':79,'李':90,'陳':81, '王':65})
se2 = pd.Series({'王':92,'李':72,'陳':76, '林':56})
se3 = pd.Series({'王':78,'李':76,'陳':91, '林':47})
se4 = pd.Series({'王':83,'李':93,'陳':89, '林':94})
se5 = pd.Series({'王':70,'李':56,'陳':94, '林':80})
df = pd.concat([se1,se2,se3,se4,se5], axis=0)
df = pd.concat([se1,se2,se3,se4,se5], axis=1)
df.columns=['國','英','數','自','社' ]    
# hardcode :寫進程式碼,好清楚,不好維護更改

print(df)
'''




# Sample 4:   建立 DataFrame 資料 / 取值
# loc[]   location
# iloc[] 
# head() / tail()
'''
scores = {'國':{'林':79,'李':90,'陳':81, '王':65},
          '英':{'王':92,'李':72,'陳':85, '林':53},
          '數':{'王':78,'李':76,'陳':91, '林':47},
          '自':{'王':83,'李':93,'陳':89, '林':94},
          '社':{'王':70,'李':56,'陳':94, '林':80}}
df = pd.DataFrame(scores)
print(df)

print(df['自'], '\n')

print(df[['國','數','自']], '\n')

print(df['國'] >= 80, '\n')
print(df[['國','英']] >= 80, '\n')

print(df[df['國'] >= 80], '\n')
#國文、數學都大於80分

print(df.values, '\n')
print(df.values[1], '\n')
print(df.values[1][2], '\n')


# loc[]   location
print(df.loc['林', '社'], '\n')
print(df.loc['林', ['國','社']], '\n')
print(df.loc[['林','王'], ['國','社']], '\n')
#取法有包含終值!!!!!
print(df.loc['林':'王', '國':'自'], '\n')
print(df.loc['林', :], '\n')
print(df.loc[:'王', '國':'自'], '\n')
print(df.loc['李': , '國':'自'], '\n')
# 順序顛倒
print(df.loc[::-1, '國':'自'], '\n')

# iloc[]   index location
print(df.iloc[3, 4], '\n')
print(df.iloc[0, [0, 4]], '\n')
print(df.iloc[[0, 1],[2, 4]], '\n')

print(df.iloc[0: 3, 2: 5], '\n')
print(df.iloc[2, : ], '\n')
print(df.iloc[:2, 2:5 ], '\n')
print(df.iloc[1: , 2:5 ], '\n')

# head() / tail()
print(df.head(2))
print(df.tail(2))
'''

# Sample 4:   建立 DataFrame 資料 / 取值(2)


scores = {'國':{'林':79,'李':90,'陳':81, '王':65},
          '英':{'王':92,'李':72,'陳':85, '林':53},
          '數':{'王':78,'李':76,'陳':91, '林':47},
          '自':{'王':83,'李':93,'陳':89, '林':94},
          '社':{'王':70,'李':56,'陳':94, '林':80}}
df = pd.DataFrame(scores)
# 1. 排序
# df.sort_values(by='數', ascending=True)
'''
print(df.sort_values(by='數', ascending=True), '\n')   #數上升
print(df.sort_values(by='數', ascending=False), '\n')  #數下降
'''
# df.sort_index(axis=0)
'''
print(df.sort_index(axis=0), '\n')     #較少用
print(df.sort_index(axis=1), '\n')
'''

# 2. 修改
# df.loc['王']['數']
'''
df.loc['王']['數'] = 100
print(df, '\n')
df.loc['王', : ] = 100
print(df, '\n')
'''

# 3. 刪除 (產生新的DataFrame, 故要給新變數)
# df1 = df.drop('王', axis=0) 
'''
df1 = df.drop('王')
print(df1, '\n')
df1 = df.drop('王', axis=0)    #axis=0 預設
print(df1, '\n')
df1 = df.drop('數', axis=1)
print(df1, '\n')
df1 = df.drop(['數', '自'], axis=1)
print(df1, '\n')
'''
# df.drop(df.index[:])
'''
df1 = df.drop(df.index[1:4])
print(df1, '\n')
'''
# df.drop(df.columns[:], axis=1)
'''
df1 = df.drop(df.columns[1:4], axis=1)
print(df1, '\n')
'''

#第八堂 補充
# Sample 5:   pandas 資料讀取 - csv
'''
datas = pd.read_csv('score2.csv', header=0, index_col=0)
print(datas)
print(type(datas))
'''

# Sample 6:   pandas 資料讀取 - html
'''
url = 'http://www.giobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])
'''


# Sample 7:   pandas 資料儲存 - to csv
'''
scores = {'國':{'林':79,'李':90,'陳':81, '王':65},
          '英':{'王':92,'李':72,'陳':85, '林':53},
          '數':{'王':78,'李':76,'陳':91, '林':47},
          '自':{'王':83,'李':93,'陳':89, '林':94},
          '社':{'王':70,'李':56,'陳':94, '林':80}}
df = pd.DataFrame(scores)
df.to_csv('scores3.csv',encoding='utf-8-sig')
'''


# Sample 8:   pandas 繪圖
#類型一   長條圖、橫條圖、堆疊長條圖
'''
#設定中文字型及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
#也可以設定 mingliu / DFKai-SB
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame([[250,320,300,312,280],
                  [280,300,280,290,310],
                  [220,280,250,305,250]],
                  index=['北部','中部','南部'],
                  columns=[2015,2016,2017,2018,2019])
g1 = df.plot(kind='bar', title='長條圖', figsize=[10,5])
g2 = df.plot(kind='barh', title='橫條圖', figsize=[10,5])
g3 = df.plot(kind='bar', stacked=True, title='堆疊圖', figsize=[10,5])
'''
    
#類型二   折線圖
'''
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
#也可以設定 mingliu / DFKai-SB
plt.rcParams['axes.unicode_minus'] = False 
                                      
df = pd.DataFrame([[250,320,300,312,280],
                  [280,300,280,290,310],
                  [220,280,250,305,250]],
                  index=['北部','中部','南部'],
                  columns=[2015,2016,2017,2018,2019])
g1 = df.iloc[0].plot(kind='line', legend=True, xticks=range(2015,2020), title='公司分區年度銷售圖', figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True, xticks=range(2015,2020))#, title='公司分區年度銷售圖', figsize=[10,5])
g1 = df.iloc[2].plot(kind='line', legend=True, xticks=range(2015,2020))#, title='公司分區年度銷售圖', figsize=[10,5])
'''

#類型三   圓餅圖
'''
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
#也可以設定 mingliu / DFKai-SB
plt.rcParams['axes.unicode_minus'] = False 

df = pd.DataFrame([[250,320,300,312,280],
                  [280,300,280,290,310],
                  [220,280,250,305,250]],
                  index=['北部','中部','南部'],
                  columns=[2015,2016,2017,2018,2019])

df.plot(kind='pie', subplots=True, autopct='%2.1f%%', figsize=[20,20], \
        shadow=True, startangle=0)
'''


# Sample 9:   資料清洗
#當資料有缺失時, 可以 [刪除]、[填入] 資料

#讀取資料
df = pd.read_csv('customer.csv')

# 方式一   找空值、 找錯誤
'''
#空值處理
print('各個欄位有空值的狀況: ')
print(df.isnull().sum())
print('有空值的紀錄筆數: ', df.isnull().any(axis=1).sum())
print('有空值的欄位數: ', df.isnull().any(axis=0).sum())
print('age欄有空值的紀錄: ')
### 重要!!!
print(df[df['age'].isnull()])
'''
# 方式二   [填入]

# 1.   將age 的空值填入 0
'''
# fillna(value=0) ， 空值、非數值時, 填入 value
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=0)
print(df_sample.head())
'''
# 2.   將age 的空值填入平均數 mean()
'''
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=df_sample['age'].mean())
print(df_sample.head())
'''

# 3.   以 前一個值往下填ffill 或往上填 bfill
'''
df_sample = df.copy()
df_sample['gender'] = df_sample['gender'].fillna(method='ffill')
df_sample['area'] = df_sample['area'].fillna(method='ffill')
print(df_sample.head())
'''


#刪除不完整的資料   [刪除]
'''
df_sample = df.copy()
print(df.dropna())
'''

















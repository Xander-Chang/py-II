# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:17:42 2022

@author: user
"""

import matplotlib.pyplot as plt

#範例一    
# Sanple 1. 折線圖
# plot()
'''
listx = [10, 20, 30, 40, 50]
listy = [100, 200, 300, 400, 500]
plt.plot(listx, listy, color='green', ls='--', lw='2.0', label='label')
plt.legend()
plt.show()
'''
# Sanple 2. 設定標題
#title('', fontsize=) / xlabel('', fontsize=) / ylabel('', fontsize=)
'''
listx = [10, 20, 30, 40, 50]
listy = [100, 200, 300, 400, 500]
plt.plot(listx, listy, color='green', ls='--', lw='2.0', label='label')
plt.title('Chart Title', fontsize=14)
plt.xlabel('X-label', fontsize=14)
plt.ylabel('Y-label', fontsize=14)
plt.legend()
plt.show()
'''

# Sanple 3. 設定範圍
#xlim() / ylim()
'''
listx = [10, 20, 30, 40, 50]
listy = [100, 200, 300, 400, 500]
plt.plot(listx, listy, color='green', ls='--', lw='2.0', label='label')
plt.title('Chart Title', fontsize=20)
plt.xlabel('X-label', fontsize=14)
plt.ylabel('Y-label', fontsize=14)
plt.xlim(0, 100)
plt.ylim(0, 1000)
plt.legend()
plt.show()
'''

# Sanple 4. 設定座標刻度
#plt.tick_params(axis='', labelsize= , color= ) 
#plt.yticks(range(0, 5500, 500))
'''
listx = [10, 20, 30, 40, 50, 60]
listy = [100, 200, 300, 400, 500, 5000]
plt.plot(listx, listy)
#plt.ylim(0, 1000)
plt.yticks(range(0, 5500, 500))
#plt.ylim(0, 1000)
plt.tick_params(axis='both', labelsize=10, color='red')
plt.show()
'''
# Sanple 5. 設定格線
#grid(color='', linestyle=":", linewidth='', alpha= )
'''
listx = [10, 20, 30, 40, 50]
listy = [100, 200, 300, 400, 500]
plt.plot(listx, listy, color='green', ls='--', lw='2.0', label='label')
plt.title('Chart Title')
plt.xlabel('X-label', fontsize=14)
plt.ylabel('Y-label', fontsize=14)
plt.xlim(0, 100)
plt.ylim(0, 1000)
plt.grid(color='black', linestyle=":", linewidth='1', alpha=0.5 )
plt.legend()
plt.show()
'''

# Sanple 6. 多組資料
'''
listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1, 'r-.s')
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2, 'y-s')
plt.show()
'''
# Sanple 7. 多組資料一起繪圖
'''
listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
listx3 = [3, 9, 11, 17, 19, 22]
listy3 = [66, 45, 99, 77, 46, 50]
plt.plot(listx1, listy1, 'r-.s', listx2, listy2, 'y-s', listx3, listy3, 'b-')
plt.show()
'''

# Sample 8:折線圖
'''
year = [2016, 2017, 2018, 2019, 2020]
city1 = [100, 180, 90, 220, 150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label='Taipei')
city2 = [160, 50, 120, 140, 110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label='Kaohsiung')
plt.legend()
plt.ylim(0, 250)
plt.xticks(year)
plt.title('Sales Report', fontsize=18)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Million', fontsize=12)
plt.grid(color='k', linestyle=':', linewidth='1', alpha=0.5 )
plt.show()
'''

# Sample 9:顯示中文
#plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' #微軟正黑字形
#plt.rcParams['axes.unicode_minus'] = False
'''
year = [2016, 2017, 2018, 2019, 2020]
city1 = [100, 180, 90, 220, 150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label='台北')
city2 = [160, 50, 120, 140, 110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label='高雄')
plt.legend()
plt.ylim(0, 250)
plt.xticks(year)
plt.title('銷售報表', fontsize=18)
plt.xlabel('年度', fontsize=12)
plt.ylabel('百萬', fontsize=12)
plt.grid(color='k', linestyle=':', linewidth='1', alpha=0.5 )
#設定中文字型以及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' #微軟正黑字形
plt.rcParams['axes.unicode_minus'] = False
plt.show()
'''

#範例二
#類型一 長條圖
# Sample1. 直條圖
#plt.bar(listx, listy, color='b', width=0.5)

'''
listx = ['c', 'c++', 'c#', 'java', 'python']
listy = [45, 28, 38, 32, 50]
plt.bar(listx, listy, color='b', width=0.5)
plt.title('資訊城市課程選修人數')
plt.xlabel('程式課程')
plt.ylabel('選修人數')
#設定中文字型以及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' #微軟正黑字形
plt.rcParams['axes.unicode_minus'] = False
plt.show()
'''


#類型一 長條圖
# Sample2. 橫條圖
#plt.barh(listx, listy, color='b', height=0.5) 
'''
listy = ['c', 'c++', 'c#', 'java', 'python']
listx = [45, 28, 38, 32, 50]
plt.barh(listy, listx, color='b', height=0.5)         #注意位置(y)在先
plt.title('資訊城市課程選修人數')
plt.xlabel('程式課程')
plt.ylabel('選修人數')
#設定中文字型以及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' #微軟正黑字形
plt.rcParams['axes.unicode_minus'] = False             #中字不會被拆開
plt.show()
'''

#類型一 長條圖
# Sample3. 堆疊長條圖
#plt.bar(listx, listy2,  width=0.5, bottom=listy1, label='男')
'''
listx = ['c', 'c++', 'c#', 'java', 'python']
listy1 = [25, 20, 30, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx, listy1,  width=0.5, label='男')
plt.bar(listx, listy2,  width=0.5, label='女', bottom=listy1)
#注意 bottom的位置
plt.legend()
plt.title('資訊城市課程選修人數')
plt.xlabel('程式課程')
plt.ylabel('選修人數')
#設定中文字型以及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' #微軟正黑字形
plt.rcParams['axes.unicode_minus'] = False
plt.show()
'''

#類型一 長條圖
# Sample3. 並列長條圖
#listx1 = [x - width/2 for x in range(len(listx))]
#listx2 = [x + width/2 for x in range(len(listx))]
'''
width = 0.25
listx = ['c', 'c++', 'c#', 'java', 'python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]

listy1 = [25, 20, 30, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx1, listy1,  width, label='男')
plt.bar(listx2, listy2,  width, label='女')
#plt.xticks(range(len(listx)), labels=listx)
#plt.xticks((listx), labels=listx)                          #看不懂???
plt.legend()
plt.title('資訊城市課程選修人數')
plt.xlabel('程式課程')
plt.ylabel('選修人數')
#設定中文字型以及負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
plt.rcParams['axes.unicode_minus'] = False
plt.show()
'''

# 類型二 散佈圖
#scale = [x**3 for x in [5 , 4, 2, 6, 7, 1, 8, 9, 2, 3, 2, 4, 5, 7, 2]]
#plt.scatter(listx, listy, c='b', s=scale, marker='0', alpha=0.5)
'''
listx = [31, 15, 20, 25, 12, 18, 45, 21, 33, 5, 18, 22, 37, 42, 10]
listy = [68, 20, 61, 32, 45, 56, 10, 18, 70, 64, 43, 66, 19, 77, 21]

scale = [x**3 for x in [5, 4, 2, 6, 7, 1, 8, 9, 2, 3, 2, 4, 5, 7, 2]]
plt.scatter(listx, listy, c='b', s=scale, marker='o', alpha=0.5)

plt.xlim(0, 50)
plt.ylim(0, 80)
plt.show()
'''

# 類型三 圓餅圖
#plt.pie(sizes,explode,colors,labels,
#         labeldistance, pctdistance, autopct = '%2.1f%%', 
#         shadow, startangle)
'''
sizes = [25, 30, 15, 10]
labels = ['北部', '西部', '南部', '東部']
#colors = ['r', 'b', 'y', 'g']
explode = (0, 0, 0.2, 0.15)
plt.pie(sizes, 
        explode = explode,
        labels = labels,
        #colors = colors,
        labeldistance = 1.1,
        autopct = '%2.1f%%',
        pctdistance = 0.5,
        shadow = True,
        startangle = 0)

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False
plt.show()
'''





#範例三 程式實作
# Sample1 設定圖表區
#新增圖表區
'''
plt.figure()
plt.plot([1,2,3])
'''
#新增圖表區並設定屬性
'''
plt.figure(figsize=[8, 4], dpi=84, facecolor='whitesmoke', edgecolor='r', linewidth=1, frameon=True)

plt.plot([1,2,3])
plt.show()
'''

# Sample2 圖表區中，加入多張圖表 2列1欄
#plt.subplot(211)、plt.subplot(212)
'''
plt.figure(figsize=[8, 8])

plt.subplot(211)
plt.title(label='Chart 1')
plt.plot([1,2,3], 'r:o')

plt.subplot(212)
plt.title(label='Chart 2')
plt.plot([1,2,3], 'g--o')
plt.show()
'''

# Sample3 圖表區中，加入多張圖表 1列2欄
#plt.subplot(121)、plt.subplot(122)
'''
plt.figure(figsize=[8,8])

plt.subplot(121)
plt.title('Chart 1')
plt.plot([1,2,3], 'r:*')

plt.subplot(122)
plt.title('Chart 2')
plt.plot([1,2,3], 'g--s')

plt.show()
'''

# Sample 4 圖表區中，加入多張圖表 2列2欄
'''
#plt.figure(figsize=[8,8])
plt.figure(figsize=[16,16])
#plt.figure(figsize=[32,32])
#折線圖1
plt.subplot(441)
plt.title('Chart 1')
plt.plot([1,2,3], 'r:*')
#折線圖2
plt.subplot(442)
plt.title('Chart 2')
plt.plot([1,2,3], 'g--s')
#長條圖
plt.subplot(443)
plt.title('Chart 3')
plt.bar([1,2,3], [4,5,6], width=0.5)
#橫條圖
plt.subplot(444)
plt.title('Chart 4')
plt.barh([1,2,3], [4,5,6], height=0.5)
#推疊長條圖
plt.subplot(445)
plt.title('Chart 5')
x = ['kid','man','elder']
plt.bar(x, [1,2,3],  width=0.5)
plt.bar(x, [4,5,6],  width=0.5, bottom=[1,2,3])
#並列長條圖  (#記住!!!! plt.xticks(range(len()), labels= )
plt.subplot(446)
plt.title('Chart 6')
width = 0.25
x = ['kid','man','elder']
x1 = [x-width/2 for x in range(len(x))]
x2 = [x+width/2 for x in range(len(x))]

plt.bar(x1, [1,2,3],  width)
plt.bar(x2, [4,5,6],  width)
plt.xticks(range(len(x)), labels=x)        

#散布圖 記住!!! s = scale
plt.subplot(447)
plt.title('Chart 7')
x = ['k','m', 'f', 'e', 'ch']
y = [11,25,15,8,1]
scale = [x**3 for x in [4,5,10,2,6.2]]
plt.scatter(x, y, s=scale, alpha=0.5)

#圓餅圖 explode、autopct='%2.f%%'、shadow、startangle
plt.subplot(448)
plt.title('Chart 8')
x = ['kid','man','elder']
y = [1,2,3]
explode = (0, 0, 0.1)
plt.pie(y, labels=x,  autopct='%2.f%%',explode=explode, shadow=True, startangle=0)

plt.show()
'''

# Sample 5 圖表區中，加入多張圖表 相對位置、距離
#plt.axes([x軸距, y軸距, 寬, 高])                                 
'''
plt.figure(figsize=[8, 4])

plt.axes([0,0,0.4,1])
plt.title(label= 'Chart 1')
plt.plot([1,2,3], 'r:o')

plt.axes([0.5,0,0.4,1])
plt.title(label= 'Chart 2')
plt.plot([1,2,3], 'g--s')

plt.show()
'''
# Sample 6 圖表區中，加入多張圖表 子母圖表
'''
plt.figure(figsize=[8, 4])

plt.axes([0,0,0.8,1])
plt.title(label= 'Chart 1')
plt.plot([1,2,3], 'r:o')

plt.axes([0.55,0.1,0.2,0.2])
plt.title(label= 'Chart 2')
plt.plot([1,2,3], 'g--s')

plt.show()
'''




























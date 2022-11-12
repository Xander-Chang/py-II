# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:19:33 2022

@author: user
"""

import xml.etree.ElementTree as ET

tree = ET.parse('sample_country.xml')
root = tree.getroot()
#print(root.tag)                      #root屬性
#print(root.attrib)                   #attrib屬性,以字典方式呈現
#print(root.text)                     #節點內容

#for child in root:                    #找出子節點與屬性
#    print(child.tag, child.attrib)

#for neighbor in root.iter('neighbor'): #搜尋所有子節點-iter 可以在指定節點之下,以地回方式搜尋所有子節點
#    print(neighbor.attrib)

for country in root.findall('country'): #findall 從第一子層中搜尋,傳回所有子節點
    rank = country.find('rank').text    #find 從子第一子層找一個子節點
    name = country.get('name')
    print(name, rank)

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:45:41 2022

@author: user
"""

import xml.etree.ElementTree as ET
tree = ET.parse('view-source_https___w3.feitsui.gov.tw_FeitsuiWebService_tpe_Feitsui_Hourly.asmx_RESOIR_RAIN_HOUR.xml')
root = tree.getroot()

for Table1 in root.iter('Table1'):
    time = Table1.find('時間', )
    height = Table1.find('水位').text
    storage = Table1.find('有效蓄水量').text
    percentage = Table1.find('有效蓄水量百分比').text
    print(time,'\n',height,'\n',storage,'\n',percentage)
    
    
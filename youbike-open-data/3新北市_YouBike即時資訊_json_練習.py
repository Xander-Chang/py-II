import requests

#開放資料：'YouBike新北市公共自行車即時資訊'
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json"
html = requests.get(url)

json_datas = html.json()   #將回傳內容轉換成json格式
print(json_datas)
print('= '*60)
for json_data in json_datas:
    print('站點代號:\t',json_data['sno'],\
          '場站名稱(中文):\t',json_data['sna'],\
          '場站總停車格:\t',json_data['tot'],\
          '場站目前車輛數量:\t',json_data['sbi'],\
          '場站區域(中文):\t',json_data['sarea'],\
          '資料更新時間:\t',json_data['mday'],\
          '緯度:\t',json_data['lat'],\
          '經度:\t',json_data['lng'],\
          '地:\t',json_data['ar'],\
          '場站區域(英文):\t',json_data['sareaen'],\
          '場站名稱(英文):\t',json_data['snaen'], \
          '地址(英文):\t', json_data['aren'], \
          '空位數量:\t', json_data['bemp'],
          '全站禁用狀態:\t', json_data['act'],\
          )

'''
#資料欄位說明
sno：站點代號
sna：場站名稱(中文)
tot：場站總停車格
sbi：場站目前車輛數量
sarea：場站區域(中文)
mday：資料更新時間
lat：緯度
lng：經度
ar：地(中文)
sareaen：場站區域(英文)
snaen：場站名稱(英文)
aren：地址(英文)
bemp：空位數量
act：全站禁用狀態 
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:35:29 2022

@author: user
"""
import sqlite3
# fetchone():
# fetchall():
# rowcount:

def menu():
    usage = ('\tL/l: 顯示所有會員資料',
             '\tD/d: 刪除會員資料',
             '\tA/a: 新增會員',
             '\tQ/q: 離開系統',
             '\tH/h: 幫助/說明')
    print('Main menu'.center(70, '='))
    for i in usage:
        print(i)



def main(): 
    print('歡迎來到會員資料系統')    
    menu()
    while True:
        command = input('請選擇你需要的服務:')
        print()
        if command in ('L', 'l'):
            listInformation()
        elif command in ('D', 'd'):
            remove()
            menu()
        elif command in ('A', 'a'):
            add()
            menu()
        elif command in ('Q', 'q'):
            break
        elif command in ('H', 'h'):
            menu()
        else:
            print('\t你的輸入有誤, 請重新輸入')



def doSql(sql):
    '''用來執行 SQL, 尤其是 insert / delete'''
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    
    
    
def exist(recordId):
    '''用來測試數據表中是否存在recordId的id'''
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute('SELECT COUNT(id) from addressList where id=' + str(recordId))
    c = cur.fetchone()[0]
    conn.close()
    return c!=0
    
    
    
def listInformation():
    '''查看所有紀錄'''
    sql = 'SELECT * FROM addressList ORDER BY id ASC'
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    if not result:
        print('\tDatabase has no record at this time.')
    else:
        #格式化輸出所有紀錄
        print('All record'.center(70,'='))
        print('Id     Name     Sex     Age     Department     Telephone     LINE')
        for record in result:
            print(str(record[0]).ljust(7), end='')
            print(record[1].ljust(9), end='')
            print(record[2].ljust(8), end='')
            print(str(record[3]).ljust(8), end='')
            print(record[4].ljust(15), end='')
            print(record[5].ljust(14), end='')
            print(record[6])
        print('='*30)
    conn.close()



def remove():
    print('Delete records'.center(70,'='))
    while True:
        x = input('請輸入 ID 進行 delete / (輸入Q/q 可以離開):\n')
        if x in ('q','Q'):
            print('\t You have stopped removing record.')
            return
        try:
            recordId = int(x)
            if not exist(recordId):
                print('\tThis id does not exists.')
            else:
                sql = 'DELETE FROM addressList where id=' + x
                doSql(sql)
                print('\tYou have deleted a record.')
        except:
            print('\tid must be an integer')
            


def add():
    print('Add record'.center(70,'='))
    while True:
        record = input('Please input name, sex, age, department, telephone, qq(Q/q to return):\n')
        if record in ('q','Q'):
            print('\tYou have stopped adding record.')
            return
        #正確的格式應該包含 5 個英文逗號
        if record.count(',') != 5:
            print('\tformat or data error.')
            continue
        else:
            name, sex, age, department, telephone, qq = record.split(',')
            # 性別必為 F / M
            if sex not in ('F','M'):
                print('\tsex must be F or M.')
                continue
            # 手機號碼 和 LINE 必須是數字字串
            if (not telephone.isdigit()) or (not qq.isdigit()):
                print('\ttelephone and LINE must be integers.')
                continue
            # 年齡介於 1-130 之間整數
            try:
                age = int(age)
                if not 1 <= age <= 130:
                    print('\tage must be between 1 and 130.')
                    continue
            except:
                print('\tage must be an integer.')
                continue
        sql = 'INSERT INTO addressList(name,sex,age,department,telephone,qq) VALUES("'
        sql = sql + name + '","' + sex + '",' + str(age) + ',"' + department + '","'
        sql = sql + telephone + '","' + qq + '")'
        doSql(sql)
        print('\tYou have add a record.')
main()
import os
os.system("pause")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
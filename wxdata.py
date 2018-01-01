# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:18:08 2017

@author: lianxiaorui
"""

import itchat 
import json
from pandas import DataFrame 
#爬取自己好友相关信息， 返回一个json文件 
#friends = itchat.get_friends(update=True)[0:] 
#itchat.send('Message Content', '微信传输助手')

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]
DataFrame(friends).to_excel('friends_data.xls', index=True)
def friends_sex(friends):
    male = female = other = 0 
    #friends[0]是自己的信息，所以要从friends[1]开始 
    for i in friends[1:]: 
        sex = i["Sex"] 
        if sex == 1: 
            male += 1 
        elif sex == 2: 
            female += 1 
        else: 
            other +=1 
    #计算朋友总数 
    total = len(friends[1:]) 
    #打印出自己的好友性别比例 
    print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" + 
    "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" + 
    "不明性别好友： %.2f%%" % (float(other) / total * 100)) 
#friends_sex(friends)
#定义一个函数，用来爬取各个变量 
def get_var(var): 
    variable = [] 
    for i in friends: 
        value = i[var] 
        variable.append(value) 
    return variable 
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面 
NickName = get_var("NickName") 
Sex = get_var('Sex') 
Province = get_var('Province') 
City = get_var('City') 
Signature = get_var('Signature') 

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 
        'City': City, 'Signature': Signature} 
frame = DataFrame(data) 
frame.to_excel('1data.xls', index=True) 
itchat.run()

#itchat.logout()
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:01:19 2017

@author: lianxiaorui
"""
from pandas import DataFrame as df
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import operator
import itchat
import json
print("正在打印登录二维码...")
itchat.auto_login(hotReload=False)
friends = itchat.get_friends(update=True)[0:]
DataFrame(friends).to_excel('friends_data.xls')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.style.use("ggplot")  
friends=pd.read_excel("friends_data.xls")

#朋友圈好友男女比例
man_num=len(friends['Sex'][friends['Sex']==1])
woman_num=len(friends['Sex'][friends['Sex']==2])
other_num=len(friends['Sex'][friends['Sex']==0])
sex=['男','女','女博士']
num=[man_num,woman_num,other_num]
width=0.35
explode = (0.1,0.1,0.1)
patches,l_text,p_text =plt.pie(num,explode=explode,labels=sex,autopct='%1.2f%%',shadow = True)
plt.axis('equal')
plt.legend()
plt.title("微信好友男女比例")
X=np.arange(3)
for x,y in zip(X,num):
   plt.text(x+0.03, y+10,str(round(y/len(friends['Sex'])*100,3))+"%", ha='center', va= 'bottom',fontsize=16)
plt.savefig("sex_rate.jpg")
plt.show()
#朋友圈好友在哪个市
city=friends['City'].dropna()
city_dict={}
cities=[]
for i in list(city):
   if i not in cities:
       cities.append(i)
       city_dict[i]=1
   else:
       city_dict[i]+=1
city_dict=dict(sorted(city_dict.items(),key=operator.itemgetter(1),reverse=True))
j=0
city_name=[]
peo_num=[]
for i in city_dict:
   if j<10:
       city_name.append(i)
       peo_num.append(city_dict[i])
   j+=1
plt.title("微信好友在哪个城市")
plt.bar(np.arange(10)+1,peo_num,0.8,color=['b','y','r'])
plt.xticks(np.arange(10)+1,tuple(city_name),fontsize=14)
for x,y in zip(np.arange(10)+0.9,peo_num):
   plt.text(x, y+1,y, ha='center', va= 'bottom',fontsize=14)
plt.savefig("frinds_where.jpg")
plt.show()
itchat.run()
#朋友圈好友在哪个省
#province=friends['Province'].dropna()
#pro_dict={}
#provinces=[]
#for i in list(province):
#    if i not in provinces:
#        provinces.append(i)
#        pro_dict[i]=1
#    else:
#        pro_dict[i]+=1
#pro_dict=dict(sorted(pro_dict.items(),key=operator.itemgetter(1),reverse=True))
#for i in pro_dict:
#    print(str(i)+":"+str(pro_dict[i])+"人")
#个性签名分析

# import re
# siglist = []
# signature=friends["Signature"].dropna()
# for i in signature:
#     s =i.strip().replace("span","").replace("class","").replace("emoji","")
#     rep = re.compile("1f\d+\w*|[<>/=]")
#     s = rep.sub("", s)
#     siglist.append(s)
# text = "".join(siglist)
# import jieba
# wordlist = jieba.cut(text, cut_all=True)
# word_space_split = " ".join(wordlist)
#
#
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import numpy as np
# import PIL.Image as Image
# coloring = np.array(Image.open("C:\\Users\\lianxiaorui\\Pictures\\Camera Roll\\1.jpg"))
# my_wordcloud = WordCloud(background_color="white", max_words=2000,
#                          mask=coloring, max_font_size=60, random_state=42, scale=2,
#                          font_path="C:\\Users\\lianxiaorui\\Downloads\\simheittf\\SimHei.ttf").generate(word_space_split)
#
# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.savefig("cloud.jpg")
# plt.show()



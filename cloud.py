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
friends=DataFrame(friends)

import re
siglist = []
signature=friends["Signature"].dropna()
for i in signature:
    s =i.strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    s = rep.sub("", s)
    siglist.append(s)
text = "".join(siglist)
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("C:\\Users\\lianxiaorui\\Pictures\\Camera Roll\\1.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="C:\\Users\\lianxiaorui\\Downloads\\simheittf\\SimHei.ttf").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.savefig("cloud.jpg",dpi=200)
plt.show()


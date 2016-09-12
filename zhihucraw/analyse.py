# -*- coding: utf-8 -*-
# encoding:utf-8

import sys


#sys.setdefaultencoding("utf-8")

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
data = pd.read_csv("output.csv")
font=FontProperties(fname=r'/usr/share/fonts/truetype/字体管家扁黑体.ttf',size=14)

'''
sr=data['user_education_school'].value_counts()[:30]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎大学分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,30)
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 ,fontproperties=font)
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''
'''
sr=data[data['user_gender']=='female']['user_education_school'].value_counts()[:30]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎女性大学分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,30)
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 ,fontproperties=font)
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''

'''
sr=data[data['user_education_school']=='北京大学']['user_education_subject'].value_counts()[:30]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎北京大学专业分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,30)
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 ,fontproperties=font)
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''

'''
sr=data['user_employment'].value_counts()[:30]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎公司分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,30)
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0,fontproperties=font)
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''

'''
plt.plot(data[data['user_followers']>50]['user_followers'].order(),np.arange(len(data[data['user_followers']>50])),color='blue',alpha=0.6)
plt.scatter(data[data['user_followers']>50]['user_followers'].order(),np.arange(len(data[data['user_followers']>50])),color='purple',alpha=0.6)
plt.title("知乎被关注者数(>50)分布",fontproperties=font)
plt.show()
'''



sr=data['user_gender'].value_counts()


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎性别分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)),sr.values, align = 'center',alpha=0.4,color="red")
ax.set_ylim(-1,2)
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 ,fontproperties=font)
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()



'''
sr=data[((data['专业']=='计算机科学')|(data['专业']=='软件工程')|(data['专业']=='计算机')|(data['专业']=='计算机科学与技术')|(data['专业']=='通信工程')|(data['专业']=='计算机科学与技术'))]['公司'].value_counts()[:30]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎计算机相关专业公司分布")
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 )
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''
'''
sr=data[((data['专业']=='金融')|(data['专业']=='经济学')|(data['专业']=='计算机')|(data['专业']=='金融学')|(data['专业']=='市场营销')|(data['专业']=='会计'))]['公司'].value_counts()[:30]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎金融相关专业公司分布")
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 )
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''
'''
sr=data[((data['专业']=='计算机科学')|(data['专业']=='软件工程')|(data['专业']=='计算机')|(data['专业']=='计算机科学与技术')|(data['专业']=='通信工程')|(data['专业']=='计算机科学与技术'))]['所在地'].value_counts()[:30]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎计算机相关专业所在地分布")
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 )
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()
'''
'''
sr=data[((data['专业']=='金融')|(data['专业']=='经济学')|(data['专业']=='计算机')|(data['专业']=='金融学')|(data['专业']=='市场营销')|(data['专业']=='会计'))]['所在地'].value_counts()[:30]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎金融相关专业所在地分布")
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 )
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()

'''
'''
sr=data[data['所在地']=='北京']['公司'].value_counts()[:30]



fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎北京公司分布")
rects1 = ax.barh(range(len(sr.values)),sr.values[::-1], align = 'center',alpha=0.6,color="purple")
ax.set_ylim(-1,len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0 )
ax.set_xlim(0,max(sr.values)*1.1)
plt.show()

'''

'''
sr = data[data['user_location'] == '上海']['user_employment_extra'].value_counts()[:30]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("知乎上海职位分布",fontproperties=font)
rects1 = ax.barh(range(len(sr.values)), sr.values[::-1], align='center', alpha=0.6, color="purple")
ax.set_ylim(-1, len(sr))
ax.set_yticks(range(len(sr.values)))
ax.set_yticklabels(sr.index[::-1], rotation=0,fontproperties=font)
ax.set_xlim(0, max(sr.values) * 1.1)
plt.show()
'''
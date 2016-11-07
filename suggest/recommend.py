# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 18:47:40 2016

@author: Albert
"""

from random import choice
import pymysql
pymysql.install_as_MySQLdb()

def recommend(user):
    #连接数据库
    DB=pymysql.connect("localhost","root","root","recommend")
    #获得数据库游标
    c=DB.cursor()

    #下面代码为实现从数据库中得到用户user所喜欢的番剧编号，以便判断重复
    love=[]
    #sql语句
    sql="select anime_id  from user_anime where user_id=%s"%user
    c.execute(sql)
    #得到结果集
    results=c.fetchall()
    for line in results:
        love.append(line[0])

    #下面代码实现得到用户所喜欢top3类型
    sql='''
    select style_id   from
        (select user_id,style_id from
        (select user_id,anime_id as id from user_anime where user_id=%s) as s
        natural join anime natural join
        (select anime_id as id,style_id from anime_style) as n
         )as temp group by style_id order by count(user_id) desc limit 3;'''%user

    c.execute(sql)
    results=c.fetchall()
    lis=[]
    anime={}
    for (line,) in results:

        lis.append(line)
    for i in lis:
        #从番剧信息的数据库中得到Top3各个类别的所有番剧并存入anime字典中
        sql="select anime_id from anime_style where style_id="+str(i)+";"
        c.execute(sql)
        results=c.fetchall()
        anime_lis=[]
        for result in results:
            anime_lis.append(result[0])
        #类型为key，值为存放番剧数据的列表
        anime[str(i)]=anime_lis
    #建立三个类别番剧的set（集合），并取交集，即得到同时有三个类型标签的番剧
    s=set(anime[str(lis[0])])&set(anime[str(lis[1])])&set(anime[str(lis[2])])

    #建立用户喜欢番剧的集合
    loveSet=set(love)
    #如果系统得到的所有番剧用户均已看过了即loveSet>s，就从Top1类型即最喜欢的类型中挑选一个
    #这里我们默认数据库量够大，即用户没有把一个类别的所有番剧看完
    if loveSet>s:
        s=set(anime[str(lis[0])])

    #把集合转化为列表以待随机函数的使用
    set_lis=[]
    for i in s:
        set_lis.append(i)
    #从结果中随机挑选
    recommend=choice(set_lis)
    #直至挑选到用户没看过的
    while  recommend in love:
        recommend=choice(set_lis)
    dic={}
    #得到推荐番剧的相关信息，返回以待使用，显示
    sql="select name,brief from anime where id="+str(recommend)+";"
    c.execute(sql)
    results=c.fetchall()
    dic['name']=results[0][0]
    dic['brief']=results[0][1]

    DB.close()
    return dic




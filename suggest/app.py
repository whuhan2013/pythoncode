# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:45:40 2016

@author: Albert
"""

from flask import Flask,render_template,request
import recommend
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search/')
def search():
    #request为全局变量可得到用户输入信息
    n=request.args.get('user')
    #调用推荐函数
    dic=recommend.recommend(n)
    #用返回结果进行模板渲染
    return render_template('search.html',Data=dic)
if __name__=="__main__":
    app.run(debug=True)
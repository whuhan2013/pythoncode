import requests
from random import randint
from lxml import etree
from flask import Flask, request, make_response
import hashlib


url="http://www.qiushibaike.com/text/"
print("here1")
r = requests.get(url)
tree = etree.HTML(r.text)
contentlist = tree.xpath('//div[@class="content"]/span/text()')
jokes = []
#print("here2",contentlist[0])

for i in contentlist:

    contentstring = ''.join(i)
    contentstring = contentstring.strip('\n')
    #print(contentstring,'\n')
    jokes.append(contentstring)

joke = jokes[randint(0, len(jokes))]
print(joke)
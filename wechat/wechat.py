#coding:utf-8
import requests
from random import randint
from lxml import etree
from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        print('coming Get')
        data = request.args
        token = 'weixin'
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s).encode("utf-8")
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)

    if request.method == 'POST':
        xml_str = request.stream.read()
        xml = ET.fromstring(xml_str)
        toUserName = xml.find('ToUserName').text
        fromUserName = xml.find('FromUserName').text
        createTime = xml.find('CreateTime').text
        msgType = xml.find('MsgType').text
        if msgType != 'text':
            reply = '''
                <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                </xml>
                ''' % (
                fromUserName,
                toUserName,
                createTime,
                'text',
                'Unknow Format, Please check out'
            )
            return reply
        content = xml.find('Content').text
        msgId = xml.find('MsgId').text
        if u'笑话' in content:
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
                jokes.append(contentstring)
            #print("here3",jokes)
            joke = jokes[randint(0, len(jokes))]
            reply = '''
                            <xml>
                            <ToUserName><![CDATA[%s]]></ToUserName>
                            <FromUserName><![CDATA[%s]]></FromUserName>
                            <CreateTime>%s</CreateTime>
                            <MsgType><![CDATA[%s]]></MsgType>
                            <Content><![CDATA[%s]]></Content>
                            </xml>
                            ''' % (fromUserName, toUserName, createTime, msgType, joke)
            return reply
        else:
            if type(content).__name__ == "unicode":
                content = content[::-1]
                content = content.encode('UTF-8')
            elif type(content).__name__ == "str":
                print(type(content).__name__)
                content = content
                content = content[::-1]
            reply = '''
                            <xml>
                            <ToUserName><![CDATA[%s]]></ToUserName>
                            <FromUserName><![CDATA[%s]]></FromUserName>
                            <CreateTime>%s</CreateTime>
                            <MsgType><![CDATA[%s]]></MsgType>
                            <Content><![CDATA[%s]]></Content>
                            </xml>
                            ''' % (fromUserName, toUserName, createTime, msgType, content)
            return reply
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

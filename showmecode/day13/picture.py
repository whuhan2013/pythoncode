from html.parser import HTMLParser
import urllib.request
import requests

class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.picUrls=[]

    def handle_starttag(self, tag, attrs):
        if tag=="img":
            if len(attrs)>0:
                for key,value in attrs:
                    if key=="src":
                        self.picUrls.append(value)

def Pic(picurls):
    count=1
    for picurl in picurls:
        conn=urllib.request.urlopen(picurl)
        f=open(str(count)+".jpg",'wb')
        f.write(conn.read())
        f.close()
        count+=1

if __name__=='__main__':
    html=requests.get("http://tieba.baidu.com/p/2166231880")

    htmlParser=MyHtmlParser()
    htmlParser.feed(html.text)
    htmlParser.close()

    Pic(htmlParser.picUrls)

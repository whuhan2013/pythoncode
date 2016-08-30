
from html.parser import HTMLParser
from re import sub
import urllib.request
import sys
import requests

class HTMLParserMainText(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text=[]

    def handle_startendtag(self, tag, attrs):
        for key,value in attrs:
            if value and 'http' in value:
                self.text.append(''.join(value)+'\n')


def GetLinks():
    url = "http://www.cnbeta.com/"
    res = requests.get(url)
    
    parser=HTMLParserMainText()
    parser.feed(res.text)
    parser.close()

    return ''.join(parser.text)

if __name__=="__main__":
    print(GetLinks())

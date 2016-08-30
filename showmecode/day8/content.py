# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re
import urllib.request
import sys
import requests

class HtmlParserMainText(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.text.append("\n")

    def handle_data(self, data):
        if len(data.strip()) > 0:
            self.text.append(data.strip())



def GetMainText():
    url = "http://localhost:8080/Test/"
    res = requests.get(url)


    html_code = re.sub('<script[^>]*?>[^>]*?</script>','',res.text.strip()) #delete all scripts



    parser = HtmlParserMainText()
    parser.feed(html_code)
    parser.close()

    return ''.join(parser.text).strip()

if __name__ == '__main__':
    print(GetMainText().encode('utf-8').decode())
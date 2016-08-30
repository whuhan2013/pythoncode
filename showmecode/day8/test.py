#-*- coding:utf-8 -*-
import requests
import re

url="http://localhost:8080/Test/"
r=requests.get(url)
html_code = re.sub('<script[^>]*?>[^>]*?</script>','',r.text.strip())
print(html_code.encode('utf-8'))


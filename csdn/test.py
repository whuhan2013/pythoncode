__author__ = 'MrChen'

import urllib.request
import re
import time
from bs4 import BeautifulSoup

p = re.compile('/whuhan2013/article/details/........')

# 自己的博客主页
url = "http://blog.csdn.net/whuhan2013"

# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

html = opener.open(url).read().decode('utf-8')

allfinds = p.findall(html)
# print(allfinds)

urlBase = "http://blog.csdn.net"  # 需要将网址合并的部分
# 页面中的网址有重复的，需要使用set进行去重复
mypages = list(set(allfinds))
for i in range(len(mypages)):
    mypages[i] = urlBase + mypages[i]

print('要刷的网页有：')
for index, page in enumerate(mypages):
    print(str(index), page)

# 设置每个网页要刷的次数
brushNum = 200

# 所有的页面都刷
print('下面开始刷了哦：')
for index, page in enumerate(mypages):
    for j in range(brushNum):
        try:
            pageContent = opener.open(page).read().decode('utf-8')
            # 使用BeautifulSoup解析每篇博客的标题
            soup = BeautifulSoup(pageContent)
            blogTitle = str(soup.title.string)
            blogTitle = blogTitle[0:blogTitle.find('-')]
            print(str(j), blogTitle)

        except urllib.error.HTTPError:
            print('urllib.error.HTTPError')
            time.sleep(3)  # 出现错误，停几秒先

        except urllib.error.URLError:
            print('urllib.error.URLError')
            time.sleep(3)  # 出现错误，停几秒先
        time.sleep(0.5)  # 正常停顿，以免服务器拒绝访问

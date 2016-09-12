# coding: utf-8
__author__ = 'Reed'

import urllib.request
import queue
import threading
from bs4 import BeautifulSoup
from pandas import Series
# import mysql.connector
from io import BytesIO
import gzip
import numpy


'''
class Desc(threading.Thread):
    def __init__(self, q_url, q_proxy):
        threading.Thread.__init__(self)
        self.q_url = q_url
        self.q_proxy = q_proxy
        self.flag = True

    def run(self):
        while 1:
            if not self.q_proxy.empty() and not self.q_url.empty():
                url = self.q_url.get()
                rqt = urllib.request.Request(
                    url=url,
                    headers={'User-Agent': 'Mozilla/5.0'})

                while 1:
                    if self.flag and not self.q_proxy.empty():
                        addr = self.q_proxy.get()
                    print(addr, self.name, url)
                    proxy_handler = urllib.request.ProxyHandler({'http': addr})
                    opener = urllib.request.build_opener(proxy_handler)
                    try:
                        page = opener.open(rqt, timeout=4).read().decode('utf-8')
                        print('%s read DESCOK!' % self.name)
                        self.flag = False
                        break
                    except:
                        print('%s read DESCFALSE' % self.name)
                        self.flag = True
                        q_proxy.task_done()
                        continue

                soup = BeautifulSoup(page)

                info = soup.select('#info')[0].text.encode('gbk', 'ignore').decode('gbk').replace(' ', '').replace('/', '').split('\n')
                infor = list(filter(lambda x: x, info))
                dct = dict()
                for i in range(len(infor)):
                    if infor[i].endswith(':'):
                        dct[infor[i][:-1]] = infor[i+1]
                    elif ':' in infor[i]:
                        k = infor[i].split(':')[0]
                        dct[k] = ''.join(infor[i].split(':')[1:])

                rate = soup.select('.rating_wrap')[0].select('strong')[0].text.replace(' ', '').replace('\n', '')
                raters = soup.select('.rating_wrap')[0].select('a')[0].text[:-3]
                title = soup.title.text.encode('gbk', 'ignore').decode('gbk')[:-5]

                dct['评分'] = rate
                dct['评分人数'] = raters
                dct['书名'] = title

                data = Series(dct, index=['书名', '作者', '译者', '评分', '评分人数', '定价', '出版社', '出版年', '页数', 'ISBN', '装帧', '副标题', '丛书', '原作名'])
                desc_book = list(data.replace(numpy.nan, ''))

                q_desc.put(desc_book)
                q_url.task_done()
'''
# 上面的Desc（注释掉了）和Book共用一个IP代理队列，其他速度均正常，只有Desc慢很多，有可能是资源竞争搞的，嗯，我猜
# 下面的Desc没有用代理，用本机访问，速度果然就恢复正常了，然后...就被封了
# 应该IP代理队列一分为二，效果应该会好，（免费代理，可用率惊的低人啊）


# 从每本书的详情主页，拿出图书信息，并格式化数据
class Desc(threading.Thread):
    def __init__(self, q_url):
        threading.Thread.__init__(self)
        self.q_url = q_url
        self.flag = True

    def run(self):
        while 1:
            if not self.q_url.empty():
                url = self.q_url.get()
                rqt = urllib.request.Request(
                    url=url,
                    headers={'User-Agent': 'Mozilla/5.0'})

                while 1:
                    opener = urllib.request.build_opener()
                    try:
                        page = opener.open(rqt, timeout=4).read().decode('utf-8')
                        self.flag = False
                        break
                    except:
                        self.flag = True
                        continue

                # 网页解析，而且雷特别多，比如 · 这个东西GBK无法编码，虽然utf8编码存到DB里，取的时候也可以修正，但是别扭
                # douban的html代码搞的有点复杂，所以格式化费劲了点，各种replace
                soup = BeautifulSoup(page)
                info = soup.select('#info')[0].text.encode('gbk', 'ignore').decode('gbk').replace(' ', '').replace('/', '').split('\n')
                infor = list(filter(lambda x: x, info))

                # 这个里就是在格式化数据，存到字典里，为后面pandas.Series格式化数据做好准备
                # 遗憾的是译者有多个的时候，无法全部取出
                dct = dict()
                for i in range(len(infor)):
                    if infor[i].endswith(':'):
                        dct[infor[i][:-1]] = infor[i+1]
                    elif ':' in infor[i]:
                        k = infor[i].split(':')[0]
                        dct[k] = ''.join(infor[i].split(':')[1:])

                # 取评分，评分人数，书名是上面忘了取
                rate = soup.select('.rating_wrap')[0].select('strong')[0].text.replace(' ', '').replace('\n', '')
                raters = soup.select('.rating_wrap')[0].select('a')[0].text[:-3]
                title = soup.title.text.encode('gbk', 'ignore').decode('gbk')[:-5]
                dct['评分'] = rate
                dct['评分人数'] = raters
                dct['书名'] = title

                # pandas.Series严格的按照index的顺序，排列dict.values()，空白处会置NAN(numpy.nan)，再次replace
                data = Series(dct, index=['书名', '作者', '译者', '评分', '评分人数', '定价', '出版社', '出版年', '页数', 'ISBN', '装帧', '副标题', '丛书', '原作名'])
                desc_book = list(data.replace(numpy.nan, ''))

                q_desc.put(desc_book)
                q_url.task_done()


# 从q_page队列里，取每一页的url然后获取每本书的url
class Book(threading.Thread):
    def __init__(self, q_page, q_proxy):
        threading.Thread.__init__(self)
        self.q_page = q_page
        self.q_proxy = q_proxy
        self.sign = True

    def run(self):
        while 1:
            if not self.q_page.empty() and not self.q_proxy.empty():
                page_url = self.q_page.get()
                rqt = urllib.request.Request(
                    url=page_url,
                    headers={'User-Agent': 'Mozilla/5.0'})

                # 内层while做到了，如果代理可用，那么下一次换url,不换代理
                # 如果代理不可用，下一次换代理，不换url
                while 1:
                    if self.sign and not self.q_proxy.empty():
                        addr = self.q_proxy.get()
                    proxy_handler = urllib.request.ProxyHandler({'http': addr})
                    opener = urllib.request.build_opener(proxy_handler)
                    try:
                        book_page = opener.open(rqt, timeout=4).read().decode('utf-8')
                        self.sign = False
                        break
                    except:
                        self.sign = True
                        q_proxy.task_done()
                        continue

                # BeautifulSoup脑残用法
                soup = BeautifulSoup(book_page)
                for dd in soup.select('dd'):
                    if dd.select('a'):
                        href = dd.select('a')[0].get('href')
                        q_url.put(href)
                q_page.task_done()


# 将格式化的数据，存到DB里
class DB(threading.Thread):
    def __init__(self, q_desc):
        threading.Thread.__init__(self)
        self.q_desc = q_desc

    def run(self):
        while 1:
            desc = q_desc.get()
            print(self.name)
            # con = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='douban')
            print('inset into table values %s' % ('/'.join(desc)))
            q_desc.task_done()

# 以上3个class均开启多线程, 与queue队列合作，不用过度关心锁等问题


# 正式开启线程爬book information之前，先爬好代理IP，放到队列
def get_proxy(proxy_url_lst):

    for each_url in proxy_url_lst:
        rqst = urllib.request.Request(each_url)
        rqst.add_header('User-Agent', 'Mozilla/5.0')

        # 这里response header返回的Content-Encoding是gzip，google到的方法是要解压
        # 其他网站有的也是这样，但是并不用解压，不明原因
        try:
            response = urllib.request.urlopen(rqst)
            if response.info().get('Content-Encoding') == 'gzip':
                buf = BytesIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                each_page = f.read()
            else:
                each_page = response.read()
        except urllib.request.URLError as r:
            print(r.reason)

        proxy_soup = BeautifulSoup(each_page)
        trs = proxy_soup.select('tbody > tr')

        for tr in trs:
            td = tr.find_all('td')
            proxy_addr = td[0].text + ':' + td[1].text
            q_proxy.put(proxy_addr)


def main():
    proxy_url_list = ['http://www.kuaidaili.com/free/intr/' + str(i) for i in range(1, 30)]
    get_proxy(proxy_url_list)

    page_url = ['http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/book?start=' + str(n) for n in range(0, 71985, 15)]
    for each in page_url:
        q_page.put(each)

    # 每项任务5个线程
    for i in range(5):
        book = Book(q_page, q_proxy)
        book.setDaemon(True)
        book.start()

        desc = Desc(q_url)
        desc.setDaemon(True)
        desc.start()

        db = DB(q_desc)
        db.setDaemon(True)
        db.start()


if __name__ == '__main__':
    q_url = queue.Queue()       # 每本书的url
    q_page = queue.Queue()      # 每页15本书概况的page url， tag:小说
    q_desc = queue.Queue()      # 每本书的详细描述信息（list）
    q_proxy = queue.Queue()     # 从代理IP网站爬下来的IP地址和端口，'127.0.0.1:8888'

    main()
    q_desc.join()
    print('Done!')
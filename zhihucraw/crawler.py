import requests
from lxml import html
from db import Zhihu_User_Profile
from red_filter import check_url, re_crawl_url
import random
import time

from bs4 import BeautifulSoup


class SpiderProxy(object):
    """黄哥Python培训 黄哥所写 Python版本为2.7以上"""
    headers = {
        "Host": "www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://www.xicidaili.com/wt/1",
    }

    def __init__(self, session_url):
        self.req = requests.session()
        self.req.get(session_url)

    def get_pagesource(self, url):
        html = self.req.get(url, headers=self.headers)
        return html.content

    def get_all_proxy(self, url, n):
        data = []
        for i in range(1, n):
            html = self.get_pagesource(url + str(i))
            soup = BeautifulSoup(html, "lxml")

            table = soup.find('table', id="ip_list")
            print(type(table))
            for row in table.findAll("tr"):
                cells = row.findAll("td")
                tmp = []
                for item in cells:

                    tmp.append(item.find(text=True))
                data.append(tmp[1:3])
        return data
class Zhihu_Crawler():

    '''
    basic crawler

    '''

    def __init__(self,url,option="print_data_out"):
        '''
        initialize the crawler

        '''

        self.option=option
        self.url=url
        self.header={}
        self.header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0"
#        self.header["Host"]="www.zhihu.com"
        self.header["Referer"]="www.zhihu.com"


        #cookie
        self.cookies={"q_c1":"a57da482190149c598ea41970ed39289|1472689490000|1472689490000",
                      "_xsrf":"bfdb84f58409e2f2b028b44a3e902d0b",
                       "d_c0":"AABAwkDceAqPTpwAGa9drbEiAVyxwnKIdLk=|1472689493",
                        " _zap":"56de3379-1be2-4fd4-8e32-e78e16c2d2e5",
                        "_za":"01619ad1-d465-4e22-89a4-8ac36b669864",
                        "a_t":'"2.0AADAlWcvAAAXAAAAB1vzVwAAwJVnLwAAAIDALVtgcQoXAAAAYQJVTdqD51cA5BWpP3Ia7DK9D31FNsVyKP043vAvISraCDclEqORCO9pgoL7d4uCQA=="',
                        "z_c0":"Mi4wQUFEQWxXY3ZBQUFBZ01BdFcyQnhDaGNBQUFCaEFsVk4yb1BuVndEa0Zha19jaHJzTXIwUGZVVTJ4WElvX1RqZThB|1472974343|dd5d7646eb4742626b9b40fd542bfc3dae0cb33b",
                       }

    def send_request(self):
        '''
        send a request to get HTML source

        '''
        added_followee_url = self.url.decode("utf-8") + "/followees"

        temp=random.randint(0,10)
        if temp<5:
            print("sleeping")
            time.sleep(3)

        session_url = 'http://www.xicidaili.com/wt/1'
        url = 'http://www.xicidaili.com/wt/'
        #p = SpiderProxy(session_url)
        proxy_ip ={
            "202.43.147.226",
            "117.166.183.111",
            "125.33.207.59",
            "218.94.149.147",
            "113.5.211.198",
            "110.73.8.230",
            "183.254.228.144",
            "111.1.3.36",
            "114.232.70.191",
            "183.224.99.151",
            "114.113.126.32"
        }

        try:

            r = requests.get(added_followee_url, cookies=self.cookies, headers=self.header, verify=False)
        except:
            re_crawl_url(self.url)
            print("here1")
            return



        content = r.text
        #print(content)
        if r.status_code == 200:
            self.parse_user_profile(content)

    def process_xpath_source(self, source):
        if source:
            #print(source[0])
            return source[0]
        else:
            return ''

    def parse_user_profile(self, html_source):
        '''
        parse the user's profile to mongo
        '''

        # initialize variances

        self.user_name = ''
        self.fuser_gender = ''
        self.user_location = ''
        self.user_followees = ''
        self.user_followers = ''
        self.user_be_agreed = ''
        self.user_be_thanked = ''
        self.user_education_school = ''
        self.user_education_subject = ''
        self.user_employment = ''
        self.user_employment_extra = ''
        self.user_info = ''
        self.user_intro = ''

        tree = html.fromstring(html_source)

        # parse the html via lxml
        self.user_name = self.process_xpath_source(tree.xpath("//a[@class='name']/text()"))
        self.user_location = self.process_xpath_source(tree.xpath("//span[@class='location item']/@title"))
        self.user_gender = self.process_xpath_source(tree.xpath("//span[@class='item gender']/i/@class"))
        if "female" in self.user_gender and self.user_gender:
            self.user_gender = "female"
        else:
            self.user_gender = "male"
        self.user_employment = self.process_xpath_source(tree.xpath("//span[@class='employment item']/@title"))
        self.user_employment_extra = self.process_xpath_source(tree.xpath("//span[@class='position item']/@title"))
        self.user_education_school = self.process_xpath_source(tree.xpath("//span[@class='education item']/@title"))
        self.user_education_subject = self.process_xpath_source(
            tree.xpath("//span[@class='education-extra item']/@title"))
        try:
            self.user_followees = tree.xpath("//div[@class='zu-main-sidebar']//strong")[0].text
            self.user_followers = tree.xpath("//div[@class='zu-main-sidebar']//strong")[1].text
        except:
            return

        self.user_be_agreed = self.process_xpath_source(
            tree.xpath("//span[@class='zm-profile-header-user-agree']/strong/text()"))
        self.user_be_thanked = self.process_xpath_source(
            tree.xpath("//span[@class='zm-profile-header-user-thanks']/strong/text()"))
        self.user_info = self.process_xpath_source(tree.xpath("//span[@class='bio']/@title"))
        self.user_intro = self.process_xpath_source(tree.xpath("//span[@class='content']/text()"))

        if self.option == "print_data_out":
            self.print_data_out()
        else:
            self.store_data_to_mongo()

            # find the follower's url
        #print("here2")
        url_list = tree.xpath("//h2[@class='zm-list-content-title']/span/a/@href")
        #print(url_list)
        for target_url in url_list:
            #print(target_url)
            target_url = target_url.replace("https", "http")
            check_url(target_url)

    def print_data_out(self):
        '''
        print out the user data
        '''

        print("*" * 60)
        print('用户名:%s\n' % self.user_name)
        print("用户性别:%s\n" % self.user_gender)
        print('用户地址:%s\n' % self.user_location)
        print("被同意:%s\n" % self.user_be_agreed)
        print("被感谢:%s\n" % self.user_be_thanked)
        print("被关注:%s\n" % self.user_followers)
        print("关注了:%s\n" % self.user_followees)
        print("工作:%s/%s" % (self.user_employment, self.user_employment_extra))
        print("教育:%s/%s" % (self.user_education_school, self.user_education_subject))
        print("用户信息:%s" % self.user_info)
        print("*" * 60)

    def store_data_to_mongo(self):
        '''
        store the data in mongo
        '''
        new_profile = Zhihu_User_Profile(
            user_name=self.user_name,
            user_be_agreed=self.user_be_agreed,
            user_be_thanked=self.user_be_thanked,
            user_followees=self.user_followees,
            user_followers=self.user_followers,
            user_education_school=self.user_education_school,
            user_education_subject=self.user_education_subject,
            user_employment=self.user_employment,
            user_employment_extra=self.user_employment_extra,
            user_location=self.user_location,
            user_gender=self.user_gender,
            user_info=self.user_info,
            user_intro=self.user_intro,
            user_url=self.url
        )
        new_profile.save()
        print("saved:%s \n" % self.user_name)

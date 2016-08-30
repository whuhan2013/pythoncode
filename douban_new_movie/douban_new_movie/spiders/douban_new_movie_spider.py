from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from douban_new_movie.items import DoubanNewMovieItem

class DoubanNewMovieSpider(Spider):
    name="douban_new_movie_spider"

    allowed_domains=["www.movie.douban.com"]

    # start_urls=[
    # 'http://movie.douban.com/chart'
    # ]

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.movie.douban.com/"
    }

    def start_requests(self):
        return [Request("http://movie.douban.com/chart", headers=self.headers)]

    def parse(self,response):
        sel=Selector(response)

        movie_name = sel.xpath("//a[@class='nbg']/@title").extract()
        movie_url=sel.xpath("//div[@class='pl2']/a/@href").extract()
        movie_star=sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()


        item=DoubanNewMovieItem()

        item['movie_name']=[n for n in movie_name]
        item['movie_star']=[n for n in movie_star]
        item['movie_url']=[n for n in movie_url]

        yield item

        #print(movie_name,movie_star,movie_url)
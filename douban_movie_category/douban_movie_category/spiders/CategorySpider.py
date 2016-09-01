from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from douban_movie_category.items import DoubanMovieCategoryItem
from scrapy.spiders import Rule,CrawlSpider
import jieba
class CategorySpider(CrawlSpider):
    name = "category_spider"
    download_delay = 1

    allowed_domains = []

    start_urls = [
        'http://movie.douban.com/top250?start=0&filter=',
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'\?start=\d+&filter=')),
             callback='parse_item'),)

    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanMovieCategoryItem()
        category = sel.xpath("//div[@class='info']/div[@class='bd']/p/text()").extract()

        print(type(category))
        x = []
        for i in category:

            if len(i) > 5 and ':' not in i:
                i = i.split('/')
                i = i[len(i) - 1]

                i = i.strip()
                i = i.replace(" ", "")
                word = i

                if word != " " and len(word) > 0:

                    print(len(word))
                    print(word)

                    words = jieba.cut(word, cut_all=False)
                    for n in words:
                        print(n)
                        x.append(n)
        item['categories'] = x
        yield item


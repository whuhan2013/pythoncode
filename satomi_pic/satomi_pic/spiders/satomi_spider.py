from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from satomi_pic.items import SatomiPicItem

class SatomiSpider(CrawlSpider):
    name="satomi_pic_spider"

    download_delay=1

    allowed_domains=[]

    start_urls=[
        'http://movie.douban.com/celebrity/1016930/photo/1253599819/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'/\d+/\#photo')), callback='parse_item',
             follow=True),

    )

    def parse_item(self,response):
        print("hello1")
        print(response)

        sel=Selector(response)

        item=SatomiPicItem()

        item['image_urls']=sel.xpath('//div[@class="photo-show"]/div[@class="photo-wp"]/a[@class="mainphoto"]/img/@src').extract()
        print("hello2",item['image_urls'])
        yield item
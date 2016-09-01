# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import sys

class DoubanMovieCategoryPipeline(object):
    def __init__(self):
        self.mongo_url = 'localhost'
        self.mongo_port = 27017
        self.collection_name = 'categories'
        self.db_name = 'douban_category'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url, self.mongo_port)
        self.db = self.client[self.db_name]
        self.con = self.db[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        for i in item['categories']:
            if self.con.find_one({"category": i}):
                add_one = self.con.find_one({'category': str(i)})
                print(add_one)
                count = int(add_one['count'])
                count = count + 1
                add_one['count'] = count
                print(add_one)
                print("here1")
                print(count)
                self.con.save(add_one)
            else:
                self.con.insert_one({'category': i, "count": 1})
                print("here2")
                print("hello")
        print("here3")
        print(item['categories'])
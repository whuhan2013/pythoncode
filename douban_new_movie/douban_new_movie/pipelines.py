# -*- coding: utf-8 -*-


import json
import codecs
import sys
import importlib

importlib.reload(sys)




class DoubanNewMoviePipeline(object):
    def __init__(self):
        self.file=codecs.open('douban_new_movie.json',mode='w',encoding='utf-8')

    def process_item(self, item, spider):
        line='the new movie list:'+'\n'

        for i in range(len(item['movie_star'])):
            movie_name={'movie_name':str(item['movie_name'][i]).replace(' ','')}
            #print(movie_name)
            movie_star={'movie_star':item['movie_star'][i]}
            movie_url={'movie_url':item['movie_url'][i]}
            line=line+json.dumps(movie_name,ensure_ascii=False)
            line=line+json.dumps(movie_star,ensure_ascii=False)
            line=line+json.dumps(movie_url,ensure_ascii=False)+'\n'

        self.file.write(line)

    def close_spider(self,spider):
        self.file.close()
import gevent.monkey
gevent.monkey.patch_all()
import sys
import gevent
import redis
import crawler
import time
from multiprocessing.dummy import Pool
import multiprocessing
from red_filter import red, red_queue

#red_queue="test_the_url_queue"
#red_crawled_set="test_url_has_crawled"

process_pool=Pool(multiprocessing.cpu_count()*2)



#connect to redis server





#wrap the class method
def create_new_slave(url,option):
    new_slave=crawler.Zhihu_Crawler(url,option)
    new_slave.send_request()
    return "ok"

def gevent_worker(option):
    while True:
        url=red.lpop(red_queue)
        if not url:
            break
        create_new_slave(url,option)

def process_worker(option):
    jobs=[]
    for i in range(2):
        jobs.append(gevent.spawn(gevent_worker,option))
    gevent.joinall()



if __name__=="__main__":

    '''
    start the crawler

    '''

    start=time.time()
    count=0

    #choose the running way of using database or not

    try:
        option=sys.argv[1]
    except:
        option=''
    if "mongo" not in option:
        option="print_data_out"

    #the start page

    red.lpush(red_queue,"https://www.zhihu.com/people/mo-ming-42-91")
    url=red.lpop(red_queue)
    create_new_slave(url,option=option)
    for i in range(2):
        gevent_worker(option=option)

    process_pool.map_async(process_worker,option)
    process_pool.close()
    process_pool.join()


    print("crawler has crawled %d people ,it cost %s" % (count,time.time()-start))
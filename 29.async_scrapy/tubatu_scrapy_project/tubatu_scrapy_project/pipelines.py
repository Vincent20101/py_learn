# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


#实现将数据保存到mongodb当中去
class TubatuScrapyProjectPipeline(object):
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://192.168.110.129:27017")
        mydb = myclient['db_tubatu']
        self.mycollection = mydb['collection_tubatu']

    def process_item(self, item, spider):
        data = dict(item)
        self.mycollection.insert_one(data)
        return item

#自定义的图片下载类需要继承于ImagesPipeline
class TubatuImagePipeline(ImagesPipeline):
    # def get_media_requests(self, item, info):
    #     #根据image_urls中指定的URL进行爬取
    #     pass

    def item_completed(self, results, item, info):
        #图片下载完毕之后，处理结果的,返回是一个二元组
        #(success,image_info_or_failure)
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        return item

    def file_path(self, request, response=None, info=None):
        #用于给下载的图片设置文件名称的
        url = request.url
        file_name = url.split('/')[-1]
        #aaaa.jpg
        return file_name

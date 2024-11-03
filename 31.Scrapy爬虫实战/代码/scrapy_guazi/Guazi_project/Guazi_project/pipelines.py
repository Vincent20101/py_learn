# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pytesseract
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os
from PIL import Image
import pymongo


class GuaziProjectPipeline:
    def process_item(self, item, spider):
        return item


class HandleImagePipeline(ImagesPipeline):
    """
    用于处理上牌时间图片解析成数据
    """

    def item_completed(self, results, item, info):
        # 返回图片的路径
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Item contains no images')
        # 解析图片到数据
        item["register_time"] = self.get_register_time(image_paths[0])
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        # 设置图片文件名称
        url = request.url
        # https://image1.guazistatic.com/qn2004161741106362a3b27a43d2054ca8bd8bb7c42212.jpg
        # qn2004161741106362a3b27a43d2054ca8bd8bb7c42212.jpg
        file_name = url.split("/")[-1]
        return file_name

    def get_register_time(self, image_path):
        """
        # 找到图片
        :param image_path: 图片的名称
        :return:
        """
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # 定位图片
        url_path = os.path.join(file_path, "images", image_path)
        # 图片识别
        register_time = pytesseract.image_to_string(Image.open(url_path)).strip()
        return register_time


class MongoPipeline:
    # 保存的集合的名称
    collection_name = 'guazi_car_info'

    def __init__(self, mongo_uri, mongo_db, mongo_port):
        """
        mongodb初始化
        :param mongo_uri: mongodb的地址127.0.0.1
        :param mongo_db: guazi
        """
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_port = mongo_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'),
            # 取端口
            mongo_port=crawler.settings.get("MONGODB_PORT")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        存储数据使用的方法
        :param item:
        :param spider:
        :return:
        """
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item

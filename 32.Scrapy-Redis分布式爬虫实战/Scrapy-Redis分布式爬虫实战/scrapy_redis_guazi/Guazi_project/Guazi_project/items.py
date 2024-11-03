# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 车源号
    car_id = scrapy.Field()
    # 车名字
    car_name = scrapy.Field()
    car_detail_url = scrapy.Field()
    # 上牌时间
    register_time = scrapy.Field()
    # 表显历程
    display_mileage = scrapy.Field()
    # 变速箱
    transmission = scrapy.Field()
    # 解析图片的URL地址
    image_urls = scrapy.Field()

import scrapy
from Guazi_project.items import GuaziProjectItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    start_urls = ['http://guazi.com/']

    def start_requests(self):
        # 所有品牌数据
        with open("brand.txt", "r", encoding="utf-8") as f:
            brands = f.readlines()
        # 遍历到所有品牌
        for brand in brands:
            # 构造品牌的URL数据
            url = "https://www.guazi.com{}i7c-1/".format(brand)
            # 发送请求，请求品牌下的列表页
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        解析列表页，发送下一页请求
        :param response:
        :return:
        """
        # 返回的是当前列表页里面所有二手车数据，获取的是二手车的详情页的URL
        item_urls = response.xpath("//ul[@class='carlist clearfix js-top']/li/a/@href").extract()
        for url in item_urls:
            # 详情页的URL
            item_url = "https://www.guazi.com{}".format(url)
            # 发送详情页URL的请求，编辑回调方法，解析详情页
            yield scrapy.Request(url=item_url, callback=self.detail_parse)

        # 是否有下一页的标签
        next_url_element = response.xpath("//a[@class='next']/@href")
        if next_url_element:
            # 构造下一页URL，并发送下一页请求
            next_url = "https://www.guazi.com{}".format(next_url_element.extract_first())
            yield scrapy.Request(url=next_url, callback=self.parse)

    def detail_parse(self, response):
        """
        解析详情页
        :param response:
        :return:
        """
        car_item_info = GuaziProjectItem()
        # 车源号
        car_item_info["car_id"] = self.handle_item(response.xpath("//div[@class='right-carnumber']/text()").extract_first())
        # 车名字
        car_item_info["car_name"] = self.handle_item(response.xpath("//h1[@class='titlebox']/text()").extract_first())
        car_item_info["car_detail_url"] = response.url
        # 上牌时间
        # register_time = scrapy.Field()
        # 拿到上牌时间的图片的URL,返回一个列表
        car_item_info["image_urls"] = response.xpath("//li[@class='one']/span/img/@src").extract()
        # 表显里程
        car_item_info["display_mileage"] = self.handle_item(response.xpath("//li[@class='two']/span/text()").extract_first())
        try:
            # 变速箱
            car_item_info["transmission"] = self.handle_item(response.xpath("//li[@class='last']/span/text()").extract_first())
        except:
            pass
        # yield到pipelines里面去
        yield car_item_info

    def handle_item(self, item):
        """
        处理数据两侧的特殊字符，/r/n
        :param item:
        :return:
        """
        return item.strip()



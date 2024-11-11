import scrapy
import json
from scrapy_guazi_xhr.items import ScrapyGuaziXhrItem
from urllib.parse import urlparse, parse_qsl, urlunparse, unquote, urlencode


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    # start_urls = ['http://guazi.com/']

    def start_requests(self):
        """发送列表页的请求"""
        with open("brands.txt", "r", encoding="utf-8") as f:
            brands_data = f.read()
        # 获取品牌列表
        brands_list = json.loads(brands_data).get("data").get("common")
        for brand in brands_list:
            # 第一页列表页的URL
            url = "https://mapi.guazi.com/car-source/carList/pcList?minor={}&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=7&key_word=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page=1&pageSize=20&city_filter=13&city=13&guazi_city=13&versionId=0.0.0.0&osv=Unknown&platfromSource=wap".format(brand.get("value"))
            yield scrapy.Request(url=url, callback=self.parse)
            # 仅发送第一页请求，限定在一个品牌中的,方便我们讲课
            break

    def parse(self, response):
        """第一页列表页请求的返回"""
        data = response.json().get("data")
        # 列表页里面的每一条二手车数据
        guazi_items = data.get("postList")
        for item in guazi_items:
            detail_url = "https://www.guazi.com/Detail?clueId={}".format(item.get("clue_id"))
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, dont_filter=True)

        # 当前页码
        now_page = int(data.get("page"))
        # 总页码
        total_page = int(data.get("totalPage"))
        # 判断是否超过1页
        if total_page >1 and now_page == 1:
            # 从第二页开始发送请求，发送到total_page
            for page in range(2, total_page + 1):
                # 现获取第一页的URL
                url = response.url
                # 构造下一页的URL
                params = {"page": str(page)}
                # 解析URL，解析第一页的URL
                # urlparse返回6个部分，协议，位置，路径，参数，查询，片段
                url_parts = list(urlparse(url))
                # 通过parse_qsl转换成列表,keep_blank_values处理参数中字段为空的,true是保留空字段的
                query = dict(parse_qsl(url_parts[4], keep_blank_values=True))
                # 更新页码
                query.update(params)
                # encode update页码之后的url,放入到解析好的url第四个索引里
                url_parts[4] = urlencode(query)
                # 解码
                page_url = unquote(urlunparse(url_parts))
                yield scrapy.Request(url=page_url, callback=self.parse)

    def parse_detail(self, response):
        """解析详情页"""
        guazi_info = ScrapyGuaziXhrItem()
        guazi_info["title"] = response.xpath("//h1[@class='titlebox']/text()").extract_first().strip()
        guazi_info["price"] = response.xpath("//span[@class='price-num gzfont']/text()").extract_first()
        yield guazi_info

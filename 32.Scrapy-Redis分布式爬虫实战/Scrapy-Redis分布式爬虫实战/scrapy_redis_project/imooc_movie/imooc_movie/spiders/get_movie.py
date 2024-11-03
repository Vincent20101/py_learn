import scrapy
from imooc_movie.items import ImoocMovieItem
from scrapy_redis.spiders import RedisSpider


class GetMovieSpider(RedisSpider):
    name = 'get_movie'
    # allowed_domains = ['54php.cn']
    # start_urls = ['http://movie.54php.cn/movie/?&p=1']
    redis_key = "get_movie:start_urls"

    def parse(self, response):
        # 获取每一页电影的items
        movie_items = response.xpath("//div[@class='row']/div")
        for item in movie_items:
            # 获取详情页的URL
            detail_url = item.xpath(".//a[@class='thumbnail']/@href").extract_first()
            # 需要查看能否获取到detail_url
            if detail_url:
                yield scrapy.Request(url=detail_url, callback=self.parse_detail, dont_filter=True)
        next_page = response.xpath("//a[@aria-label='Next']/@href").extract_first()
        if next_page:
            next_page_url = "http://movie.54php.cn{}".format(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        """
        解析详情页
        :param response:
        :return:
        """
        movie_info = ImoocMovieItem()
        movie_info["title"] = response.xpath("//div[@class='page-header']/h1/text()").extract_first()
        movie_info["desc"] = response.xpath("//div[@class='panel-body']/p[4]/text()").extract_first()
        movie_info["download_url"] = response.xpath("//div[@class='panel-body']/p[5]/text()").extract_first()
        # yield到pipelines
        yield movie_info

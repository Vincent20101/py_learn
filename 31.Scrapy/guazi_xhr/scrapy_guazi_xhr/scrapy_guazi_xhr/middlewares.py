# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyGuaziXhrSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyGuaziXhrDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HandleDetail(object):
    """用户破解详情页的中间件"""

    # 直接携带cookie访问目标信息,而不是通过返回的js代码计算cookie
    def process_request(self, request, spider):
        # 如果说请求的URL里面有www.guazi.com/Detail并且request.cookie没有值的
        if "www.guazi.com/Detail" in request.url and not request.cookies:
            cookie_value = {"uuid": "badf427f-0079-443c-baad-37ec3cfe9553"}
            request.cookies = cookie_value
            # 重新发送请求，入队列
            return request

    def process_response(self, request, response, spider):
        """处理带有cookie请求的返回数据"""
        replace_value = {
            "0": "&#59854;",
            "1": "&#58397;",
            "2": "&#58928;",
            "3": "&#60146;",
            "4": "&#58149;",
            "5": "&#59537;",
            "6": "&#60492;",
            "7": "&#57808;",
            "8": "&#59246;",
            "9": "&#58670;"
        }
        # 获取返回数据
        text = response.text
        for i, v in replace_value.items():
            if v in text:
                text = text.replace(v, i)
        # 把返回数据中的body替换成修改后的text
        response = response.replace(body=text)
        # 最终的返回数据
        return response
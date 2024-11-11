# -*- coding: utf-8 -*-
import scrapy
import re
import json
from tubatu_scrapy_project.items import TubatuScrapyProjectItem


class TubatuSpider(scrapy.Spider):
    #名称不能冲突，也就是说不能重复,name不能冲突
    name = 'tubatu'
    #允许爬虫去抓取的域名
    allowed_domains = ['xiaoguotu.to8to.com']
    #项目启动之后要启动的爬虫文件
    start_urls = ['https://xiaoguotu.to8to.com/tuce/p_1.html']

    #默认的解析方法
    def parse(self, response):
        print(response.request.headers)
        #这里使用了正则表达式来获取项目的id,需要使用转义字符来转义这个.
        content_id_search = re.compile(r"(\d+)\.html")
        #response后面可以直接使用xpath方法
        #response就是一个Html对象
        pic_item_list = response.xpath("//div[@class='item']")
        for item in pic_item_list:
            info = {}
            #这里有一个点不要丢了,是说明在当前的Item下面再次使用xpath
            #我们可以通过extract_first这个方法来获取项目的名称,项目的数据
            #获取的项目的名称
            info['content_name'] = item.xpath(".//div/a/text()").extract_first()
            #项目的URL
            content_url = 'https:'+item.xpath(".//div/a/@href").extract_first()
            info['content_id'] = content_id_search.search(content_url).group(1)
            info['content_ajax_url'] = 'https://xiaoguotu.to8to.com/case/list?a2=0&a12=&a11='+str(info['content_id'])+'&a1=0&a17=1'
            #我们使用yield来发送这个异步请求
            #使用的是scrapy.Request发送请求的
            #回调函数,只写方法的名称，不要调用方法
            yield scrapy.Request(url=info['content_ajax_url'],callback=self.handle_pic_parse,meta=info)

        #页码逻辑
        if response.xpath("//a[@id='nextpageid']"):
            now_page = int(response.xpath("//div[@class='pages']/strong/text()").extract_first())
            next_page_url = 'https://xiaoguotu.to8to.com/tuce/p_%d.html'%(now_page+1)
            yield scrapy.Request(url=next_page_url,callback=self.parse)

    def handle_pic_parse(self,response):
        pic_dict_data = json.loads(response.text)['dataImg']
        for pic_item in pic_dict_data:
            for item in pic_item['album']:
               tubatu_info =  TubatuScrapyProjectItem()
               #昵称
               tubatu_info['nick_name'] = item['l']['n']
               #图片的地址
               # tubatu_info['pic_url'] = 'https://pic1.to8to.com/case/'+item['l']['s']
               #必须要使用这个字段，后面的数据要改成列表格式
               tubatu_info['image_urls'] = ['https://pic1.to8to.com/case/'+item['l']['s']]
               #图片的名称
               tubatu_info['pic_name'] = item['l']['t']
               tubatu_info['content_name'] = response.request.meta['content_name']
               tubatu_info['content_id'] = response.request.meta['content_id']
               tubatu_info['content_url'] = response.request.meta['content_ajax_url']
               #yield到pipelines，我们通过setting里面启用，如果不启用，是无法使用的
               yield tubatu_info

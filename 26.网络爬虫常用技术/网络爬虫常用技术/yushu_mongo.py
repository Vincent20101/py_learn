import requests
from lxml import etree
import pymongo

# 创建数据库的连接
# 使用的是虚拟机，需要设置端口转发
myclient = pymongo.MongoClient("mongodb://127.0.0.1:1112")
# 使用的物理机，独立的服务器，云服务器，阿里云，腾讯云
# mongodb://数据库的IP:27017
# 指定数据库和集合
mydb = myclient["db_yushu"]
mycollection = mydb["book_python"]
# 插入数据

# 请求图书的页码链接
# 获取每一页图书数据，并抽取出图书数据
# 格式化每一条图书数据

def handle_list(item_list):
    return "".join(item_list)


def handle_detail_xpath(content):
    """
    解析图书数据，格式化每一条图书数据
    :param content: 传入的response.text
    :return:
    """
    # 进行数据的实例化
    html = etree.HTML(content)
    # 获取所有的图书条目
    all_book_items = html.xpath("//div[@class='col-md-7 flex-vertical description-font']")
    for item in all_book_items:
        # 获取到作者，出版社，价格信息
        author_press_price = handle_list(item.xpath("./span[2]/text()")).split("/")
        if len(author_press_price) == 3:
            # 把原来的print修改为mycollection.insert_one
            mycollection.insert_one(
                {
                    # 从当前节点下使用xpath进行解析,如果不这么写//,.这个点需要大家注意
                    "title": handle_list(item.xpath("./span[@class='title']/text()")),
                    "author": author_press_price[0],
                    "press": author_press_price[1],
                    "price": author_press_price[2],
                    "summary": handle_list(item.xpath("./span[@class='summary']/text()"))
                }
            )


def main():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }
    for i in range(1, 5):
        url = "http://yushu.talelin.com/book/search?q=python&page={}".format(i)
        response = requests.get(url=url, headers=header)
        handle_detail_xpath(response.text)


if __name__ == '__main__':
    main()

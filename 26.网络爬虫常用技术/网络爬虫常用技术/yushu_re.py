import requests
import re


# 请求图书列表页的链接
# 获取每一条图书信息
# 格式化每一条图书信息

def handle_detail_re(content):
    """
    处理列表页返回数据
    :param content: response.text
    :return: print
    """
    # 图书条目正则表达式,re.S可以进行全文匹配
    item_search = re.compile('description-font">.*?</div>', re.S)
    # 获取每一页图书条目数据
    all_item = item_search.findall(content)
    # 图书的名称
    title_search = re.compile('title">(.*?)</span>')
    # 获取图书的作者，出版社，价格
    author_press_price_search = re.compile(r'<span>(.*?)</span>')
    # 图书的描述
    desc_search = re.compile(r'summary">(.*?)</span>')
    for item in all_item:
        # 获取到了作者，出版社，价格 的列表信息
        author_press_price = author_press_price_search.search(item).group(1).split('/')
        if len(author_press_price) == 3:
            print(
                {
                    "title": title_search.search(item).group(1),
                    "author": author_press_price[0],
                    "press": author_press_price[1],
                    "price": author_press_price[2],
                    "desc": desc_search.search(item).group(1)
                }
            )


def main():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }
    for i in range(1, 5):
        url = "http://yushu.talelin.com/book/search?q=python&page={}".format(i)
        response = requests.get(url=url, headers=header)
        handle_detail_re(response.text)

if __name__ == '__main__':
    main()
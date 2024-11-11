import requests
from bs4 import BeautifulSoup


def handle_detail_bs4(content):
    """
    解析目标页面返回数据的
    :param content:response.text
    :return:
    """
    # 数据的实例化,传入要解析的数据，和解析器，解析器使用的是lxml
    soup = BeautifulSoup(content, "lxml")
    # 获取所有的图书条目,使用find_all,查找div标签，通过class属性查找，class是一个关键字,class_
    all_book_items = soup.find_all("div", class_="row col-padding")
    # 打印未格式化的数据,可以看到html标签的
    for item in all_book_items:
        # print(item)
        # 获取图书信息,先查找上层的div,发现里面包含着三个span，find_all来查找所有span
        info = item.find("div", class_="col-md-7 flex-vertical description-font").find_all("span")
        # 获取作者，出版社，价格信息
        author_press_price = info[1].string.split("/")
        if len(author_press_price) == 3:
            print(
                {
                    # 最终信息
                    "title": info[0].string,
                    "author": author_press_price[0],
                    "press": author_press_price[1],
                    "price": author_press_price[2],
                    "summary": info[2].string
                }
            )


def main():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }
    for i in range(1, 5):
        url = "http://yushu.talelin.com/book/search?q=python&page={}".format(i)
        response = requests.get(url=url, headers=header)
        handle_detail_bs4(response.text)


if __name__ == '__main__':
    main()

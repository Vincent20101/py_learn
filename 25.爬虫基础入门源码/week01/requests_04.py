import requests


# 构造4页连接
# 发送请求，请求4页连接数据
# 获取response数据response.text
# with open文件，把response.text写入html文件

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

proxy = {
    # http://用户名:密码@代理的接口信息
    "http": "http://dazhuang:abcd1234@dynamic.xingsudaili.com:10010",
    "https": "http://dazhuang:abcd1234@dynamic.xingsudaili.com:10010"
}

for i in range(1, 5):
    # 构造4页链接
    url = "http://yushu.talelin.com/book/search?q=python&page={}".format(i)
    # 发送请求, 还要携带自定义的请求头和购买的代理
    response = requests.get(url=url, headers=header, proxies=proxy)
    # 获取response数据
    # print(response.text)
    # 将response数据写入html文件
    html_file_name = "page_{}.html".format(i)
    # 写入本地html文件
    with open(html_file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("{}文件已下载好".format(html_file_name))
# dynamic.xingsudaili.com:10010
import requests

# 用来查看我们源IP地址的
url = "http://pv.sohu.com/cityjson"
# response = requests.get(url=url)
# 47.240.60.15
# print(response.text)

proxy = {
    # http://用户名:密码@代理的接口信息
    "http": "http://dazhuang:abcd1234@dynamic.xingsudaili.com:10010",
    "https": "http://dazhuang:abcd1234@dynamic.xingsudaili.com:10010"
}

while True:
    response = requests.get(url=url, proxies=proxy)
    print(response.text)

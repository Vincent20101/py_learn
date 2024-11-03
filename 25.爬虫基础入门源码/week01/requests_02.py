import requests

# verify默认是开启的
# 是一个自签名的证书的网站
# 当前浏览器是没有这个网站的证书的
response = requests.get(url="https://218.28.111.252/login.html", verify=False)
print(response.text)
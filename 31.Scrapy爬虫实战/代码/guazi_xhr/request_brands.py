import requests

# 浏览器抓包，切换xhr
url = "https://mapi.guazi.com/car-source/carList/suggestion?city=12&field=1&versionId=0.0.0.0&osv=Unknown&platfromSource=wap"
# 需要不断的实验，不断的测试,client-time,verify-token
headers = {
    "client-time": "1627304832",
    "verify-token": "dca47b7d443ac7f442f2702b05ac88a9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

response = requests.get(url=url, headers=headers)
# 把品牌数据保存到本地
with open("brands.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
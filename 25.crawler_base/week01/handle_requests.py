#在发送请求的时候，是必须要导入requests包
import requests

# 通过get方法来请求数据,requests.get
# url
# response = requests.get(url='http://www.qq.com')
# 查看返回text
# print(response.text)

#导入requests包
# import requests

#构造发送的数据,字典的格式
# data = {"name":"imooc"}
#发送的是post请求,data关键字，data参数
# response = requests.post('http://httpbin.org/post',data=data)
#查看返回数据
# print(response.text)

#这个网页，返回的get请求的数据和post请求的数据是不一样的。

# import requests
#
#构造的URL的数据，一定要和Post请求做好区分
# data = {'key1':'value1','key2':'value2'}
#使用的是GET请求的方法,params关键字一定要做好区分
# response = requests.get('http://httpbin.org/get',params=data)
#查看了是哪个URL给我们返回的数据
# # print(response.url)
#查看返回头,注意，是headers不是header
# # print(response.headers)
#查看返回体
# print(response.text)

#请求图片
# import requests
#get方法
# response = requests.get("https://www.imooc.com/static/img/index/logo.png")
#一定要使用wb模式
# with open('imooc.png','wb') as f:
#返回的不再是文本数据了，而是二进制的数据,content
#     f.write(response.content)

# #请求的json数据
# import requests
# #定义了一个变量,设置了一个浏览器的请求头,user-agent
# header = {
#     'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
# }
# #发送自定义的请求头部的时候，关键字是headers
# response = requests.get('http://httpbin.org/ip',headers=header)
# #查看状态码
# # print(response.status_code)
# # #返回的是json数据,response.json
# # data = response.json()
# # print(data)
# # print(data['origin'])
# print(response.headers)
# print(response.request.headers)

# import requests
#
# #设置了关键字timeout超时时间,0.001,如果0.001秒之内，没有给我返回数据，则会抛出一个timeout报错
# #项目里一般设置为2-3秒合适
# response = requests.get('http://www.github.com',timeout=2)
# print(response.status_code)
# print(response.text)

# import requests
# url = 'https://www.baidu.com'
# #定制请求头,使用了一个标准的浏览器的UA
# header = {
#     'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'
# }
#
# response = requests.get(url=url,headers=header)
# print(response.headers)
# #cookie是一个对象RequestsCookieJar，行为和字典类似
# print(response.cookies)
# print(response.cookies['BIDUPSID'])

# import requests
# #可以查看当前发送cookie的url,可以进行测试
# url = 'http://httpbin.org/cookies'
# #使用了字典来构造cookie
# cookies = dict(cookies_are='hello imooc')
# #get请求方法,cookies，变量也叫cookies，不要搞混
# response = requests.get(url=url,cookies=cookies)
# print(response.text)





import requests


#在requests模块中有session方法

# 为什么没有携带请求头
# 不需要提供定制化的请求头，直接使用python默认的请求头就可以

# 需要提供请求的数据
login_data = {
    "email": "dazhuang_python@sina.com",
    "password": "abcd1234"
}

# 实例化session方法，用于自动化的记录session信息
session = requests.session()

# 发送了一个POST请求，并且提供了login_data数据
# login_response = requests.post(url="http://yushu.talelin.com/login", data=login_data)
# 1.需要把原来的requests替换为实例化好的session
login_response = session.post(url="http://yushu.talelin.com/login", data=login_data)
# print(login_response.text)
# 登录之后，请求个人信息页的时候是失败的
# 可以在请求头中提供cookies就可以访问个人信息页面了
# personal_response = requests.get(url="http://yushu.talelin.com/personal")
# 自动化的带上session,个人的登录凭据信息
personal_response = session.get(url="http://yushu.talelin.com/personal")
print(personal_response.text)
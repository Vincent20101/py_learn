#安装的是beautifulsoup4，但是导包的时候，是通过bs4来导入的，并且导入的是大写的BeautifulSoup
from bs4 import BeautifulSoup



html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#lxml提前安装好，pip install lxml,第一个参数是html代码段，第二个参数是解析器
soup = BeautifulSoup(html,'lxml')
#查看经过bs4实例化，初始化的代码段
# print(soup.prettify())
#获取到的是数据结构，tag，tag有很多方法，如string
# print(type(soup.title))
#来查看文档中title的属性值
# print(soup.title.string)
# print(soup.head)
#当有多个节点的时候，我们当前的这种选择模式，只能匹配到第一个节点，其他节点会被忽略
# print(soup.p)
#获取节点的名称
# print(soup.title.name)
#attrs会返回标签的所有属性值,返回的是一个字典
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
#返回的节点属性，可能是列表，也可能是字符串，需要进行实际的判断
# print(soup.p['name'])
# print(soup.p['class'])
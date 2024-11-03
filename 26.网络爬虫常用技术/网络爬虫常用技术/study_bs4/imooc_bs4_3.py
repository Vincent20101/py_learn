#子节点和子孙节点
from bs4 import BeautifulSoup


html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
#获取p标签的子节点，注意是子节点,返回的是一个列表
#列表中的元素是p节点的直接子节点
#返回结果没有单独的吧a标签中的span标签选出来
#contents方法获取直接子节点的列表
# print(soup.p.contents)
#contents和children返回的结果是一样的，都是直接子节点
#只不过children方法需要使用for循环来进行遍历
# print(soup.p.children)
for i,j in enumerate(soup.p.children):
    print(i,j)
print("==============================")
#获取子节点和孙节点
#会把中间的孙节点也单独的取出来
# print(soup.p.descendants)
for i,j in enumerate(soup.p.descendants):
    print(i,j)

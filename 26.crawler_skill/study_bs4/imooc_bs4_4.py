#获取父节点和获取祖先节点

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
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
#获取a节点的父节点
# print(soup.a.parent)
#获取所有的祖先节点
print(soup.a.parents)
for i,j in enumerate(soup.a.parents):
    print(i,j)
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

soup = BeautifulSoup(html,'lxml')
#获取a标签的下一个兄弟节点
# print(soup.a.next_sibling)
#获取上一个兄弟节点
# print(soup.a.previous_sibling)

print(soup.a.next_siblings)
#获取当前节点后面的所有兄弟节点
# for i,j in enumerate(soup.a.next_siblings):
#     print(i,j)
#获取当前节点前面所有的兄弟节点
for i,j in enumerate(soup.a.previous_siblings):
    print(i,j)
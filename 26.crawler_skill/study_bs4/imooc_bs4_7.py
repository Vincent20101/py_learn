#通过属性来进行查询
#通过text文本来获取匹配的文本

import re
from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list" id="list-1">
            <li class="element">Foo2</li>
            <li class="element">Bar2</li>
            <li class="element">Jay2</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
#attrs，传入的是属性参数,类型是字典,attrs={"id":"list-1"}
# print(soup.find_all(attrs={"id":"list-1"}))
# print(soup.find_all(attrs={"name":"elements"}))
#也可以直接传入ID这个参数
# print(soup.find_all(id="list-1"))
#class在Python中是一个关键字，find_all方法里面要用class的时候，后面加上一个下划线
# print(soup.find_all(class_="list"))

#可以通过text参数来获取文本的值，可以传递正则表达式，返回是一个列表
# print(soup.find_all(text=re.compile("Foo\d")))

#find方法,返回的是一个单个的元素,第一个匹配的元素,而find_all返回的是所有值的列表
# print(soup.find(name="ul"))


"""
find_parents 和 find_parent：前者返回所有祖先节点，后者返回直接父节点。
find_next_siblings 和 find_next_sibling：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
find_previous_siblings 和 find_previous_sibling：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
find_all_next 和 find_next：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
find_all_previous 和 find_previous：前者返回节点前所有符合条件的节点，后者返回第一个符合条件的节点。
"""
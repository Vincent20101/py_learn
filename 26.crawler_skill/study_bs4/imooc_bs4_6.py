#方法选择器,find_all,通过节点名来进行查询的

from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
#find_all，name=ul,可以获取到当前文本中所有ul标签的数据,返回的是一个列表
# print(soup.find_all(name='ul'))
#tag类型
# print(type(soup.find_all(name='ul')[0]))
#可以进行嵌套查询
for ul in soup.find_all(name="ul"):
    for li in ul.find_all(name='li'):
        #tag
        print(li.string)
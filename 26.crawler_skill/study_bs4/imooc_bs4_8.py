#使用css选择器，只需要呢，调用select方法，传入css选择器即可

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
#需要调用select方法，传入css选择器
# print(soup.select(".panel .panel-heading"))

#获取ul标签下所有Li标签
# print(soup.select("ul li"))

#获取id为list-2，class为element两个Li标签
# print(type(soup.select("#list-2 .element")[0]))

#支持嵌套选择
#先获取到ul标签，tag类型,for 调用select方法在次传入css选择器
for ul in soup.select("ul"):
    for li in ul.select("li"):
        #调用tag类型里面的方法，string方法来获取文本内容
        # print(li.string)
        print(li['class'])

#支持使用属性获取元素
# for ul in soup.select("ul"):
#     print(ul['id'])


#建议大家使用find find_all查询匹配单个结果或多个结果
#css选择器非常的熟悉，那么就可以使用css选择器
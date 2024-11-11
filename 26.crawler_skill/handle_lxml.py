#导入lxml库,etree
from lxml import etree


#准备的html数据,不完整，html,body,li不完整
html_data = '''
<div>
  <ul>
       <li class="item-0"><a href="link1.html">first item</a></li>
       <li class="item-1"><a href="link2.html">second item</a></li>
       <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
       <li class="item-1"><a href="link4.html">fourth item</a></li>
       <li class="item-0"><a href="link5.html">fifth item</a>
   </ul>
</div>
'''
#使用etree.HTML
html = etree.HTML(html_data)
#etree.tostring,decode()
# <html><body><div>
#   <ul>
#        <li class="item-0"><a href="link1.html">first item</a></li>
#        <li class="item-1"><a href="link2.html">second item</a></li>
#        <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
#        <li class="item-1"><a href="link4.html">fourth item</a></li>
#        <li class="item-0"><a href="link5.html">fifth item</a>
#    </li></ul>
# </div>
# </body></html>
# print(etree.tostring(html).decode())
#返回_Element，就是整个xml树的根节点
# print(type(html))
#使用的是双斜杠,返回是一个列表，每一个元素都是element类型,列表里面的每一个element类型的元素就
#代表我们获取到的标签元素
# result = html.xpath("//li/a/text()")
#获取li标签下面所有的class属性值
# result = html.xpath("//li/@class")
#获取的li标签href值为link1.html这个a标签,使用了单引号，如果外面使用的是
#双引号，内部一定要使用单引号,大家一定要注意
# result = html.xpath("//li/a[@href='link1.html']/text()")
#我们需要获取span标签，一定要注意span他是a标签的子元素,而不是li标签的子元素,使用双斜杠
# result = html.xpath("//li//span")
#我们使用了last()函数，最后一个标签，-1代表倒数第二个标签
result = html.xpath("//li[last()]/a/@href")
print(result)
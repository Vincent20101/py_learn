#导入RE正则表达式模块
import re

#这个正则表达式，用来匹配数字
# pattern = re.compile(r"\d+")
################################################
# #match头部匹配,如果头部匹配失败了则返回None
# m1 = pattern.match('one12twothree34four')
# #没有匹配到数据
# print(m1)
# #进行了指定起始位置和终止位置
# m2 = pattern.match('one12twothree34four',3,10)
# #查看数据可以使用group
# print(m2.group())
####################################################
#search方法,如果匹配失败，则返回None
#search方法是在字符串任意位置开始匹配，但是match是从头部开始匹配
# m1 = pattern.search('one12twothree34four')
# #查看数据的时候，使用group
# print(m1.group())
#############################################
#findall方法,搜索全文 ，得到一个列表返回,如果没有匹配，则返回一个空列表
# result = pattern.findall('one12twothree34four')
# #findall方法返回的是一个列表
# print(result)
####################################
#我们在学习字符串的split，可以通过一些分隔符进行分割，返回也是一个列表
# string = 'a,b,c'
# print(string.split(','))

# #通过空格，都好，以及分号对我们这个字符串进行了分割，返回了一个列表
# pattern = re.compile(r"[\s\,\;]+")
# string = 'a,b;; c  d'
# #split方法,返回一个列表
# print(pattern.split(string))
#############################################
string = '<h1 class="test">imooc</h1>'
#我们匹配数字
# pattern = re.compile('\d')
# #这里调用了re模块的sub,把h1标签里面的1换成了2
# print(pattern.sub('2',string))
# #这个count用来指定替换次数的,如果不指定，则为全文替换
# print(pattern.sub('2',string,1))
#分组乱入，使用了search方法来获取分组里面的数据，通过group()里面的数字，来
#确定分组,这个正则表达式，也在函数中用到了
#.\d被后面的\1所引用,使用了命名分组方法，制定了一个名字，classname


# pattern = re.compile('<(.\d)\sclass="(?P<classname>.*?)">.*?</(\\1)>')
pattern = re.compile(r'<(.\d)\sclass="(?P<classname>.*?)">.*?</(\1)>')
print(pattern.search(string).group(1))



#


# #定义一个函数,match对象
# def func(m):
#     #取了第二个分组
#     return 'after sub ' + m.group('classname')
# #调用sub方法
# print(pattern.sub(func,string))
# string = '<h1 class="test">imooc</h1>'
# #使用了贪婪模式，匹配到了所有的字符串
# pattern1 = re.compile(r'<.\d\sclass=.*>')
# print(pattern1.search(string).group())
# #关闭了贪婪模式，使用?
# pattern2 = re.compile(r'<.\d\sclass=.*?>')
# print(pattern2.search(string).group())













# with open('test.txt', 'a+') as f:
#     f.seek(0)
#     content = f.readlines()
#     f.seek(2)
#     for line in content:
#         f.write(line)

f = open('test.txt', 'r')
lines = f.readlines()
f1 = open('test1.txt', 'w')
f1.seek(0)
for line in lines:
    line = line[::-1]
    f1.write(line)

f1.close()
f.close()


f = open('test.txt', 'a')
f.write('Hello Everyone\n')
f.close()
# 使用a的打开方式打开文件，文件游标默认是在文件的尾部，因此，可以便捷的往文件尾部添加内容，除此以外，文件对象还提供seek()方法，
# 可以移动文件的游标位置，它接受一个参数，表示文件的位置，0：文件首部，1：当前位置，2：文件尾部，
# 通过seek()可以把文件游标移动到文件首部但不删除文件的内容。

f = open('test.txt', 'a+')
content = f.readlines()
print(content) # ==> []
f.seek(0)
content = f.readlines()
print(content) # ==> ['Hello World\n', 'Hello Python\n', 'Hello Imooc\n']
# 第一次print(content)的时候，由于文件游标在文件的尾部，所以readlines()读取不到任何数据，打印了空的结果，
# 第二次print(content)的时候，由于通过seek(0)，文件游标移动到了文件的首部，因此readlines()就返回了文件所有的内容。
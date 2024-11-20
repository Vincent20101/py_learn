from collections import namedtuple

# namedtuple 的应用: 将 user 表的数据全部取出然后加一个列
User = namedtuple('User', ['name', 'age', 'height', 'edu'])

user_tuple = ('bobby', 29, 175)
user_dict = {
    'name': 'bobby',
    'age': 29,
    'height': 175,
}

# 向 namedtuple 传参可以使用 tuple 和 dict 两种方式
#  user = User(*user_tuple, 'master')
# user = User(**user_dict, edu='master')
# user = User(name='bobby', age=29, height=175, edu=29)

user_tuple_new = ('bobby', 29, 175, 29)
user_dict_new = {
    'name': 'bobby',
    'age': 29,
    'height': 175,
    'edu': 29
}
user_list_new = ['bobby', 29, 175, 29]
# 需要补全全部参数才能使用 _make 方法
user = User._make(user_tuple_new)
print(user.age, user.name, user.height, user.edu)

# 转为 dict
user_info_dict = user._asdict()
print(user_info_dict)
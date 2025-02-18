# coding:utf-8

from functools import reduce

frunts = ['apple', 'banana', 'orange']

result = filter(lambda x: 'e' in x, frunts)
print(result)
print(list(result))
print(frunts)

def filter_func(item):
    if 'e' in item:
        return True
print('-------')
filter_result = filter(filter_func, frunts)
print(type(filter_result))
print(list(filter_result))

map_result = map(filter_func, frunts)  # > all
print(list(map_result))

map_result = map(lambda x, y: x * y, [1, 1, 2, 4, 4], [1, 1, 2, 4, 4])
print("map_result:", map_result)
print("map_result:", list(map_result))

reduce_result = reduce(lambda x, y: x * y, [1, 1, 2, 4, 4])
print(reduce_result)

reduce_result_str = reduce(lambda x, y: x + y, frunts)
print(reduce_result_str)

my_list = [1, 2, 3, 4, 5]

# 使用map()函数和lambda表达式与enumerate()结合
result = list(map(lambda x: (x[0] * 2, x[1] * 2), enumerate(my_list)))

for index, value in result:
    print(f'Index: {index}, Value: {value}')
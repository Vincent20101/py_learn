from collections import deque
import copy

from queue import Queue

# deuue GIL是线程安全的， list 不是线程安全的

user_list = ['bobby', 'bobby2']
user_name = user_list.pop()
print(user_name, user_list)

user_list_new = deque(('bobby', ['bobby2', 'bobby3']))
named_tuple = ('bobby', 29, 175)
user_list_new.append(named_tuple)
user_list_new.appendleft("bobby8")
user_deque = user_list_new.copy()
print(id(user_deque), id(user_list_new))

user_list_new[2].append('bobby10')
print(user_list_new, user_deque)

user_deque2 = copy.deepcopy(user_list_new)
user_list_new[2].append('bobby12')
print(id(user_deque2), id(user_list_new))
print(user_deque2,user_list_new)

user_deque2.extend(user_list_new)
user_deque2.insert(0, 'bobby11')
user_deque2.reverse()
print(user_deque2)


from collections import defaultdict

user_dict = {}
users = ['bobby1', 'bobby2', 'bobby3', 'bobby1', 'bobby2', 'bobby2']
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1

print(user_dict)

# default_dict = defaultdict(list)
default_dict = defaultdict(int)
print(default_dict['bobby'])
for user in users:
    default_dict[user] += 1
print(default_dict)


def gen_default():
    return {
        "name": "",
        "nums": 0
    }

default_dict_new = defaultdict(gen_default)
print(default_dict_new["group1"])
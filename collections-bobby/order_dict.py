from collections import defaultdict, OrderedDict

user_dict = OrderedDict()
user_dict["x"] = "bobby1"
user_dict["v"] = "bobby2"
user_dict["z"] = "bobby3"
print(user_dict)
print(user_dict.move_to_end("v"))
print(user_dict)
print(user_dict.popitem())
print(user_dict.pop('x'))



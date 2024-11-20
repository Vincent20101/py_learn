from collections import ChainMap

user_dict1 = {"a": "bobby1", "b": "bobby2"}
user_dict2 = {"b": "bobby22", "d": "bobby3"}

new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict["d"])
print(new_dict)
# new_dict.new_child({"aa": "bobby4", "bb": "bobby5"})
print(new_dict.maps)
new_dict.maps[0]["a"] = "bobby"
for key, value in new_dict.items():
    print(key, value)
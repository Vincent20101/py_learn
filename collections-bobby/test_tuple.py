user_tuple = ('bobby', 29, 175)
print(user_tuple[1])
# 元组拆包及变式
name, age, height = user_tuple
name1, age1 = user_tuple[:2]
name2, *others = user_tuple  # 只对name属性感兴趣

print(name, age, height)
print(name1, age1)
print(name, others)

# 元组不可变性不是绝对的
name_tuple = ('bobby1', [29, 175])
name_tuple[1].append(22)
print(name_tuple)

# tuple 因为可哈希, 所以可以作为 dict 的 key
user_info_dict = {}
user_info_dict[user_tuple] = "bobby"
print(user_info_dict)
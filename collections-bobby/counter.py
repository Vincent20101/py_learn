from collections import Counter

users = ['bobby8', 'bobby','bobby2','bobby', 'bobby2', 'bobby3', 'bobby10']
user_counter = Counter(users)
print(user_counter)

user_counter1 = Counter("sfdfsfjnlsdfsdfljjf")
user_counter1.update("dssdggss")
print(user_counter1)

user_counter2 = Counter("sdfsdfsdfsdf")
user_counter1.update(user_counter2)
print(user_counter)

# top_n 的問題  堆
print(user_counter.most_common(2))
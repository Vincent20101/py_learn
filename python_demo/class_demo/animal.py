class Animal(object):
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1

dog = Animal('wangwang', 1)
print(Animal.count)
cat = Animal('mimi', 3)
print(Animal.count)
pig = Animal('panpan', 1)
print(Animal.count)
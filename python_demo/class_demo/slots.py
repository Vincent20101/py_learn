class Person(object):
    # __slots__的目的是限制当前类所能拥有的属性，避免因为外部属性的操作导致类属性越来越难以管理。
    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    __slots__ = ('score',)

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
# s.age = 10 // error
print(s.score)
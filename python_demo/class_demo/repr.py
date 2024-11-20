# Enter a code
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    # def __str__(self):
    #     return 'Student: {}, {}, {}'.format(self.name, self.gender, self.score)
    def __repr__(self):
        return 'Student: {}, {}, {}'.format(self.name, self.gender, self.score)

s = Student('Bob', 'Male', 88)
print(s)
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin, Student):
    pass

class FTeacher(FootballMixin, Teacher):
    pass

s = BStudent()
print(s.skill())

t = FTeacher()
print(t.skill())
class student:
    school = 'Flicon High'   # class variables work with class methods

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, values):
        self.m1 = values

    @classmethod # This is a decorator
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a student class in the module')

s1 = student(34,60,53)
s2 = student(89,94,21)

print(s2.avg())
print(student.get_school())

student.info()
# to fetch values you use accessors...to modify values you use mutators


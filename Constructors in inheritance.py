'''class A():

    def __init__(Self):
        print('in a init')

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')

class B(A):

    def __init__(Self):
        super().__init__()
        print('in b init')

    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')

a1 = B()'''

class A():

    def __init__(Self):
        print('in a init')

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')

class B():

    def __init__(Self):
        print('in b init')

    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')

class C(A,B):
    def __init__(Self):
        super().__init__() #Because of Method Resolution Order(MRO), it'll print the init of class A
        print('in c init')
    def feat(self):
        super().feature2()

a1 = C()
a1.feat()
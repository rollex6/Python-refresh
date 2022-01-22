# Inheritance: Types of inheritance

# Single level inheritance 

class A():
    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')

class B(A):     #including (A) into class B makes class B inherit all the features of class A
    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')

# In this single level inheritance, A is the SuperClass and B is the SubClass


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature4() # b1 can access thr features of both class A and Class B

# The above script is an example of SINGLE LEVEL INHERITANCE



# MultiLevel inheritance

class C():  #grand parent class
    def feature5(self):
        print('feature 5 is working')

    def feature6(self):
        print('feature 6 is working')

class D(C):    #Parent class #including (C) into class B makes class B inherit all the features of class A
    def feature7(self):
        print('feature 7 is working')

    def feature8(self):
        print('feature 8 is working')

class E(D):    #child class # including D into class E(child class) makes class E inherit all the features of class A which means it automatically inherits the features of class C
    def feature9(self):
        print('feature 9 is working')

c1 = C()
c1.feature5()
c1.feature6()

d1 = D() # d1 can access all the features from class C to class D
d1.feature5()
d1.feature6()
d1.feature7()
d1.feature8()

e1 = E()  #e1 can access all the features from class C, class D and class E
e1.feature5
e1.feature6()
e1.feature7()
e1.feature8()
e1.feature9()


# Multiple inhetitance
class G():  
    def feature10(self):
        print('feature 10 is working')

    def feature11(self):
        print('feature 11 is working')

class H():
    def feature12(self):
        print('feature 12 is working')

    def feature13(self):
        print('feature 13 is working')

class I(G,H): #class I can access the features of both class G and class H
    def feature14(self):
        print('feature 14 is working')

i1 = I()

i1.feature10()
i1.feature11()
i1.feature12()
i1.feature13()
i1.feature14()
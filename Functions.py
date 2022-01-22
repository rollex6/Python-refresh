# Functions

def greet():
    print('Hello')
    print('Good morning')

greet()

def add(x,y):
    c = x + y
    print(c)

add(5,3)

def add_sub(x,y):
    c = x + y
    d = x - y
    print(c,d)

add_sub(5,6)

def add_mult(x,y):
    c = x + y
    d = x * y
    return c,d

addition,multiplication = add_mult(5,6)
print(addition,multiplication)

def person(name,age):
    print('my name is ', name ,', and I am ', age , 'years old.')

person(name='Rawlings', age=23)

def baby(name, month=10):
    print(name, ' is a baby because he/she is ', month, 'months old')

baby('elijah')
baby('elijah', 6)

def sum(a,*b):
    c = a
    for i in b:
        c = c + i
    print(c)

sum(2,2,2,2,4)

def person(name, **data):
    print(name)
    print(data)

person('rollex', age = 23, city = 'PH', mob = 90345)

def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('rollex', age = 23, city = 'PH', mob = 90345)

class car:

    wheels = 4  # this is a class(static) variable because it was created outside the __inir__ function

    def __init__(self):
        self.brand = 'BMW'  # This is an instance variable because it was created within the __init__ function
        self.length = 10    # This is an instance variable because it was created within the __init__ function

c1 = car()
c2 = car()

c1.length = 6
c2.brand = 'Honda'
print(c1.brand, c1.length, c1.wheels)
print(c2.brand, c2.length, c2.wheels)
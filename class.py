class computer:
    def __init__(self):
        self.name = 'Rollex6'
        self.age = 23


    def update(self):
        self.age = 30

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False

c1 = computer()
c1.age = 20
c2 = computer()

if c1.compare(c2):
    print('They are same')
else:
    print('They are not same')

c1.name = 'Rex'
c1.age = 12


print(c1.name)
print(c2.name)

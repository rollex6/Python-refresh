# Arrays

from array import *
values = array('i', [5,9,2,6,7])
print(values)
print (values.typecode)
values.reverse()
print(values)
values.append(3)
print(values)

for num in values:
    print(num)
    
# creating a new array with the same values in 'values'

newarray = array(values.typecode, (num for num in values))
print(newarray)

# if you want the values in newarray to be double of what is in values
newarray = array(values.typecode, (num*num for num in values))
print(newarray)
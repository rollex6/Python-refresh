from numpy import *

arr1 = array([1,2,3,4])
arr2 = array([2,4,6,8])

print(concatenate([arr1,arr2]))

# Two types of copy: Shallow copy(edits changes for both paths) and Deep copy (edits changes for one side)
# copying arrays

# For shallow copying
arr1 = array([1,3,5,7,9])
arr2 = arr1.view()
print (arr2)

arr1[1] = 9

print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))

# For deep copying
ary1 = array([3,4,5,7])
ary2 = ary1.copy()
print(ary2)

ary1[1] = 0

print(ary1)
print(ary2)

print(id(ary1))
print(id(ary2))
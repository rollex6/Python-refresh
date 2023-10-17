'''
def happy_new_year(wishes = True): 
    print("Three...") 
    print("Two...") 
    print("One...") 
    if not wishes: 
        return 
    print("Happy New Year!")

happy_new_year(2021)


def boring_function(): 
    return 123 
x = boring_function() 
print("The boring_function has returned its result. It's:", x) 


def boring_function(): 
    print("'Boredom Mode' ON.") 
    return 123 
print("This lesson is interesting!") 
boring_function() 
print("This lesson is boring...")
#the code does not return 123 because it is not assigned to a variable


def list_sum(list): 
    s = [] 
    for elem in range(0,list): 
        s.insert(0,elem)
    return s
print(list_sum(5))
'''

def my_function(my_list_1): 
    print("Print #1:", my_list_1) 
    print("Print #2:", my_list_2) 
    my_list_1 = [0, 1] 
    print("Print #3:", my_list_1) 
    print("Print #4:", my_list_2) 
my_list_2 = [2, 3] 
my_function(my_list_2) 
print("Print #5:", my_list_2)
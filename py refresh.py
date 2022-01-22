print('Welcome to Stem movie selection program \n Please enter your age')
age = int(input())
if age > 70:
    print('Go watch African Magic')
elif age >= 50 :
    print('Go watch Netflix')    
elif age >= 19:
    print('Go watch Avengers')
elif age >= 7:
    print("Go to 'room 1' the childrens room") 
    if age >= 12:
        print('Go watch Power Rangers')
    elif age >= 7:
            print ('Go watch Barny and friends')
else:
    print('Go find your Mama')
print('Thank you for using stem')
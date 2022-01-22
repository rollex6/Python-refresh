# continue vs break vs pass
print('for continue function')
# continue is used for skipping outpot
for letter in range(5):
    
    if letter == 3:
        continue
    print ('hi', letter)

print ('for pass function')
# pass is used to skip variable/print definition
for letter in range(5):
     pass
  

print('for break function')
# brak terminates operation after condition is met
for letter in range(5):
    
    if letter == 3:
        break
    print ('hi', letter)


a = [1,2,3,4,5]  # list
print(type(a))
b = (1,2,3,4,5) # tuple
print(type(b))
 
print('a = ' + str(a))
for i in range(5):
    print('i={},value={}'.format(i,a[i]))
   
print('b = ' + str(b))
for i in range(5):
    print('i={},value={}'.format(i,b[i]))
   
# So what is the difference? Try to alter a single value
a[2] = 30
print(a)
b[2] = 30
# the values in a tuple are not subject to change
#------------------
 
# Dictionary
eng_spa = {'one': 'uno', 'two':'dos', 'three':'tres', 'four':'cuatro', 'five':'cinco'}
print(eng_spa['two'])
print(eng_spa['dos'])
 
# altering is allowed
eng_spa['two'] = 'zwei'
print(eng_spa['two'])
 
#printing keys
eng_spa.keys()
list(eng_spa.keys())
 
#printing values
eng_spa.values()
list(eng_spa.values())
 

# Loop for all keys and values
for k,v in eng_spa.items():
    print(f'key={k}, value={v}')
   
# note that keys and values in a dictionary-type value can be of any type themselves
d = {1:'one', 'two':True, 7.0:None, False:[1,'sth',True]}
print(d[1])
print(d['two'])
print(d[7])
print(d[False])
print(d[10])
 
# Adding to a dictionary
d['New item'] = 33
print(d)
 
# deleting
del d['New item']
print(d)
 
# checking if an item is in your dictionary
1 in d
8 in d
 
# Task 1
# Why is the 0 item missing when printing the below?
e = {0:'zero', 'two':True, 7.0:None, False:'Not true'}
print(e)
 
 
# Additional info
a = [1,2,3,4,5]
b = a
c=a.copy()
print(id(a))
print(id(b))
print(id(c))
 
a[2]=324
# what will be the values of b and c now?
print(b)
print(c)
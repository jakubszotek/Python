v1 = 1
print(v1)
print(type(v1))

v2 = [1,2,3,4,5,6,7,8,9,10]
print(v2)
print(type(v2))

v3 = v2[0]
print(v3)

v4 = v2[10]

# Conclusion: lists in Python are indexed starting from 0

# Subsets of lists
v5 = v2[1:5]
print(v5)

v6 = v2[:5]
print(v6)

v7 = v2[5:]
print(v7)

v8 = v2[-1]
print(v8)

v9 = v2[-5:-3]
print(v9)

v10 = v2[4::2]
print(v10)
#---------------


# Other operations on lists
w = [1,2,3,5,4,3,6,5,3,3]
print(w.index(3))   # what is the first position of number 3?
print(w.index(3,4)) # what is the first position of number 3 starting from position number 4

print(w.count(3))   # number of occurences

w.sort()
print(w)

w.sort(reverse=True)
print(w)

w.append(18)    # adds an element at the end of the list
print(w)

w.remove(5) # removes an alement but only the first occurence
print(w)

w.pop(1)    # removes item from specified position
print(w)
w.pop()     # removes last item
print(w)

w.extend([10,11])   # allows adding other lists
print(w)
w = w + [12,13]     # same as above
print(w)

w.insert(2,22)      # inserting a item in the specified position
print(w)
#---------------

# Please take a look at these examples
z = ['a', 4, [3, 5], ['abc', 'ijk', 'xyz']]

print(z[0])
print(type(z[0]))

print(z[2])
print(type(z[2]))

print(z[2][0])
print(type(z[2][0]))

print(z[3])
print(type(z[3]))

print(z[3][1])
print(type(z[3][1]))

print(z[3][1][0])
print(type(z[3][1][0]))
#---------------




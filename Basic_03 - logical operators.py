a = 1
b = 2
c = 4
l = [1,2,3]
s = {1,2,3}
t = (1,2,3)
d = {1:'one',2:'two',3:"three"}
 
print(a>b)
print(not(a>b))
print(a<b and b<c)
print(a<b or b<c)
 
print(a == b)  # Remember double equality sign when checking for equality
print(a != b)
 
# checking for appearance
print(a in l)
print(c in l)
print(c in range(10))
 
print(a in s)
print(c in s)
 
print(a in t)
print(c in t)
 
print(a in d)
print(c in d)
 
 
# Short circuiting
# Why does the first line work and the second doesn't?
print(a == 1 or l[5] == 6)
print(l[5] == 6 or a == 1)
 
# Task 1 - Precedence
# Explain the results of the below
print(True and True or False and False)
print(True or True and False or False)
print(1<2**-2)
print(1<2**-2==0)
print(1<3<2)
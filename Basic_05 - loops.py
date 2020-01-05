# Fibonacci numbers with a 'while' loop
 
def fib(n = 10):
    x1 = 1
    if n >= 1:
        print(x1)
    x2 = 1
    if n >= 2:
        print(x2)
    i = 3
    while(i <= n):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        print(x3)
        i += 1
       
fib(20)
 
 
# Squares with 'for' loop
for x in range(1,10):
    print(x**2)
       
# 'for' loop for each element on a list
a = [1,-1,2,-2]
for item in a:
    print(item*5)
   
# compact way:
b = [item*5 for item in a]
print(b)

# break and continue
for i in range(0,10):
    if i==3: break
    print(i)
 
for i in range(0,10):
    if i % 3 == 0: continue
    print(i)


# Task 1
# Find the highest and the lowest value of the below function in a specified range of integers
def fun(n):
    return -n^5+14*n^4-20*n^3+n-2

def max_and_min(start = 1, end = 11):
    
    max_value = 
    min value =
    return max_value, min_value


# Task 2
# write a function that will sum the number from 1 to n except those that divide by a specified parameter.
# example: sum_except(10,3) should return 1+2+4+5+7+8+10 which is 37
def sum_except(n, divisor):
    value = 0
    for i in range():
       
    return value
 
#check
print(sum_except(n=4, divisor=2))
print(sum_except(n=10, divisor=1))
print(sum_except(n=15, divisor=5))
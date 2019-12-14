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


# Task 1
# Find the highest and the lowest value of the below function in a specified range of integers
def fun(n):
    return -n^5+14*n^4-20*n^3+n-2

def max_and_min(start = 1, end = 11):
    
    max_value = 
    min value =
    return max_value, min_value
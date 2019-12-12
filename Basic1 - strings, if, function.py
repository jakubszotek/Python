# Defining a variable and printing it
a = 0
b = "hello"
c = "world"
print(a)
print(b)
print(c)
 
# Concatenation of strings
d = b + ' ' + c
print(d)
 
# Try to execute the below
print(b + a)
 
# Since b is a string Python expects to see a string and we have a number there
# solution:
print(b + str(a))
 
 
# ------- A simple function -------
def first_function():
    a = 10
    print(a)

# Remember that we have already defined variable a above?
# What will the below statements return?
first_function()
print(a) 

# That's because parameter a in the function is a local variable and is stored just for the purpose
# of this function. The other a used outside of the function is a global variable
 

# ------- Using arguments in a function -------
def hello(nm, surnm):
    print('hello ' + nm + ' ' + surnm)
   
hello("John","Smith")

 
# Using arguments with default values
def hello2(nm = "John", surnm = "Smith"):
    print('hello ' + nm + ' ' + surnm)

hello2(surnm = "Kowalski")

  

# ------- Using "if" -------
a = 10
b = -3*a^3+18*a^2+4*a
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")

 

# ------- Task 1 -------

# Create a function that solves a quadratic equation ax^2 + bx + c == 0. Think what default values could be used
def quadratic_equation(a = , b = , c = ):

    x1 =
    x2 =
    return [x1, x2]
 

# Let's test your function
result1 = quadratic_equation(a = 1, b = 7, c = 12)
print(result1)

result2 = quadratic_equation(a = 1, b = -2, c = 1)
print(result2)

result3 = quadratic_equation(a = 1, b = 2, c = 4)
print(result3)

result4 = quadratic_equation(b = 2, c = 4)
print(result4)
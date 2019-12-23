# working with classes
#defining
class myClass():
    def function1(self):
        print("Hello 1!")
    def function2(self, txt):
        print("Hello " + txt + "!)

# using a class      
a = myClass()
a.function1()
a.function2("John")
 
# Inheriting
class yourClass(myClass):
    def function2(self, txt):
        print("Goodbye!")
        myClass.function1(self)
       
b = yourClass()
b.function1()
b.function2("John")
 
 
 
 
# self and __init__
# self represents the instance of the class
# __init__ is a constructor in object oriented concepts
class Paper_sheet():
    def __init__(self,length, height):
        self.length = length
        self.height = height
        self.diagonal = (self.length**2 + self.height**2)**0.5
       
    def get_area(self):
        return self.length * self.height
   
    def diagonal_convert(self, ratio):
        return self.diagonal * ratio
       
r = Paper_sheet(length = 10, height = 5)
print(r.diagonal)
print(r.get_area())
print(r.diagonal_convert(0.393701))
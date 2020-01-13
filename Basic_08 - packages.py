# Numpy
import numpy as np

# Creating array from list with type float 
a = np.array([[10, 11, 12], [13, 14, 15]], dtype = 'float') 
print(a)
print(a[1,2])

# Transpose
at = a.T
print(at)
# Reshape the array
b = a.reshape(3,2)
print(b)
c = a.reshape(1,-1)
print(c)
d = a.reshape(-1,1)
print(d)

# Create a matrix of zeros
zer = np.zeros((3,4))
print(zer)

# Create a matrix of ones
ones = np.full((2,4),1)
print(ones)

# Create an array of random values
ra = np.random.random((3,5))
print(ra)

# Create a sequence of integers  
# from 0 to 30 with steps of 5 
ran = np.arange(0, 30, 5) 
print(ran) 
  
# Create a sequence of 10 values in range 0 to 5 
lin = np.linspace(0, 5, 10) 
print(lin)

# Flatten
fl = a.flatten()
print(fl)
#--------------

# Slicing
# Just as a regular list a numpy arrays can be sliced
arr = np.array([[-1, 2, 0, 5, 7], 
                [4, -0.5, 6, -1, 2], 
                [2.6, 0, 7, 3, 0], 
                [3, -7, 4, 6, -3]]) 
sli = arr[1:3, 1:]
print(sli)

# Conditions
cond = arr > 2
print(cond)
temp = arr[cond]
print(temp)

# Operations
regular_list = [1,2,3]
regular_list2 = [4,5,6]
np_list = np.array([1,2,3])
np_list2 = np.array([4,5,6])
print(regular_list+1)
print(np_list+1)
print(regular_list*5)
print(np_list*5)
print(regular_list**2)
print(np_list**2)
print(regular_list + regular_list2)
print(np_list + np_list2)

# Max, Min, Sum
print(arr.max())
print(arr.max(axis = 0))
print(arr.max(axis = 1))
print(arr.sum(axis = 0))
print(arr.sum(axis = 1))
#--------------


# Pandas
import pandas as pd
data = pd.read_csv("D:\Materialy\Python\Basic_08 - data.csv")
print(data)
print(data['Name'])
print(data['Name'][1])

#Selecting data
sel = data[['Name','Surname']]
print(sel)
print(data.iloc[1,:]) # select all columns in the first row
print(data.iloc[:,1]) # select all rows in the first column

# Filter, sort
# filter all people with age above 25
above_25 = data[data['Age'] > 25]
print(above_25)
# sort by surname in descending order
data.sort_values('Surname', ascending = False)
print(data)
#--------------


# Task 1
# Find names of people that are
# Taller than 175
taller_175 =
# older than the mean age
older_than_mean = 

#Creating arrays with numpy
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(f"{arr1} and type is {type(arr1)}" )

#2- D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# 3 D array
arr3 = np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)

# To check the dimensions of the array use "ndim" attribute which returns integer.
print("dimesnion of array1", arr1.ndim)
print("dimesnion of array2", arr2.ndim)
print("dimesnion of array3", arr3.ndim)

# creating N dimensional array. can be created using ndmin attribute
arrn= np.array([1,2,3,4,5], ndmin=5)
print(arrn)

# Accesing array elements
r1= arr1[0]
r2= arr1[4]
print("0th element of array1 is ", r1)
print("4th element of array1 is ", r2)

# Accesing 2-D or matrices elements
print(arr2)
print("Access 2nd rows 3rd element", arr2[1,2])

# Accessing 3-D array elements
print(arr3)
print("Access 3rd row 2nd element", arr3[1,0,1])

# Negative indexing
print("Access last element of 3-D array", arr3[1,1,-1])
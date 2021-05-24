#Task 1
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

import numpy as np
def list_to_array(my_list):
	my_array = np.array(my_list)
	return my_array
my_list = [1,2,3,4,5,2334,323,546,43]
print(list_to_array(my_list))

# Task 2
# Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
def array_range(down,up):
	my_array = np.arange(down,up)
	return my_array
print(array_range(2,11))
# Task 3
# Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
def update_sixth():
	my_null = np.zeros(10)
	my_null[5:8] = 11
	return my_null
print(update_sixth())
# Task 4
# Write a NumPy program to test whether each element of a 1-D
#  array is also present in a second array
def check_numbers(array_1,array_2):
	result = np.in1d(array_1,array_2)
	return result
array_1 = np.array([12.,234.,45.,12.,4.,456.,1.,36.,4.,6.])
array_2 = np.array([323.,4.,6.,23.,6.,7.,34.,65.,7.])
print(check_numbers(array_1,array_2))

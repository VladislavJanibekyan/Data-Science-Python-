#Task 1
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

import numpy as np
my_list = [1,2,3,4,5,2334,323,546,43]
my_array = np.array(my_list)
print(my_array)

# Task 2
# Write a NumPy program to create a NumPy array with values ranging from 2 to 10.
my_array = np.arange(2,11)
print(my_array)

# Task 3
# Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.
my_null = np.zeros(10)
my_null[5:8] = 11
print(my_null)

# Task 4
# Write a NumPy program to test whether each element of a 1-D
#  array is also present in a second array
array_1 = np.array([12,234,45,12,4,456,1,36,4,6])
array_2 = np.array([323,4,6,23,6,7,34,65,7])
new_list = []
for i in array_1:
	for j in array_2:
		if i == j:
			new_list.append(i)
print(set(new_list))

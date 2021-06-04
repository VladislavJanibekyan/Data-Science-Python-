import numpy as np
# Task 1
# Write a NumPy program to compute the multiplication of two given matrixes

def matrices_mult(x,y):
	if len(x[0]) == len(y):
		mult = x.dot(y)
	else:
		print("not possible")
	return mult 
first = np.array([[1,3,4],[2,3,1], [4,5,2]])
second = np.array([[2,4],[5,6],[3,5]])
print(matrices_mult(first,second ))

# Task 2
# Write a NumPy program to compute the determinant of an array

def matrices_determinant(x):
	return np.linalg.det(x)

mat = np.array([[1,3,4],[2,3,1], [4,5,2]])
print(matrices_determinant(mat))

# Task 3
# Write a NumPy program to compute the sum of the diagonal element of a given array

def matrices_diag(x):
	result = 0
	index = 0
	value = True
	while value:
		try:
			result = x[index][index] + result
			
			index += 1
		except:
			value = False


	return result 
mat = np.array([[1,3,4],[2,3,1], [4,5,2]])
print(matrices_diag(mat))



# Task 4
# Write a NumPy program to compute the inverse of a given matrix

def inv_mat(x):
	return np.linalg.inv(x)

mat = np.array([[1,3,4],[2,3,1], [4,5,2]])
print(inv_mat(mat))


# Task 5 
# Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.

def final():
	x = np.arange(100)
	np.save("final_mat", x)
	file = np.load('final_mat.npy')
	return file
print(final())

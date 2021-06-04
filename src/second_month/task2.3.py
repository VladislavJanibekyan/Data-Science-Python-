import numpy as np
from numpy.random import random
from numpy import newaxis
# Task 1
# Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները։
def max_min(x):
    return x.max(), x.min()

mat = random((5,5))
print(mat)
print(max_min(mat))

# Task 2
# Գրել ծրագիր, որը բազմաչափ NumPy
#  զանգվածում կգտնի նրա մաքսիմում և մինիմում արժեքները ըստ երկրորդ սյան։

def max_min_coulm(x):
	return x[1].max(), x[1].min()

mat = random((5,5))
print(mat)
print(max_min_coulm(mat))

# Task 3
# Գրել ծրագիր, որը բազմաչափ NumPy զանգվածում կգտնի նրա մեդիանան։  
def med(x):
	return np.median(x)
mat = random((5,5))
print(mat)
print(med(mat))


# Task 4
# Ստեղծել միաչափ և երկչափ NumPy զանգվածներ և բազմապատկել իրար։

def broad(x,y):
	x = x[:,newaxis]
	
	result = x + y
	return result

arr_1 = np.array([23,3,4,2,4,3])
arr_2 = np.array([22,3,4])
print(broad(arr_1,arr_2))

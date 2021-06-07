import pandas as pd
import numpy as np
# Task1
# Write a Pandas program to add, subtract, multiple and divide two Pandas Series
def ser_math(x,y):
    add = x + y
    sub = x - y
    mult = x * y
    div = x/y
    return add,sub,mult,div

new_s = pd.Series([3,4,5,6,7])
new_s2 = pd.Series([5,7,3,7,5])
print(ser_math(new_s,new_s2))

# Task 2
# Write a Pandas program to convert a dictionary to a Pandas series.
def pand_dic(x):
    return pd.Series(x)
print(pand_dic({"a":45,"b":34,"g":567}))

# Task 3
# Write a Pandas program to convert a NumPy array to a Pandas series

def pand_arr(x):
    return pd.Series(x)
arr = np.random.random(5)
print(pand_arr(arr))

# Task 4
# Write a Pandas program to convert the first column of a DataFrame as a Series

def first_col(x):
    return pd.Series(x.iloc[:,0])

data = {"state":["ohio","nevada","california"],
        "year":[2000,2021,2003]}

print(first_col(pd.DataFrame(data)))


# Task 5
# Write a Pandas program to sort a given Series
def sort_ser(x):
    return x.sort_index(), x.sort_values()

ser = pd.Series([3,334,2,6,3], index = ["d","s","f","j","l"])
print(sort_ser(ser))

# Task 6
# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive). 
# Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)

print(df[df['score'].between(15, 20)])

# Task 7
# Write a Pandas program to calculate the sum of the examination attempts by the students.
# Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


df = pd.DataFrame(exam_data,index= labels)
print(df["attempts"].sum())
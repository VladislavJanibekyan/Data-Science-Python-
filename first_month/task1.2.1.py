# Task 1
# Write a Python program to get the largest number from a list.
my_list = [3, 5, 6, 3, 4, 34, 5465, 123, 432, 43, 6, 56758, 56]
my_list.sort(reverse=True)
print('the largest number is:', my_list[0])

# Task 2
# Write a Python program to get the frequency of the given element in a list to.  

my_list = [3, 5, 6, 3, 4, 34, 5465, 123, 432, 5,  43, 6, 56758, 5,  56]
freq = my_list.count(5)
print(f'the frequency of 5 in a list is {freq} times.')

# Task 3
# Write a Python program to remove the second element from a given list, if we 
# know that the first elements index with that value is n. 

my_list = [3, 5, 6, 3, 4, 34, 5465, 123, 432, 5,  43, 6, 56758, 5,  56]
n = my_list.index(5)
new = my_list[n+1:]
new.remove(5)
result = my_list[:n+1] + new
print(result)
# Task 1
# Write a python program which returns a given list without duplicates.

my_list = [3,4,6,7,2,'f','dfb',2,'r',5,6,3,'d','f','g']

print(set(my_list))


# Task 2
# Write a python program which returns common elements of 2 lists.

first_list = [2,3,6,5,2,6,4,3,4,7,4,5]
second_list = [2,5,5,7,5,3,6,4,6,8]

print(set(first_list) & set(second_list))


# Task 3
# Write a python program which return elements which are in first list but not in second

first_list = [2,3,6,5,2,6,4,3,4,7,4,5,9,0]
second_list = [2,5,5,7,5,3,6,4,6,8]

print(set(first_list) - set(second_list))

# Task 4
# Write a python program which return elements are or in first list, either in second, but not in both

first_list = [2,3,6,5,2,6,4,3,4,7,4,5,9,0]
second_list = [2,5,5,7,5,3,6,4,6,8]

print(set(first_list) ^ set(second_list))


# Task 5
# Write a python program which return elements which are or in first, either in second, or in both


first_list = [2,3,6,5,2,6,4,3,4,7,4,5,9,0]
second_list = [2,5,5,7,5,3,6,4,6,8]


print(set(first_list) | set(second_list))

# Task 6
# Write  python function which get set and element value, and remove from set element with given value if exist
my_set = {2,3,6,5,2,6,4,3,4,7,4,5,9,0}
number = 4
if number in my_set:
	my_set.remove(number)
print(my_set)


# Task 7
# Write a python python program, which return list from given set, where each element of list, is equal to cub of set element

my_set = {2,3,6,5,2,6,4,3,4,7,4,5,9,0}
list_set = []
for i in my_set:
	list_set.append(i**3)
print(list_set)




















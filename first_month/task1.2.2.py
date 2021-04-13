# Task 1
# gWrite a Python program to multiply all the items in a list.

my_list = [34,31,234,2,34,45,57,135,57]
x = my_list[0] * my_list[1]
for i in my_list[2:]:
    x = x * i 
print(x)

# Task 2
# Write a Python program to get the largest number from a list.

my_list = [34,31,234,2,34,45,57,135,57, 234234, 435, 2,34, 34,565, 34634634643, 34, 234]
largest_number = 0
for i in my_list:
    if i > largest_number:
        largest_number = i 
 
print("The lasrgest number is",largest_number)

# Task 3
# Write a Python program to generate and print a list except for the first 5 elements,
#  where the values are square of numbers between 1 and 30 (both included)

my_list = []
x = 1
while x <= 30:
    my_list.append(x**2)
    x += 1

print(my_list[4:])

# Task 4
# Write a Python program to remove duplicates from a list

my_list = [1,2,3,4,5,6,7,2,3,4,5]

for i in my_list.copy():
    if my_list.count(i) > 1:
        my_list.remove(i)

print("list without duplicates", my_list)

# Task 5
#  Write a Python program to find the most appeared element in a list.

my_list = [123,3,6, 454,3536,45,4,6,2,43,6,6,2,52,6,46,4,62,6,564,6,56]
most_appeared_times = 0
most_appeared = 0
for i in my_list:
    if my_list.count(i) > most_appeared_times:
        most_appeared_times = my_list.count(i)
        most_appeared = i


print(most_appeared)








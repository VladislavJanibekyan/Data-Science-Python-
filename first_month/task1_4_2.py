# Task 1
# Write a python program, which adds a new value with the given key in dict.
d = {2:"sdcdsc", "csdcsc":1122}
given_key = 4

d[given_key] = "sadsad"
print(d)

# Task 2
# Write a python program which concat 2 dicts.

d1 = {23:23423, 234: "Sdfsdf", 2432:456456, "$#346": "fdhfdh"}

d2 = {23:23423, 234: "Sdfsdf",21:"SDcsdc", 4:"sdfdsf", 2432:456456}

d1.update(d2)
print(d1)


# Task 3
# Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers

given_n = 234
my_dic = {}
for i in range(1,given_n+1):
	my_dic[i] = i **3

print(my_dic)

# Task 4
# Write a python program which create dict from 2 lists with the same length

l1 = [1,2,3,4,5,6,7,8,9]
l2 = ["sd",234,"sdv",5,6,7,6,"FGb",True]
d = {} 
for i in range(len(l1)):
	d[l1[i]]=l2[i]
print(d)

# Task 5
# Write a python program which gets the maximum and minimum values of a dictionary.

d = {1:324,2:2123,3:234234,4:4,5:2,6:78}
d_l = list(d.values())
d_l.sort()
print("highest is ", d_l[::-1][0])
print("lowest is ", d_l[0])

# Task 6
# Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict 
# will be an element with that key, and sum of values as value.

d1 = {1:2,2:3,3:4,6:7,4:5,5:8}
d2 = {11:3,22:45,56:478,4:4}

s_d1 = set(d1)
s_d2 = set(d2)


for i in (s_d1 & s_d2):
	d2[i] = d1[i] + d2[i]

d1.update(d2)
print(d1)


# Task 7
# Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string

s = "aksdlknsdjlfnsjd"
d = {} 
for i in s:
	d[i] = s.count(i)
print(d)























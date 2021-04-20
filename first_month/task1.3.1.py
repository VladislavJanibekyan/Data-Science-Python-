# Task 1
# Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.

def divider(a,b):
	if a % b == 0:
		return print('result:',True)
	else:
		return print('result:',False)

# divider(12,4)

# Task 2
# Write a Python function, which gets a number, and return True if that number is palindrome, 
# otherwise False

def palindrome(a):
	if str(a) == str(a)[::-1]:
		return print(f"number is palindrome because {a} == {str(a)[::-1]}")
	else:
		return print(f"number is palindrome because {a} != {str(a)[::-1]}")

# palindrome(565)

# Task 3
# Write a Python function, which gets a number, and return True if that number is prime,
# otherwise False.

def prime(a):
	c = bool
	for i in range(2,a+1):
		if a % i == 0 and a != i:
			c = False
			break
		else:
			c = True
	if c == True:
		return print("this number is prime")
	elif a == 2:
		return print("this number is prime")
	else:
		return print("this number is not prime")

prime(3)

# Task 4
# Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.

def perfect(a):
	factor_list = []
	for i in range(1,a):
		if a % i == 0:
			factor_list.append(i)
	if sum(factor_list) == a:
		return print("this number is a perfect number")
	else:
		return print("this number is not perfect")


# perfect(8128)

# Tasl 5
# Write a function, which gets 2 numbers, and return their Great common divisor - 

def gcd(a,b):
	factor_a = 0
	for i in range(1,b+1):
		if a % i == 0 and b % i ==0:
			factor_a = i
	return factor_a

print(gcd(4,6))	































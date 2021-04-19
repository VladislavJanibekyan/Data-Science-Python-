import task1_3_1
import timeit
# Task 1
# Write a Python function, which Implements the Euler function.
# Euler function is return a count of numbers not great than N, which are mutually simple with N. 
# Example  φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function which 
# returns a count of numbers mutually simple with given N.
def euler(n):
    start = timeit.default_timer()
    factor_n = []
    count = 0
    local_factor = []
    for i in range(2,n):
        if n % i == 0:
            factor_n.append(i)
    for i in range(2, n):
        local_factor = []
        for j in range(2,i+1):
            if i % j == 0:
                local_factor.append(j)
        for item in local_factor:
            if factor_n.count(item) > 0:
                count +=1
                break
    stop = timeit.default_timer()

    return n -(count+1), stop - start
print(euler(231))

def euler_(n):
    start = timeit.default_timer()
    count = 0 
    for i in range(1,n):
        if task1_3_1.gcd(i, n) == 1:
            count +=1
    stop = timeit.default_timer()
    return count, stop - start

print(euler_(231))

# Task 2
# Ticket numbers usually consist of an even number of digits. A ticket number is 
# considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.
# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    half = int(len(str(n)) / 2)
    first_half = str(n)[:half]
    second_half = str(n)[half:]
    first_half_result =0
    second_half_result = 0
    for i in first_half:
        first_half_result += int(i)
    for i in second_half:
        second_half_result += int(i)
    if first_half_result == second_half_result:
        return True
    else:
        return False


print(isLucky(239017))

# Task 3
# The robot is standing on a rectangular grid and is currently located at the point (X0, Y0). The coordinates are integers. 
# It receives N remote commands(list with n elements each of them is a command). Each command is one of : up, down, left, right. 
# Upon receiving a correct command, the robot moves one unit in the given direction. If the robot receives an incorrect command,
# it simply ignores it. Where will the robot be located after following all the commands?

def robot(n):
    x = 0
    y = 0
    for i in range(0,len(n),4):
        y += n[i]
    for i in range(1,len(n),4):
        y -= n[i]
    for i in range(2,len(n),4):
        x -= n[i]
    for i in range(3,len(n),4):
        x += n[i]
    return x, y

print(robot([45,34,67,34,23,65,78]))

# Task 4

# Write a python function, which returns the sum of digits of given number N.

def sum_dig(n):
    result = 0
    for i in str(n):
        result += int(i)
    return result

print(sum_dig(4234567))



# Task 5
# Write a python program to find the next smallest palindrome of a specified number. For example, for 119 next palindrome is 121. 

def next_palin(n):
    while not task1_3_1.palindrome(n):
        n += 1
        if task1_3_1.palindrome(n):
            break
        else:
            n+=1
    return n

print(next_palin(234))


















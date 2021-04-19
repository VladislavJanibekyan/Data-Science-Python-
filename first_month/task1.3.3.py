# Task 1
# Write a Python function which returns factorial value of given number n.

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n
print(fact(5))


# Task 2
# Write a Python function which returns the n-th element of the fibonacci series. 
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibo(n-1) + fibo(n-2)
        

print(fibo(5))
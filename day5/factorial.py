def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_simple(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
import sys
sys.setrecursionlimit(2000)
print(factorial(1000))
print(factorial_simple(1000))
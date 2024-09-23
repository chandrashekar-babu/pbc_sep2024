"""
Write a program to generate first 'n' fibonacci series

Example usage:
--------------
    >>> fib(10)
    0 1 1 2 3 5 8 13 21 34 

    >>> fib(20)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 

    >>> square(2)
    4

"""


def square(n):
    return n*n


def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == '__main__':
    from doctest import testmod
    testmod()

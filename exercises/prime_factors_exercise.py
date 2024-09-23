"""

Implement the prime_factors() function that should return a
list of prime factors for a number passed as its argument.

Example:
--------
     >>> prime_factors(27)
     [3, 3, 3]

     >>> prime_factors(125)
     [5, 5, 5]

     >>> prime_factors(1221)
     [3, 11, 37]

     >>> prime_factors(100)
     [2, 2, 5, 5]

"""

def prime_factors(n):
    """
    Returns a list of prime factors of 'n' passed as
    argument.

    >>> prime_factors(3472)
    [2, 2, 2, 2, 7, 31]

    >>> prime_factors(15)
    [3, 5]

    """
    factors = []  # Accumulate prime factors of 'n' into this list.

    # TODO: Implement logic here.

    return factors


if __name__ == '__main__':
	import doctest
	doctest.testmod()


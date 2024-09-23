"""
Implement the findall() function below that should return
a list of indices all occurrence of a substring found in 
a string (both passed as arguments to the function).

Example usage:
--------------
   >>> quote = '''
   ... When I see a bird
   ... that walks like a duck
   ... and swims like a duck
   ... and quacks like a duck,
   ... I call that bird a duck
   ... '''

   >>> findall(quote, "duck")
   [37, 59, 82, 107]

"""

def findall(main_string, sub_string):
    """
    Returns a list of indices of each occurrence of
    sub_string in main_string

    Example usage:
    --------------
        >>> poem = '''
        ... A fly and flea flew into a flue,
        ... said the fly to the flea 'what shall we do ?'
        ... 'let us fly' said the flea
        ... and said the fly 'let us flee'
        ... and so they flew through a flaw in the the flue.
        ... '''

        >>> findall(poem, 'fly')
        [3, 43, 88, 120]

    """
    indices = []
    pass # TODO: Implement the logic here!
    return indices

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Running this program using 'python3 findall.py' should
    # ideally pass all tests in the doctest - on implementation
    # of findall() function


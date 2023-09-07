#!/usr/bin/python3
""" add two integers method"""


def add_integer(a, b=98):
    """  add two integres 
    
    a: the first number 
    b: the second number 

    raises 
    typeError : if a,b is not int or float 

    return 
    sum of two number 
    """

    if type(a) not in (int , float):
        raise TypeError('a must be an integer')
    if type(b) not in (int,float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

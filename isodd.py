#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 06.09.2019

def is_Odd(num):
    '''
    is_Odd(num) -> boolean

    Checks to see is a given number is an Odd number and returns a True or False.
    >>> is_Odd(5)
    True
    >>> is_Odd(8)
    False
    >>> is_Odd(10)
    False

    '''
    return num % 2 != 0

if __name__ == "__main__":
    print("The Number 10 not an 0dd Number and therefore returns : ", is_Odd(10))
    print("The Number 8 not an 0dd Number and therefore returns : ", is_Odd(10))
    print("The Number 5 is Odd Number and therefore returns : ", is_Odd(5))

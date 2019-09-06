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


print("The num 10 not 0dd: ", is_Odd(10))
print("The num 8 not 0dd: ", is_Odd(10))
print("The num 5 is an Odd number: ", is_Odd(5))

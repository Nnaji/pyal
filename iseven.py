#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 06.09.2019


def is_Even(num):
    '''
    is_Even(num) -> boolean

    Checks to see is a given number is an even number and returns a True or False.
    >>> is_Even(5)
    False
    >>> is_Even(8)
    True
    >>> is_Even(10)
    True

    '''
    return num % 2 == 0

if __name__ == "__main__":
    print("The Number 5 is not not even and therefore returns : ",  is_Even(5))
    print("The Number 10 is even and therefore returns : ",  is_Even(10))

#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 06.09.2019
def is_prime(num):
    '''
    is_prime(num) -> boolean

    Checks to see is a given numb is a prime and returns a True or False.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(8)
    False

    '''
    if num < 1:
        return False
    current = 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                current = i
    return current < 2

print("is 23 a prime number: ", is_prime(23))
print("is 3 a prime number: ", is_prime(3))
print("is 8 a prime number: ", is_prime(8))

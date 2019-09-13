#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 02.09.2019

def fib(n):
    """ fib(number) -> number
    fib takes a number as an Argurment and returns the fibonacci value of that number
    >>> fib(8) -> 21
    >>> fib(6) -> 8
    >>> fib(0) -> 1
    """
    y = {};
    if n in y.keys():
         return y[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
        y[n] = f
    return f

if __name__ == "__main__":
    print(" The 8th fibonaccifib number is : ",  fib(8))

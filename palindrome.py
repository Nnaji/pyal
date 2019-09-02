#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 02.09.2019

def is_palindrome(s):
    """ (str) -> true
    Returns true if the argument is a palindrome else false
    >>> is_palindrome("noon")
    True
    >>> is_palindrome("dented")
    False
    >>> is_palindrome("racecar")
    True
    """
    return s == s[::-1]


#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 03.09.2019

def is_Vowel(char):
    '''
    is_Vowel() -> boolean

    Checks to see is a given character is a vowel and returns a True or False.
    >>> is_Vowel("b")
    False
    >>> is_Vowel("i")
    True
    >>> is_Vowel("a")
    True

    '''
    vowels = "aeiou"
    to_lower_case = char.lower()
    result =  to_lower_case in vowels
    return result;

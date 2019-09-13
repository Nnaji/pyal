#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 02.09.2019

def is_palindrome(s):
    """ (str) -> boolean
    Returns true if the argument is a palindrome else false
    >>> is_palindrome("noon")
    True
    >>> is_palindrome("later")
    False
    >>> is_palindrome("radar")
    True
    """
    # converts (s) to lower case and assigns it to the variable word
    word = s.lower()
    return word == word[::-1]

if __name__ == "__main__":
    print("Is the word radar a Palindrome? : ", is_palindrome("radar"))
    print("Is the word Later a Palindrome? : ", is_palindrome("Later"))
    print("Is the word NOON a Palindrome? : ", is_palindrome("NOON"))


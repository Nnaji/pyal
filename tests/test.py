#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 10.09.2019

import sys
import unittest
sys.path.append("..")
import iseven
import palindrome
import fibonacci
import isodd
import prime
import vowels

class MyUnitTest(unittest.TestCase):
    def test_iseven(self):
        self.assertTrue(iseven.is_Even(10), "It should return true")
        self.assertFalse(iseven.is_Even(3), "It should return false")

    def test_isPalindrome(self):
        self.assertTrue(palindrome.is_palindrome("noon"), "Noon is a Palindrom")

    def test_fibonacci(self):
        self.assertEqual(fibonacci.fib(8), 21, "8 fibonacci should equal 21")

    def test_isodd(self):
        self.assertTrue(isodd.is_Odd(7), "It should return true")

    def test_prime(self):
        self.assertTrue(prime.is_prime(3), "It should return true")

    def test_vowel(self):
        self.assertTrue(vowels.is_Vowel("a"), "It should return true")
        self.assertFalse(vowels.is_Vowel("b"), "It should return false")

if __name__ == "__main__":
    unittest.main()


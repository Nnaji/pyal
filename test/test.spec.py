#!/usr/bin/env python3

#  @AUTHUR: Kingsley Nnaji <kingsley.nnaji@gmail.com>
#  @LICENCE: MIT
#  Creation Date: 10.09.2019

import sys
import unittest
sys.path.append("..")
import iseven
import palindrome

class MyUnitTest(unittest.TestCase):
    def test_iseven_function(self):
        self.assertTrue(iseven.is_Even(10), "It should return true")
        self.assertFalse(iseven.is_Even(3), "It should return false")

    def test_isPalindrome_function(self):
        self.assertTrue(palindrome.is_palindrome("noon"), "Noon is a Palindrom")

if __name__=="__main__":
    unittest.main()


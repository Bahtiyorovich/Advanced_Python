# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:14:06 2024

@author: Sherzodbek
"""

import unittest
from fibonachchi import is_fibonacci_number

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_numbers(self):
        # Fibonachchi ketma-ketligidagi sonlar
        self.assertTrue(is_fibonacci_number(0))
        self.assertTrue(is_fibonacci_number(1))
        self.assertTrue(is_fibonacci_number(2))
        self.assertTrue(is_fibonacci_number(3))
        self.assertTrue(is_fibonacci_number(5))
        self.assertTrue(is_fibonacci_number(8))
        self.assertTrue(is_fibonacci_number(13))
    
    def test_non_fibonacci_numbers(self):
        # Fibonachchi bo'lmagan sonlar
        self.assertFalse(is_fibonacci_number(4))
        self.assertFalse(is_fibonacci_number(6))
        self.assertFalse(is_fibonacci_number(7))
        self.assertFalse(is_fibonacci_number(9))
        self.assertFalse(is_fibonacci_number(10))

if __name__ == '__main__':
    unittest.main()

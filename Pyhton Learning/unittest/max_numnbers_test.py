# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:20:58 2024

@author: Sherzodbek
"""

import unittest
from three_numbers import maxNumbers

class MaxNumbersTest(unittest.TestCase):
    def test_max_number(self):
        self.assertTrue(maxNumbers(7, 6, 9), 9)
        
unittest.main()
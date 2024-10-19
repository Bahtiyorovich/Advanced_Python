# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:30:11 2024

@author: Sherzodbek
"""
import unittest
from circle import getArea, getPerimetr

class CircleTest(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975, 4)
        self.assertAlmostEqual(getArea(10),314.159)

    def test_circle_perimetr(self):
        self.assertAlmostEqual(getPerimetr(2), 12.56636)

unittest.main()
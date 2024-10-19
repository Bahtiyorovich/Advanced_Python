# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:41:59 2024

@author: Sherzodbek
"""

import unittest
from class_car import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        model = "Malibu"
        color = "Black"
        year = 2021
        self.price = 40000
        self.__km = 10000
        self.avto1 = Car(model, color, year)
        self.avto2 = Car(model, color, year, km = self.__km, price = self.price)
        
        
    def test_create_car(self):
        """Qiymatlarni borligini assertIsNotNone metodi bilan tekshirish"""
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNotNone(self.avto2.price)
        
        """assertIsNone metodi bilan qiymat yo'qligini tekshiramiz"""
        self.assertIsNone(self.avto1.price)
        
        """assertEqual metodi bilan qiymatlar tengligini tekshiramiz"""
        self.assertEqual(0, self.avto2.get_km())
        self.assertEqual(self.price, self.avto2.price)


    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)
        
    def test_set_km(self):
        self.avto1.set_km(self.__km)
        self.assertEqual(self.__km,  self.avto1.get_km())



unittest.main()


























        
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:41:43 2024

@author: Sherzodbek
"""

class Car:
    def __init__(self, model, color, year, km=0, price=None):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = 0
        
    def get_model(self):
        return self.model
    
    def get_full_info(self):
        return f"{self.model}, {self.color}, {self.year}, {self.price}"
    
    def set_km(self, km):
        self.__km += km
        
    def get_km(self):
        return self.__km
    
    def set_price(self, new_price):
        self.price += new_price
    
    def get_price(self):
        return self.price
    
    
# car1 = Car('Malibu', 'black', 2021, 30000)

# print(car1.get_full_info())
# car1.set_km(1000)
# print(car1.get_km())






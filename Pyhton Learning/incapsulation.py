# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:32:25 2024

@author: Sherzodbek
"""

from uuid import uuid4
class Avto:
    """Avtomobil classi"""
    __num_avto = 0
    def __init__(self, make, model, color, year, price, km):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1 

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
           print( "avtomobilning km ni o'zgartirib bo'lmaydi")


avto1 = Avto("GM", "Malibu premier", "black", 2023, 40000, 1000)


class Gm:
    pass

class Toyota:
    pass





































































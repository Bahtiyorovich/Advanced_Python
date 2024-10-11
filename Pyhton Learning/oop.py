# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:17:51 2024

@author: Sherzodbek
"""

# dir(object) - metodi yordamida istalgan obektning metodlarini ko'rishimiz mumkin
# __dict__ METODI
# Yuqorida zikr qilingan dunder metodlardan biri bu __dict__ metodi bo'lib,
 # bu metod obyketning xususiyatlarini lug'at ko'rinishida qaytaradi:



class Talaba:
    def __init__(self, ism, familya, yosh):
        self.ism = ism
        self.familya = familya
        self.yosh = yosh
        
    def get_name(self):
        return self.ism
    
    def get_age(self, year):
        return year - self.yosh
        
    def get_info(self):
        return f"{self.ism}, familyam {self.familya}, yoshim {self.yosh}da"
    
talaba1 = Talaba("Ali", "Valiyev", 20)

def see_methods(klass):
    """Talaba classi ichidagi metodlarni ko'rish funksiyasi"""
    return [method for method in dir(Talaba) if method.startswith("__") is False]

# amaliyot

class User:
    def __init__(self, email, username, fullname, phone_number):
        self.email = email
        self.username = username
        self.fullname = fullname
        self.phone_number = phone_number
        
    def get_full_info(self, age=None):
        return f"Ismi: {self.fullname}, phone number: {self.phone_number}"
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_phone_number(self):
        return self.phone_number
    
    def set_username(self, username):
        self.username = username
        
    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        
    def set_email(self, new_email):
        self.email = new_email
    
    
    
user1 = User("test@gmail.com", "pythonDev", "Yoqubov Sherzod", "+998933609798")


class Car:
    def __init__(self, model, color, price, year):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.ordinal_number = 1
        
        
    def set_year(self, new_year):
        """change the color of the car"""
        self.year = new_year

    def set_price(self, price):
        """change the price of the car"""
        self.price = price

    def update_ordinal_number(self):
        """change the ordinalnumber of the car"""
        self.ordinal_number += 1
        
    def get_mode(self):
        return self.model
    
    def get_color(self):
        return self.color


class Science:
    def __init__(self, science_name):
        self.science_name = science_name
        self.students_count = 0
        self.students_list = []
        
    def append_students(self, talaba):
        """adda new student"""
        self.students_list.append(talaba)
        self.students_count += 1
        
    def get_student_info(self):
        return [talaba.get_info() for talaba in self.students_list]
    
    


# Amaliyot

class Avto:
    def __init__(self, model, color, year, price, karobka):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.karobka = karobka
        self.walking = 0
        
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.color
    
    def get_year(self):
        return self.year
    
    def get_price(self):
        return self.price
    
    def get_karobka(self):
        return self.karobka
    
    def get_info(self):
        return f"My car: {self.model},color: {self.color}, year: {self.year}"
               
    def set_km(self, km):
        self.walking += km


class CarCity:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []
    
    def add_car(self, new_car):
        self.cars.append(new_car)
        
    def get_car_city(self):
        return [f"{car}" for car in self.cars]
    
    
car_shop = CarCity("CarBrand", "Namangan")

def see_car_city(name):
    return [name_car for name_car in dir(CarCity) if name_car.startswith("__") is False]
    
    
# print(see_car_city(CarCity))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    










































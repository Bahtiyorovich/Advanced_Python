# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:25:37 2024

@author: Sherzodbek
"""

class Shaxs:
    def __init__(self, ism, familya, passport, t_yil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.t_yil = t_yil
        
    def get_info(self):
        info = f"{self.ism} {self.familya}, "
        info += f"Passport: {self.passport}, {self.t_yil} yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        info = yil - self.t_yil
        full_info = f"Siz {info} yoshdasiz"
        return full_info
    
shaxs1 = Shaxs("Sherzod", "Yoqubov", "AD8669657", 1997)
# print(shaxs1.get_info())
# print(shaxs1.get_age(2024))



class Talaba(Shaxs):
    """Talaba classi Shaxs classidan vorislik xususiyatlaridan foydalanmoqda"""
    def __init__(self, ism, familya, passport, t_yil, id_raqam, manzil):
        super().__init__(ism, familya, passport, t_yil)
        self.id_raqam = id_raqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
    def get_id(self):
        """Talabaning id raqami"""
        return self.id_raqam
    
    def get_bosqich(self):
        """Talabaning bosqichi"""
        return self.bosqich
    
    def set_bosqich(self):
        """Talabaning bosqichini o'zgartirish"""
        self.bosqich += 1
        
    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            self.fanlar.append(fan)
        else:
            return f"{fan} rejamizga kiritilmagan"
        
    def get_fanlar(self):
        return [fan.get_fan() for fan in self.fanlar]
    
    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"{fan} fani o'chirish uchun topilmadi"
    
# print(talaba1.get_id())

# print(talaba1.get_info())

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        info = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        info += f"{self.kocha} ko'chasi, {self.uy} uyda yashaydi."
        return info

class Fan:
    def __init__(self, name):
        self.name = name
    
    def get_fan(self):
        return self.name
    
    
    
# talaba1_manzil = Manzil("83", "Jayhun", "Norin", "Namangan")
# talaba2 = Talaba("Ali", "Valiyev", "AB1234567", 2000, talaba1_manzil)
talaba3_manzil = Manzil("15", "ALJ", "Uychi", "Buxoro")
talaba3 = Talaba("Xon", "jons", "ac4568", 1998, "fn654789", talaba3_manzil)

# print(talaba2.manzil.get_manzil())

# amaliyot


fan1 = Fan("Fizika")
fan2 = Fan("Ingliz tili")

# print(talaba3.manzil.get_manzil())
talaba3.fanga_yozil(fan1)
talaba3.fanga_yozil(fan2)
# print(fan1.get_fan())

# print(talaba3.get_fanlar())

print(talaba3.remove_fan('tarix'))

print(talaba3.get_fanlar())






































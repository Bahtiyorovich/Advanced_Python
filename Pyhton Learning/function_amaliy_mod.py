# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 23:13:30 2024

@author: Sherzodbek
"""

import auto_info_mod
avto1 = auto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
auto_info_mod.info_print(avto1)

# import modul_nomi komandasi bir martta, dastur boshida yoziladi.

import auto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)

# Modulga qisqa nom berganingizda bunday nomli boshqa o'zgaruvchi yoki funksiya yo'qligiga amin boling.
#  Shunigdek, dastur davomida bu nomni boshqa o'zgaruvchilarga yoki funksiylarga berib yubormang.


# MODUL ICIHDAN MA'LUM FUNKSIYALARNI KO'CHIRIB OLISH
from auto_info_mod import avto_info, info_print

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)



# FUNKSIYALARGA QISQA NOM BERISH
# Huddi avvalgidek, ko'chrib olgan funksiyamizga ham qisqa nom berishimiz mumkin.

from auto_info_mod import avto_info as ainfo, info_print as iprint

avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)


# MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH
# Modul ichidagi barcha funksiyalarni asosiy dasturga ko'chirib olish uchun 
# from modul_nomi import * komandasidan foydalanamiz.

# Diqqat! Bir necha sabablarga ko'ra bu usuldan foydalanish tavsiya qilinmaydi. 
# Katta modullarda yuzlab funksiyalar bo'lishi mumkin, va funksiya nomi sizning dasturingizdagi boshqa
# funksiya yoki o'zgaruvchi bilan bir hil nomga ega bo'lsa, dastur xato ishlashiga olib keladi.

# from auto_info_mod import *

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

# math MODULI
import math

x=400
print(math.sqrt(x))




























































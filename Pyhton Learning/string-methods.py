# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:36:34 2024

@author: Sherzodbek
"""

# name = "Sherzodbek"
# surname = "Yoqubov"

# job = "FullStack Python Web Developer"
# # f{-string usuli} bir nechta o'zgaruvchilarni birlashtirish usuli

# print(f"Salom, men {name} {surname},\n hozirda {job} bo'lib ishlayman ")

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Namangan"

# print(kocha + " ko'chasi " + mahalla + " mahallasi " + tuman + " tumani " + viloyat + " viloyati")

kochangiz = input("Ko'changiz nomi?")
mahallangiz = input("mahallangiz nomi?")
tumaningiz = input("Qaysi tumandansiz?")
viloyatingiz = input("Qaysi viloyatdansiz?")
manzil = f"Siz {kochangiz} ko'chasi,\n{mahallangiz} mahallasi,\n {tumaningiz} tumani,\n {viloyatingiz} viloyatida yashaysiz!"
print(manzil.capitalize())
print(manzil.title())
print(manzil.lower())
print(manzil.upper())


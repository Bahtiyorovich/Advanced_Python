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

# kochangiz = input("Ko'changiz nomi?")
# mahallangiz = input("mahallangiz nomi?")
# tumaningiz = input("Qaysi tumandansiz?")
# viloyatingiz = input("Qaysi viloyatdansiz?")
# manzil = f"Siz {kochangiz} ko'chasi,\n{mahallangiz} mahallasi,\n {tumaningiz} tumani,\n {viloyatingiz} viloyatida yashaysiz!"
# print(manzil.capitalize())
# print(manzil.title())
# print(manzil.lower())
# print(manzil.upper())

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(a)
# matn uzunligini aniqlash uchun len() metodidan foydalaning
# matn ichida biror satr mavjudligini tekshirish uchun in metodidan, yo'qligini tekshirish uchun not in metodidan foydalaning

# txt = "Salom Python"
# print(len(txt))

# print("program" in txt)
# print("program" not in txt)

# Eslatma: Birinchi belgi 0 indeksiga ega.

# matnni kesib olish
b = "Hello, World!"
print(b[2:5])
print(b)


b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])



# Usul strip()boshidan yoki oxiridagi har qanday bo'shliqni olib tashlaydi:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Usul replace()satrni boshqa satr bilan almashtiradi:

a = "Hello, World!"
print(a.replace("H", "J"))


# Usul split()ajratuvchining misollarini topsa, satrni pastki qatorlarga ajratadi:

a = "Hello, World!"
print(a.split(',')) # returns ['Hello', ' World!']















# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:26:41 2024

@author: Sherzodbek
"""
# To'plam yaratilgandan so'ng siz uning elementlarini o'zgartira olmaysiz, 
# lekin elementlarni olib tashlashingiz va yangi elementlar qo'shishingiz mumkin.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# To'plam elementlari tartibsiz, o'zgarmas va takroriy qiymatlarga ruxsat bermaydi.

friends = ["Ali", "Vali"]

[print(f"{x} Bugun choyxonaga borasanmi ? ") for x in friends]

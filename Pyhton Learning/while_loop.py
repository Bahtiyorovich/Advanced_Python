# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:48:27 2024

@author: Sherzodbek
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

# i = 1

# ishora = True
# while ishora:
#     book = input("Siz yoqtirgan kitob: (dasturni to'xtatishni hohlasangiz; 'stop' so'zini kiriting!)>>> ")
#     if book == "stop":
#         ishora = False
#     if book != "stop":
#         print(book)
#     else:
#         print("Dasturdan foydalanganingiz uchun raxmat!")
#     i += 1

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
# 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

# while True:
#     res = input("Kirish chiptasi narxlarini bilib berishim uchun yoshingiz nechida ekanligini bilishim kerak. (Agar dasturni to'xtatishni xoxlasangiz stop yoki quit so'zini kiriting') ")
    
#     if res == "stop" or res == "quit":
#         print("Dasturimizdan foydalanganingiz uchun raxmat!")
#         break
    
#     age = int(res)
#     if age < 7:
#         print("Chipta narxi: 2000 so'm")
#     elif age > 7 and age < 18:
#         print("Chipta narxi: 3000 so'm")
#     elif age > 18 and age < 65:
#         print("Chipta narxi: 10000 so'm")
#     elif age > 65:
#         print("Siz uchun bepul!")
    


# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib,
# yangi ro'yxatga joylang.

# orders = []
# while True:
#     order = input("Nima buyurtma qilasiz, to'xtash uchun {No} deb yozing >>> ")
#     if order.lower() == "no":
#         break
#     orders.append(order)
    

# for item in orders:
#     print(item)



# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# e_market = {}

# while True:
#     order = input("Buyurtmangiz. (To'xtash uchun {No} deb yozing')>>> ")
    
#     if order.lower() == "no":
#         break
#     price = int(input("Buyurma narxi qancha bo'lsin: >>> "))
#     e_market[order] = price

# for order, price in e_market.items():
#     print(f"{order} narxi - {price}")



base = {
        "non":3000,
        "osh":15000,
        "choy":2000
    }

# while True:
#     order = input("Nima buyurasiz: ")
#     if order.lower() == 'no':
#         break
    
#     if order in base.keys():
#         print(f"{order} bor narxi {base[order]}")
#     else: 
#         print("Not found", order)














































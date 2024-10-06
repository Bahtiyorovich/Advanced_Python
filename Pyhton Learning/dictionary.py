# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 07:27:31 2024

@author: Sherzodbek
"""

my_friend = {
        "name" : "Ali",
        "age" : "28",
        "job" : "Php programmer",
        "Location" : "Namangan"
    }

# print(f"My friend: {my_friend['name']}, yoshi {my_friend['age']}, kasbi {my_friend['job']}, yashash joyi {my_friend['Location']}")

my_food = {
   "women" : {
         "salat" : "Karam salat",
         "taom" : "brizol",
         "ichimlik" : "anor Sharbat"
     }
}
    
# print(my_food["women"])

# print(f"Ayolimning kunlik parhez taomlari: {my_food["women"]["salat"]} ni ko'p istemol qiladi")

python_dictionary = {
        "python" : "python dasturlash tili",
        "variable" : "o'zgaruvchi",
        "list" : "ro'yxat",
        "loop" : "takrorlanish",
        "while" : "toki",
        "elif" : "aks-xolda agar",
        "str" : "satr, matn",
        "integer" : "Butun son",
        "float" : "Suzuvchi nuqta"
    }


# for i in range(len(python_dictionary)):
#     key = input("Search word >>> ")
#     # res = python_dictionary.get(key, "Natija topilmadi")
#     # print(res)
#     if key not in python_dictionary:
#         print("Not found")
#     else:
#         print(python_dictionary[key])


#  .items() - metodi: Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

# print(python_dictionary.items())


# [print(f"{key} -- {value}") for key, value in python_dictionary.items()]


# [print(key) for key in python_dictionary.keys()]

# .sorted() - Pythonda lug'at elementlari siz (foydalanuvchi) kiritgan tartibda saqlanadi. 
# Agar lug'at elementlarini alifbo bo'yicha chiqarish talab qilinsa, sorted() funktsiyasidan foydalanamiz.


# [print(item.title()) for item in sorted(python_dictionary)]

# .values() METODI
# Agar lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.
    
# print(python_dictionary.values())

#  set() - tarkibida bir xil elementlar mavjud bo'lmagan to'plamni taqdim etadi.
# [print(set_element) for set_element in set(python_dictionary.values())]


# Amaliyot
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

# [print(el) for el in sorted(python_dictionary.keys())]
# [print(el) for el in sorted(python_dictionary.values())]

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
#  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

countries = {
        "Uzb":"Toshkent",
        "Rus":"Moscow",
        "Tur":"Istanbul",
        "USA": "Washington",
        "China":"Pekin",
        "Korea":"Seul",
        "Japan":"Tokyo",
        "Hind":"Dehli",
    }


# for poytaxt in countries:
#     item = input("Qaysi davlatning pytaxtini bilmoqchisiz: ")
#     res = countries.get(item.title(), "Not found")
#     print(res)


# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        "Non":3000,
        "Salat":5000,
        "Choy":2000,
        "Osh":15000,
        "Sho'rva":20000,
        "Qozonkabob":20000,
        "shashlik to'rg'amchi":14000,
        "shashlik qiyma":12000
    }
buyurtmalar = []

# for i in range(3):
#     buyurtmalar.append(input(f"{i + 1} - buyurtmangiz: ").title())
    
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"{taom.title()} {menu[taom]} - so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom} yo'q edi")


#  Nesting:
    
adiblar = [
        { 
            "ism": "Anvar Nazrullayev",
            "asarlari": ["Python asoslari", "Mohirder online ta'lim platformasi"]
         },
        { 
            "ism": "Elon Mask",
             "asarlari":["SpaceX", "Tesla", "Solor City"]
         },
        { 
            "ism": "Sherzod Yoqubov",
            "asarlari": ["e-commers", "blog", "Telegram bot"]    
        },
    ]


# for adib in adiblar: 
#     print(f"{adib['ism']}ning yaratgan asarlari: ")
#     print(", ".join(adib['asarlari'])) 
    


# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.
# Natijani konsolga chiqaring.

sevimli_kinolar = {}

# for i in range(3):
#     ism = input("Do'stingiz ismi: ")
#     kinolar = []
    
#     for k in range(3):
#         kino = input("Qaysi kinoni yoqtirib ko'rgansiz: ")
#         kinolar.append(kino)

#     sevimli_kinolar[ism] = kinolar


# for ism, kinolar in sevimli_kinolar.items():
#     print(f"{ism}ning sevimli kinolari: {", ".join(kinolar)}")


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

country = {
        "Uzb": {
                "millat":"uzbek",
                "aholi_soni":"38 mln",
                "maydoni":"449 km/kv",
                "tili":"Uzbek tili"
            },
        "USA": {
                "millat":"aralash",
                "aholi_soni":"238 mln",
                "maydoni":"1449 km/kv",
                "tili":"ingliz tili"
            }
    }

# for key, values in country.items():
#     print(f"{key}:{values['millat']} ", end='')


# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa,
 # "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

# for values in country.values():
#     req = input("Qaysi davlat haqida ma'lumot kerak: ")
#     if req == "raxmat":
#         break
#     else :
#         print(f"{req}: \nMillati: {values['millat']}, \nAholi soni: {values['aholi_soni']}")
    
    



















































































































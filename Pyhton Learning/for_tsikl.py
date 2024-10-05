# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:55:28 2024

@author: Sherzodbek
"""

persons = []
print("Siz tanigan muhim shaxslar ismini ayting")

for x in range(3):
    persons.append(input(f"{x + 1} - shaxs ismi kiriting: "))
for i in persons:
    print(f"{i} sizni kechki bazimda oilangiz bilan birgalikda kelishingizni kutamiz!")
print(f"Kod {len(persons)}  marta takrorlandi")
print(persons)

toq_sonlar = []

[toq_sonlar.append(x) for x in range(10, 100) if x % 2 != 0]

print(toq_sonlar)

sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)


movies = []
print("3 ta Sevimli kinolaringiz nomini kiriting! ")

[movies.append(input(f"{n + 1} - kino nomini ayting: ")) for n in range(3)]
[print(x) for x in movies]

meeting_persons = []
x = int(input("Bugun nechta odam bilan suhbatlashdingiz: "))
[meeting_persons.append(input(f"{n + 1} - kim edi: ")) for n in range(x)]
[print(a) for a in meeting_persons]































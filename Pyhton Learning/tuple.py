# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:05:34 2024

@author: S"herzodbe"
"""
"""
Python to'plamlari (massivlar)
Python dasturlash tilida to'rtta turdagi ma'lumotlar to'plami mavjud:

Ro'yxat - bu tartiblangan va o'zgaruvchan to'plam. Takroriy a'zolarga ruxsat beradi.
Tuple - bu tartiblangan va o'zgarmas to'plam. Takroriy a'zolarga ruxsat beradi.
Toʻplam tartibsiz, oʻzgarmas* va indekslanmagan toʻplamdir. Takroriy a'zolar yo'q.
Lug'at tartibli** va o'zgaruvchan to'plamdir. Takroriy a'zolar yo'q.

"""
# Bitta element qatori, vergulni eslab qoling:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple turli xil ma'lumotlarni o'z ichiga olishi mumkin:
tuple1 = ("abc", 34, True, 40, "male")

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)



# Tuple() usulidan foydalanib, kortej yaratish:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Tupleni ro'yxatga aylantiring, "apelsin" qo'shing va uni yana kortejga aylantiring:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# "Apelsin" qiymatiga ega yangi kortej yarating va ushbu kortejni qo'shing:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

# print(thistuple)


# Eslatma: Tupledagi elementlarni olib tashlay olmaysiz.


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)



# amaliyot

countries = ("Uzb", "En", "Ru", "Kz", "Tur")

print(type(countries))


print(len(countries))

sortList = list(countries) 

print(sorted(sortList))
print(sorted(sortList, reverse = True))

# print(sortList.reverse())

n = list(range(120, 1200))
z = []
# print(n)
[z.append(x) for x in n if x % 2 == 0]

k = sum(z)

print(k)

h = min(z)
j = max(z)

print(j - h)

print(len(z))


print(z[:20])
print(z[-20:])
print(z[530:550])





























































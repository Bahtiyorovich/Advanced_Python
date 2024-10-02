# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:10:32 2024

@author: Sherzodbek
"""

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

"""
Ro'yxat elementlari tartiblangan, o'zgartirilishi mumkin va takroriy qiymatlarga ruxsat beriladi.

Ro'yxat elementlari indekslanadi, birinchi element indeksga ega [0], ikkinchi element indeksga ega [1]va hokazo.
Ro'yxatda nechta element borligini aniqlash uchun len()funktsiyadan foydalaning:
    
    Python to'plamlari (massivlar)
Python dasturlash tilida to'rtta turdagi ma'lumotlar to'plami mavjud:

Ro'yxat - bu tartiblangan va o'zgaruvchan to'plam. Takroriy a'zolarga ruxsat beradi.
Tuple - bu tartiblangan va o'zgarmas to'plam. Takroriy a'zolarga ruxsat beradi.
set - tartibsiz, oʻzgarmas* va indekslanmagan toʻplamdir. Takroriy a'zolar yo'q.
Lug'at tartibli** va o'zgaruvchan to'plamdir. Takroriy a'zolar yo'q.


Salbiy indekslash oxiridan boshlanadi degan ma'noni anglatadi

-1oxirgi elementga ishora qiladi, -2ikkinchi oxirgi elementga ishora qiladi va hokazo.
"""

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list3[-1])


# Satrlar, butun sonlar va mantiqiy qiymatlardan iborat ro'yxat:
list1 = ["abc", 34, True, 40, "male"]

print(type(list1))

# list()Ro'yxatni tuzish uchun konstruktordan foydalanish :

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Siz diapazonni qaerdan boshlash va qayerdan tugatishni belgilash orqali bir qator indekslarni belgilashingiz mumkin.

# Diapazonni belgilashda qaytariladigan qiymat belgilangan elementlar bilan yangi ro'yxat bo'ladi.
print(list2[2:5])
print(list2[:4])
print(list2[1:])

# Ushbu misol "to'q sariq" (-4) dan "mango" (-1) ni o'z ichiga olmaydi:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Ro'yxatda "olma" mavjudligini tekshiring:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# elementni o'zgartiring

list1[1] = "List-change"
print(list1)

list2[2:5] = ["Js", "Py", "Django"]
print(list2)

list3[1:2] = [10, 15, 20]
print(list3)

# Mavjud qiymatlarni almashtirmasdan yangi ro'yxat elementini kiritish uchun biz insert()usuldan foydalanishimiz mumkin.

# Usul insert()belgilangan indeksga element kiritadi:

# Misol
# Uchinchi element sifatida "tarvuz" ni qo'ying:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Roʻyxat oxiriga element qoʻshish uchun append() usulidan foydalaning:
    
list1.append("Hello")
print(list1)

# Boshqa ro'yxatdagi elementlarni joriy ro'yxatga qo'shish uchun extend()usuldan foydalaning.

list1.extend(list2)
print(list1)
# Elementlar ro'yxatning oxiriga qo'shiladi .

# Usul remove()belgilangan elementni olib tashlaydi.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# "Banan" ning birinchi ko'rinishini olib tashlang:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Usul pop()belgilangan indeksni olib tashlaydi.

# Misol
# Ikkinchi elementni olib tashlang:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# Agar siz indeksni ko'rsatmasangiz, pop()usul oxirgi elementni olib tashlaydi.

# Misol
# Oxirgi elementni olib tashlang:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# Kalit del so'z belgilangan indeksni ham olib tashlaydi:

# Misol
# Birinchi elementni olib tashlang:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Kalit del so'z ham ro'yxatni butunlay o'chirib tashlashi mumkin.

# Misol
# To'liq ro'yxatni o'chirish:

thislist = ["apple", "banana", "cherry"]
del thislist

# Roʻyxatni tozalang
# Usul clear()ro'yxatni bo'shatadi.

# Ro'yxat hali ham saqlanib qolmoqda, ammo uning mazmuni yo'q.

# Misol
# Ro'yxat tarkibini tozalang:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# or
[print(x) for x in thislist]

# Indeks raqamlari bo'ylab aylanish
# Siz shuningdek, indeks raqamiga murojaat qilib, ro'yxat elementlarini aylanib chiqishingiz mumkin.

# Tegishli takrorlanuvchini yaratish uchun range()va funksiyalaridan foydalaning .len()

# Misol
# Barcha elementlarni indeks raqamiga qarab chop eting:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# Yuqoridagi misolda yaratilgan iterativ hisoblanadi [0, 1, 2].


# whileBarcha indeks raqamlarini o'tish uchun tsikldan foydalanib, barcha elementlarni chop eting

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1



# for Ro'yxatdagi barcha elementlarni chop etadigan qisqa qo'l tsikli:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# for va if yordamida yangi ro'yxat yaratish
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("result: ", newlist)


# bir qatorda yozish

# newlist = [expression for item in iterable if condition == True]

# Qaytish qiymati yangi ro'yxat bo'lib, eski ro'yxatni o'zgarishsiz qoldiradi.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Faqat "olma" bo'lmagan narsalarni qabul qiling:

newlist = [x for x in fruits if x != "apple"]

newlistNumber = [x for x in range(10)]

newListNumber = [x for x in range(10) if x < 5]

print(newListNumber)

newlist = [x if x != "banana" else "orange" for x in fruits]

# barcha qiymatlarni "hello" ga almashtirish
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)



fruits.sort()
print(fruits)

# o'sish tartibida tartiblash
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# kamayish tartibida tartiblash
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# katta kichik harflarga sezmaydigan qilib tartiblash
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Ro'yxat elementlarining tartibini o'zgartiring:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy() usulidan foydalaning
# copy()Roʻyxatni nusxalash uchun oʻrnatilgan Roʻyxat usulidan foydalanishingiz mumkin .

# MisolO'zingizning Python serveringizni oling
# Usul bilan ro'yxatning nusxasini yarating copy():

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Usul bilan ro'yxatning nusxasini yarating list():

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Dilim operatoridan foydalaning
# Roʻyxatning nusxasini :(boʻlim) operatori yordamida ham yaratishingiz mumkin.

# Misol
# Operator bilan ro'yxat nusxasini yarating ::

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# Usul count()belgilangan qiymatga ega elementlar sonini qaytaradi.

# Sintaksis
# list.count(value)
# Ro'yxatda 9 qiymati necha marta paydo bo'lishini qaytaring:

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)


# Usul index()belgilangan qiymatning birinchi paydo bo'lishidagi pozitsiyani qaytaradi.

# Sintaksis
# list.index(elmnt)
# "Gilos" qiymatining pozitsiyasi qanday:

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")






















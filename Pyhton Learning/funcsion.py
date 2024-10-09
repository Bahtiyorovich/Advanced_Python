# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:12:22 2024

@author: Sherzodbek
"""

def hello():
    """Bu funksiya qiymat qabul qilmaydi, siz uni chaqirasiz holos"""
    print("Hello World")
# hello()



def hisobla(a, b):
    """ Bu funksiya ikkita parametr qabul qiladi: a va b va ularni qo'shadi """
    print(a + b)

# hisobla(5, 10)

# funksiyani docstring ni ko'rsatish kodi
# print(hisobla.__doc__)


"""Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak.
Aks holda xatolik yuzaga keladi."""

def my_age(name, age = 28):
    """ Bu funksiya userning ismi va yoshi 
    parametrlarini qabul qiladi, yoshni aniqlashda standart qiymatdan doydalanadi"""

    print(f"Salom {name} "
          f"siz {age} ysohdasiz"
          )

# my_age('sherzod')

# Amaliyot

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def birth_year(name, age):
    """ userning tug'ilgan yilini hisoblaymiz, userdan name va age parametrlariga argument qabul qilamiz """

    print(f"Salom {name} siz {2024 - age} yilda tug'ilgansiz")


# birth_year("Sherzod", 27)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kv_kub(a, b = 2, c = 3):
    print(f"{a} ning kvadrati {a**b}, kubi {a**3}")

# kv_kub(5)

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def number(a):
    if not a % 2:
        print("Son juft")
    else:
        print("Son toq")
    
# n = int(input("Son kiriting >>> "))
# number(n)


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
#  Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def min_max(a, b):
    if a > b:
        print(f"{a} > {b}")
    elif a < b:
        print(f"{a} < {b}")
    else:
        print(f"{a} = {b}")

# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
# min_max(a, b)


# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
# bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def qoldiq(a):
    numbers = []
    for i in range(2,11):
        if not a % i:
            numbers.append(i)
    print(f"{a} soni, \n{numbers} shu sonlarga qoldiqsiz bo'linadi")

# a = int(input("Son kiriting: "))
# qoldiq(a)


# Amaliyot
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def userInfo(name, surname, year, region, email = None, tel_number = None):
    user = {
        "Ism": name,
        "Familiya": surname,
        "Tug'ilgan yili": year,
        "Tug'ilgan joyi": region,
        }
    
    if email:
        user["email"] = email
    if tel_number:
        user["tel_number"] = tel_number
    return user

# name = input("Name: ")
# surname = input("Surname: ")
# year = int(input("Birth Year: "))
# region = input("Where are you from: ")
# email = input("email")
# tel = input("Tel number: ")

# print(userInfo(name, surname, year, region, email, tel))
    

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

# users = []
# while True:
#     name = input("Name: ")
#     surname = input("Surname: ")
#     year = int(input("Birth Year: "))
#     region = input("Where are you from: ")
#     email = input("email: ")
#     tel = input("Tel number: ")
#     users.append(userInfo(name, surname, year,region,email,tel))
#     savol = input("Yana kimnidir ro'yxatga kiritasizmi (No/Yes)")
#     if savol.lower() == 'no':
#         break
#     else :
#         continue
# print(users)
    

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def maxNumber(a, b, c):
    numbers = list((a, b, c))
    res = max(numbers)
    return res
    

# print(maxNumber(5, 10, 7))


# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing


def circle(r):
    length = 2 * 3.14 * r
    d = 2 * r
    s = 3.14 * (r ** 2)
    circle = {
        "length":length,
        "diametr": d,
        "yuza" : s
        }
    return circle


# print(circle(2))


# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)


def rangeNumber(a,b):
    tub_sonlar = []

    for son in range(a, b + 1):
        if son > 1:
            for i in range(2, int(son ** 0.5) + 1):
                if not son % i:
                    break
            else:
                tub_sonlar.append(son)
    return tub_sonlar

# print(rangeNumber(10, 30))


# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
# sonlar ro'yxatni qaytaruvchi funksiya yozing. 
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
# ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
# Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...


def fib(count_number):
    fibonachchi = [1, 1]
    
    if count_number <= 2:
        return fibonachchi[:count_number]
    
    for i in range(2, count_number):
        next_item = fibonachchi[-1] + fibonachchi[-2]
        fibonachchi.append(next_item)
        
    return fibonachchi

# print(fib(5))
    
    
    
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini
 # katta harfga o'zgatiruvchi funksiya yozing


def upperText(arr):
    upperStr = []
    
    for item in arr:
        upperStr.append(item.title())
        
    return upperStr

textArr = ["ali", "vali", "js"]
# print(upperText(textArr[:]))
# print(textArr)


# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan 
# va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.


def ball(arr):
    student_score = {}
    
    for student in arr:
        score = int(input(f"{student}ning bahosi nechi: "))
        student_score[student] = score

    return student_score

students = ["Ali", "Vali", "Jasur"]
# print(ball(students[:]))


# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def summa(*sonlar):
    kopaytma = 1
    for i in sonlar:
        kopaytma *= i
    return kopaytma


# print(summa(2,3,4,5,6))


# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.


def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')

# print(talaba)

def car(**car):
    return car

carInfo = car(model = 'Malibu', color = 'Black', price = '$ 30000') 

# print(carInfo)

# import math
uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))



product = lambda x, y : x ** y
# print(product(3, 2))




# map() FUNKSIYASI
# Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir funksiyani
 # qabul qilib, ro'yxat elementlariga qabul qilingan 
 # funksya yordamida ishlov beradi. Tushunarli bo'lish uchun quyidagi 
 # misolni ko'ramiz.

from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)
# Yuqoridagi misolda avval 0 dan 10 gacha sonlar ro'yxatini tuzib oldik, 
# keyin esa map funksiyasiga ro'yxat va sqrt funksiyasini uzatib, 
# ro'yxatdagi barcha sonlarning ildizini hisoblab oldik.

# map() funksiyasi map obyekt qaytargani sababli, qaytgan obyektni ro'yxatga
 # o'tkazib olish uchun list() funksiyasidan foyydalandik.


# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz


kvadratlar = list(map(lambda x:x*x,sonlar))
# print(kvadratlar)

ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# Bu funksiya ham argument sifatida ro'yxat va boshqa funskiyani qabul qilib
#  oladi va berilgan ro'yxat elementlarini berilgan funksiya yordamida saralaydi. 
#  Bunda argument sifatida uzatilgan funksiya
#  mantiqiy qiymat qaytarishi kerak (True yoki False).


import random as r
sonlar = r.sample(range(100), 10)

def juftmi(x):
    """x juft bo'lsa True aks xolda False qaytaruvchi funksiya"""
    return x % 2 == 0

juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)

juftSonlar = list(filter(lambda x:x%2==0, sonlar))

# print(juftSonlar)



# Keling endi filter() funksiyasi yordamida matnlarni saralashga 
# ham misollar ko'raylik.

# Quyidagi dastur mevalar ro'yxatidan b harfiga boshlanuvchi mevalarni ajratib oladi.
#  Bu yerda biz matnlarga tegishli bo'lgan .startswith() metodidan foydalandik. 
#  Bu metod, berilgan matn shu harfdan boshlanadimi yoki yo'q tekshiradi va True 
#  yoki False qiymat qaytaradi.

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)
['banan']

# Quyidagi dastur esa mevalar ro'yxatidan nomi 5 yoki undan kam harfdan 
# iborat mevalarni saralab oladi.

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)
['olma', 'anor', 'anjir', "o'rik", 'qovun', 'banan']

# Topingchi, quyidagi kod qanday vazifani bajaradi?

list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))


















# decorator - funksiyani argument sifatida olib,
# uning o’zgartirilgan nusxasini qaytaruvchi funksiya.
# Decorator bevosita funksiyani o’zgartirmasdan,
# undan oldin va keyin ishlaydigan kodlar qo’shish imkonini beradi.

# Decorator — bu boshqa funksiyani (yoki metodni) argument
# sifatida qabul qiladigan va uni o'zgartirilgan yoki
# kengaytirilgan ko'rinishda qaytaradigan funksiya.

# Python'da decoratorlar — bu funksiyalar yoki metodlarning funksional
# imkoniyatlarini kengaytirish yoki ularni o'zgartirish uchun
# mo'ljallangan maxsus konstruktsiyalardir.
# Decorator bir funksiya yoki metodni boshqa bir
# funksiya ichiga "o'ralgan" holatda chaqirish orqali
# yangi xatti-harakatlarni qo'shishga yordam beradi.
# Decoratorlardan ko'pincha kodni takrorlanmasligi uchun yoki
# muayyan xatti-harakatlarni bir necha joyda ishlatish uchun foydalaniladi.
#
# Decorator'ning Asosiy G'oyasi
# Decorator — bu boshqa funksiyani (yoki metodni)
# argument sifatida qabul qiladigan va uni o'zgartirilgan yoki
# kengaytirilgan ko'rinishda qaytaradigan funksiya.
#
# Decorator Yaratish Va Ishlatish
# Decorator yaratish va ishlatish uchun quyidagi uchta qadam mavjud:
#
# Decorator funksiyani yaratish: Dekorator bir funksiya yoki klass bo‘lib,
# boshqa funksiya ustida bajariladigan qo‘shimcha vazifalarni bajaradi.
# Dekoratorda ichki funksiya yaratish: Dekoratorda ichki funksiya ishlatiladi,
# u orqali asl funksiya ichiga yangi imkoniyatlar qo'shiladi.
# @ sintaksisi orqali dekoratorni ishlatish: Decorator ni @ operatori yordamida
# funksiya tepasida yozib ishlatish mumkin.
# Oddiy Misol: Logger Decorator
# Keling, bir dekoratorni qanday yaratish va ishlatishni logger (loglar chiqaradigan)
# misoli orqali tushuntirib chiqamiz.
#
# 1-qadam: Decorator funksiyani yaratish
# python
# Copy code
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments: {args} {kwargs}")
        result = func(*args, **kwargs)  # Asl funksiyani chaqirish
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
# logger — dekorator funksiyasi bo'lib, u boshqa funksiyani (func) qabul qiladi.
# wrapper — ichki funksiya bo'lib, asl funksiya chaqirilganda loglarni chiqaradi va natijani qaytaradi.
# 2-qadam: Funksiyaga @ yordamida dekoratorni qo'llash
# Endi dekoratorni @ operatori yordamida funksiya ustida ishlatamiz.
#
# python
# Copy code
@logger
def add(a, b):
    return a + b
# Bu yerda @logger yordamida add funksiyasi dekoratsiyalanadi,
# ya'ni add chaqirilganda logger ichida yozilgan qo‘shimcha loglar chiqariladi.
#
# 3-qadam: Dekoratsiyalangan funksiyani chaqirish
# python
# Copy code
# result = add(3, 5)
# # Chiqish:
# # Function 'add' was called with arguments: (3, 5) {}
# # Function 'add' returned: 8
# add(3, 5) chaqirilganda quyidagi amallar bajariladi:
#
# logger dekoratori add funksiyasini wrapper funksiyasi bilan o'rab oladi.
# wrapper funksiyasi add ni chaqirishdan oldin va keyin loglarni chiqaradi.
# Decorator'ning afzalliklari
# Kodni qayta ishlatish: Har bir funksiyada loglarni qo‘lda yozish o‘rniga,
# dekorator orqali barcha funksiyalarda bir xil log xatti-harakatini qo‘shish mumkin.
# Kodni soddalashtirish: Asosiy funksiyaning o‘zida keraksiz qatorlarni kamaytirish,
# faqat asosiy vazifaga e'tibor qaratish imkonini beradi.
# Moslashuvchanlik: *args va **kwargs orqali dekoratorni har qanday turdagi funksiyaga qo‘llash mumkin,
# shu bilan dekoratorlar umumiy va qayta ishlatiladigan bo‘ladi.
# Ko'p Foydalaniladigan Dekoratorlar
# @staticmethod va @classmethod: Klass metodlari uchun foydalaniladi.
# @property: Klass ichidagi metodlarni xuddi property (xususiyat) sifatida ishlatishga imkon beradi.
# Keshlash: Natijalarni keshlash (saqlash) orqali funksiyani tezlashtirish uchun ishlatiladi.
# Xulosa
# Decorator'lar Python dasturiy ta'minotida qayta foydalanish,
# xatti-harakatlarni boshqarish va kodni samarali yozishda muhim o'rin tutadi.
# Decorator bilan ishlashda @ yordamida funksiya xatti-harakatini kengaytirish mumkin,
# bu esa kattaroq dasturlarni boshqarishni soddalashtiradi va funktsiyalar orasidagi
# umumiy xatti-harakatlarni boshqarish imkonini beradi.
#












































































































































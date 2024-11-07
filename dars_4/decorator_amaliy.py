# 1. Fuksiya qaytaradigan stringni katta harflarga o'tkazib beradigan dekorator yarating.
from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_decorator
def input_string(text):
    return text

# string = input("Ixtiyoriy so'z kiriting, ijtimoiy odob qoidalariga rioya qiling: ")
# print(input_string(string))
"""
Tahlil
Dekoratorning tuzilishi:

uppercase_decorator funksiyasi dekorator sifatida ishlaydi va ichida wrapper funksiyasini yaratadi.
@wraps(func) ishlatish orqali asl funksiyaning __name__, __doc__ kabi metadata'si yo‘qolmaydi. 
Bu yaxshi amaliyot bo‘lib, dekoratsiyalangan funksiya haqidagi ma’lumotlar 
(masalan, uning nomi va dokumentatsiya stringi) saqlab qoladi.
Argumentlar bilan ishlash:

wrapper funksiyasi *args va **kwargs orqali funksiyaga kiritilgan har qanday argumentlar va 
kalit so‘z argumentlarini qabul qiladi. Bu dekoratorni ko‘p turdagi funksiyalar uchun mos va
keng qo‘llanadigan yechim qiladi.
Stringni tekshirish:

isinstance(result, str) sharti orqali dekorator faqat string natijalarni katta harflarga o‘tkazadi. 
Agar funksiya boshqa turdagi natijalarni qaytarsa (masalan, integer yoki ro'yxat), 
dekorator ularni o‘zgartirmasdan qaytaradi.
Natijani qaytarish:

Agar natija string bo‘lsa, result.upper() orqali katta harflarga o‘tkazilib qaytariladi.
Xulosa
Ushbu dekorator optimal va keng qo‘llaniladi, chunki:

Flexibilite: U ko‘p turdagi funksiyalar bilan ishlashga mos.
Keng foydalanish: @wraps dekoratorini qo‘llash orqali funksiyaning asli haqidagi ma’lumotlar saqlanadi.
Optimal tekshirish: Faqat kerakli string qiymatlar katta harfga o‘tkaziladi va 
boshqa qiymatlarga ta’sir qilinmaydi.
Bu dekorator string natijalarni katta harflarga o‘tkazish uchun sodda va samarali usul hisoblanadi.
"""

# 2. Fuksiya qaytaradigan stringni teskaraisiga aylantirib(reverse)  beradigan dekorator yarating.
def reverse_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1] # textni teskarisiga o'girishning eng keng tarqalgan va optimal usuli
        return result
    return wrapper

@reverse_decorator
def text(txt):
    return txt

# str_value = input("Ixtiyoriy so'z kiriting: ")
# print(text(str_value))

# 3. Funksiya ishlashi uchun qancha vaqt ketganini hisoblab beradigan dekorator yozing
import time
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        ellapsed_time = end_time - start_time
        print(f"Funksiya {func.__name__} {ellapsed_time:.6f} soniya bajarildi")
        return result
    return wrapper

@timer_decorator
def increment_number(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr

# print(increment_number(1000))
"""
Tahlil
Dekorator tuzilishi:

timer_decorator funksiyasi dekorator sifatida ishlaydi va wrapper ichki funksiyasini yaratadi.
@wraps(func) dekoratori asl funksiyaning metadatalarini (nomi, hujjatlari) saqlab qoladi, 
bu esa dekoratsiyalangan funksiyani debugging qilish yoki loglarda ko‘rib chiqishni osonlashtiradi.
Vaqtni hisoblash:

start_time va end_time orqali funksiya boshlanishi va tugash vaqtlari time.time() yordamida yozib olinadi.
elapsed_time o‘zgaruvchisi orqali farq hisoblanadi, bu bizga funksiya qancha vaqt davomida 
ishlaganini soniya ko‘rinishida beradi.
Natijani print orqali ko‘rsatamiz, bunda funksiya nomi va vaqtni aniqlik bilan (.6f formatida) chiqaramiz.
Qo‘llash:

Ushbu dekoratorni turli funksiyalar uchun ishlatish mumkin va ular ishlash vaqtini ko‘rsatib beradi.
"""
# 4. Funksiya necha marta chaqirilganini sanovchi dekorator yozing

def call_counter_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Funksiya {func.__name__} {wrapper.call_count} chi marta chaqirildi")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_counter_decorator
def pow_number(a, b):
    return f"result: {a ** b}"

# print(pow_number(2, 3))
# print(pow_number(3, 3))
# print(pow_number(4, 3))
# print(pow_number(5, 3))


"""
Tahlil
Dekorator tuzilishi:

call_counter dekoratori wrapper funksiyasini yaratadi va har safar funksiya chaqirilganda, 
wrapper.call_count qiymatini birga oshirib boradi.
@wraps(func) dekoratori asl funksiyaning metadatalarini saqlab qoladi, bu yaxshi amaliyot hisoblanadi.
O‘zgaruvchi tashqarida saqlanishi:

wrapper.call_count dekorator ichidagi hisoblagich sifatida ishlaydi. 
Dastlab uni 0 ga teng qilib o‘rnatamiz va har bir chaqiriqda birga oshirib boramiz.
Chop etish:

print yordamida har bir chaqiriq sonini ko‘rsatib boramiz, bu esa chaqiruvlarni kuzatish imkonini beradi.
Xulosa
Bu dekorator funksiyaning har bir chaqirig‘ini hisoblab boradi va 
wrapper.call_count orqali chaqirilish sonini ko‘rsatadi. Bu oddiy, 
lekin foydali dekorator bo‘lib, funksiyalarning ishlatilish chastotasini kuzatishda yordam beradi.

"""












































# Funksiya kod bloki bo'lib u faqat chaqirilganda ishlaydi,
# funksiya def kalit so'zi bilan yaratiladi
# """___""" ga ahamiyat bering bu docstring deyiladi va vazifasi
# funksiya nomini ustiga sichqoncha kelganda funksiya haqida ma'lumot beradi
def hello():
    """ Salomlashuvchi funksiya"""
    print("Hello Python developer")

# funksiyani chaqirish uchun uning nomi yoziladi va qavs qo'yiladi
# hello()

# funksiya yaratilayotganda qavslari ichiga parametr
# deb nomlanuvchi elementlarni qabul qiladi

def full_name(name, lastname):
    print(f"Assalomu alaykum {name + " " + lastname}")

# full_name("Sherzod", "Yoqubov")

# Biz endi pastdagi barcha funksiyalarda return bayotnotidan foydalanim
# bu bayonot funksiya bajargan amallarni javob sifatida qaytaradi

# funksiya parametriga standart qiymat berish: c = 15
def hisobla(a, b, c = 15):
    """ Bu funksiya berilgan parametr ustida hisoblash amaliyotini bajaradi"""
    return (a + b) * (a - b) - c

# print(hisobla(7, 8))
# etibor bering funksiya chaqirilganda c parametriga argument berilmadi
# sababi c = 15 standart qiymat qabul qilgan

# Funksiyada argumentlar tartibi muhim emas,
# ularni kalit=qiymat juftligi sifatida yuborish mumkin

def sum_info(a, b, c):
    return a * b + c

# print(sum_info(c = 7, b = 8, a = 10))

# agar funksiyangiz ko'proq argumentlarni qabul qilishi mumkinligini oldindan bilmasangiz
# parametr oldiga { * } yulduzcha qo'ying
def summa(*args):
    """
       Bu funksiya *args metodi yordamida juda ko'p argumentlarni qabul qiladi va
       barcha argumentlarni list (ro'yxat)ga aylantiradi
       shuning uchun bu qiymatlar ustida takrorlash operatoridan foydalanish
       yoki list ning metodlaridan foydalanish mumkin
    """
    res = 0
    for i in args:
        res += i
    return res

# print(summa(1,2,3,4,5,6,7,8,9))
def print_result(name, *info):
     return f"Salom {name}!, sizning ma'lumotlaringiz {info}"

# print(print_result("Sherzod", ["python", "web_dev"]))
# ko'rib turganingizdek *args ga list, set, tupleni ham o'tkazish mumkin

# Agar kalit so'z argumentlari soni noma'lum bo'lsa,
# parametr nomidan oldin ikkita { ** } qo'shing
def person(**info):
    person_dict = {}
    for key, value in info.items():
        person_dict[key] = value
    return person_dict
# print(person(name = "John Smith", age = "28", job = "Agent", isMarried = True))
# aslida **kvargs berilgan kalit=qiymat argumentlarini lug'atga yi'gadi,
# shuning uchun bemalol lug'at metodlaridan foydalanish mumkin


# Rekursiya
# Rekursiv funksiyalar — bu o‘zini o‘zi chaqiradigan funksiyalar.
# Ya’ni, funksiya bajarilishi davomida yana o‘sha funksiyani qayta chaqiradi.
# Bu usul, odatda,
# biror katta masalani kichik masalalarga bo‘lish kerak bo‘lganda foydali bo‘ladi.

# rekursiv funksiyaning ikki asosiy sharti mavjud
# 1- to'xtash sharti; agar to'xtash sharti bo'lmasa funksiya abadiy siklga tushib qoladi
# 2- funksiya asosiy kod qismi, ammo masala qiyinlashmasligi kerak

# Misol: Fibonachchi Sonlarini Topish
# Fibonachchi ketma-ketligi: 0, 1, 1, 2, 3, 5, 8, 13...
# Har bir son undan oldingi ikkita sondan yig‘indisi sifatida hosil bo‘ladi.

def arr(n):
    list_fib = []

    def fib_num(x):
        if x <= 1:
            return x
        else:
            return fib_num(x - 1) + fib_num(x - 2)

    for i in range(n + 1):
        list_fib.append(fib_num(i))

    return list_fib
# print(arr(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# print(factorial(5))

# Qachon Rekursiv Funksiyadan Foydalanish Tavsiya Etiladi?

# Rekursiv funksiyalar quyidagi vaziyatlarda juda qulay:
# Murakkab tuzilmalarda ishlash: Ma'lumotlar daraxti yoki grafik strukturalarda
# ma'lumotlarni izlash yoki o'tish kerak bo'lganda.
# Takrorlanuvchi matematik masalalar: Masalan, Fibonachchi ketma-ketligini yoki
# faktorialni hisoblash.
# Kichik masalalarga ajratish mumkin bo'lgan katta masalalar:
# Masalan, merge sort yoki quick sort kabi ajratish va yig‘ish usullari.

# Qachon Rekursiv Funksiyadan Foydalanish Tavsiya Etilmaydi?

# Chuqur rekursiya talab qilinadigan vaziyatlarda:
# Ko‘p darajadagi rekursiv chaqiriqlar stack overflow (xotira tugashi)
# keltirib chiqarishi mumkin.
# Takrorlanadigan hisobotlar va ishlov berishlarda:
# Ko‘p marta hisoblanadigan qiymatlarni keshlash yoki
# iteratsiya yordamida ishlash optimal bo‘lishi mumkin.










































































































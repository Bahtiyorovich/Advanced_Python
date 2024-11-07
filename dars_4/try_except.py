"""
Python dasturlash tilida xatolarni (error) boshqarish muhim mavzularidan biridir,
chunki bu dasturda yuzaga keladigan kutilmagan holatlar va
noto‘g‘ri ishlashni oldini olishga yordam beradi.
agar xatolik vaqtida nazorat qilinmasa dastur to'xtab qoladi

Xato Turlari
Python’da xatolar uchta asosiy turga bo'linadi:

1. Sintaksis xatolar (Syntax Errors): Kodning noto‘g‘ri yozilishi natijasida yuzaga keladi.
   Masalan, qavslar, nuqta-vergul kabilarning to‘g‘ri joylashmaganligi.

2. Mantiqiy xatolar (Logical Errors): Kod sintaksisi to‘g‘ri bo‘lsa ham, kutilgan natija olinmasa.
   Bu xatolarni dastur ishlayotganda sezish qiyin.

3. Istisnolar (Exceptions): Kodni bajarish davomida sodir bo'ladigan xatolar,
   masalan, nolga bo‘lish, faylni ochishda xato, kiritilgan ma'lumot noto‘g‘ri bo'lsa, va hokazo.

    try-except Bloki orqali istisnolarni boshqarish mumkin

    Python’da istisnolar bilan ishlash uchun try-except blokidan foydalaniladi. Bu blokda xatolarni aniqlab,
    ular yuzaga kelganda dastur to‘xtab qolmasdan davom etishi mumkin.

"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi")


# Bir nechta xatolarni boshqarish bir vaqtda boshqarish

try:
    number = int(input("Son kiriting>>> "))
    result = 10 / number
except ValueError:
    print("Faqat son kiritishingiz kerak!")
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi")

# Bu usul yordamida har bir xato turini o‘ziga xos xabar bilan boshqarish mumkin.

# else bloki bilan xatosiz holatni boshqarish

# Agar try blokida xato yuz bermasa, else bloki bajariladi.
# Bu usul yordamida xatosiz bajarilgan holatlarda qanday
# ishlarni bajarish kerakligini belgilab olish mumkin.

try:
    number = int(input("Son kiriting>>>"))
    result = 10 / number
except ValueError:
    print("Faqat son kiriting")
except ZeroDivisionError:
    print("Nolga bo'lish mumkinmas")
else:
    print(f"Natija: {result}")

# Bu usulda agar xato bo'lmasa, else bloki ishlaydi va natija chop etiladi.
# Eng yaxshi amaliyotga kiradi bu usul, sababi try bloki faqat funksiya vazifasi bilan ishlash kerak,
# natijani qaytarish yoki xatolar bilan ishlash uning vazifasiga kirmaydi


# finally bloki har qanday holatda, ya'ni xato yuzaga keladimi yoki yo‘qmi, albatta bajariladi.
# U asosan fayl yoki tarmoq resurslarini yopishda ishlatiladi.


# Python’da raise operatori orqali o‘zimizga kerakli xatolarni yaratishimiz mumkin.
# Masalan, agar ma'lum shart bajarilmasa, xatoni qo'lda chiqarish.

def check_age(age):
    if age < 18:
        raise ValueError("Yosh 18 dan kichik bo'lishi mumkin emas!")
    else:
        print("Yosh mos!")


# check_age(15)

# Xatolarni Qayta Ko'rib Chiqish va Loglash
# Katta loyihalarda barcha xatolarni log (ya'ni yozib borish) qilish kerak bo'ladi.
# logging moduli yordamida xatolarni faylga yozish va
# dastur ishlab chiqish jarayonida ularni tahlil qilish qulaydir.

import logging

logging.basicConfig(filename='xatolar.log', level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Xato: %s", e)



# Xatolarni Boshqarish Bo‘yicha Optimal Usullar
# optimal - eng yaxshi va tavsiya etiladigan usul
#
# 1. Xatolarni oldindan rejalashtirish: Dastur kodini yozayotganda qaysi joyda
# xato kelib chiqishi mumkinligini aniqlab,ularga try-except qo'shish.
#  Misol:
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Kiritilgan fayl mavjud emas. Iltimos, fayl nomini tekshiring.")
    except PermissionError:
        print("Faylni o'qishga ruxsat yo'q.")

# Foydalanish
file_content = read_file("try_catch.txt")
print(file_content)

# Tahlil qilamiz: Bu kodda try-except blokini read_file funksiyasiga joylashtirdik,
# chunki fayl yo‘qligi yoki ruxsat yo‘qligi kabi ehtimoliy xatolarni
# oldindan hisobga olganmiz. Shunday qilib, dasturda ushbu xatolar tufayli
# to‘xtab qolishining oldini oldik.


# 2. Xatolarni to‘g‘ri joylash: Faqat kerakli joylarda try-except ishlatish,
# barcha kodni try ga olish yomon odat.

#Faqat kerakli joylarda try-except bloklarini ishlatish muhim. Aks holda,
# barcha kodni try ichiga olish, xatolarni aniqlash va
# dastur logikasini kuzatishda qiyinchilik tug‘diradi. Faqatgina ehtimoliy
# xato keltirib chiqarishi mumkin bo‘lgan qismni ajratib olish yaxshidir.

def divide_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Faqat son kiritishingiz kerak.")
        return
    try:
        result = a / b
    except ZeroDivisionError:
        print("Nolga bo'lish mumkin emas.")
        return
    return result

# print(divide_numbers(10, 0))  # Xato, nolga bo'lish mumkin emas
# print(divide_numbers(10, "a"))  # Xato, son emas

""" Tahlil qilamiz: Bu yerda faqat bo‘lish operatsiyasi uchun try-except ishlatildi,
boshqa tekshirishlar alohida joylashtirildi.
ZeroDivisionErrorni try-except yordamida boshqarib,
son tekshiruvini esa try bloki tashqarisida qildik.
Bu kodni o'qishni osonlashtiradi va faqat kerakli joylarda
xato boshqarish imkonini beradi."""

# 3. Ma’lumotlarni to‘g‘ri tekshirish: Dasturga kiradigan ma'lumotlarni tekshirib,
# noto‘g‘ri ma'lumot kiritilishidan oldin oldini olish.

"""
Ma'lumotlarni dasturga kiritilishidan oldin tekshirib, 
noto‘g‘ri kiritilmasligini ta'minlash muhim. Bu dasturni xato va 
buzilishlardan himoya qiladi va 
foydalanuvchi kiritgan ma'lumotlarni xatoliklardan tozalashga yordam beradi.
"""


def get_age_input():
    age = input("Yoshingizni kiriting: ")
    if not age.isdigit():
        print("Faqat ijobiy son kiritishingiz kerak.")
        return None

    age = int(age)
    if age < 0:
        print("Yosh manfiy bo'lishi mumkin emas.")
        return None

    return age


# Foydalanish
age = get_age_input()
if age is not None:
    print(f"Yoshingiz: {age}")
"""
Tahlil qilamiz: get_age_input funksiyasi foydalanuvchi kiritgan ma'lumotni tekshiradi va
 noto‘g‘ri kiritilgan hollarda foydalanuvchiga xatolik haqida ma'lumot beradi. 
 Bu usulda dasturda kiritiladigan ma'lumotlarni try-except orqali tekshirish o‘rniga, 
 kiritilishdan oldin mantiqiy shartlar orqali tekshirishga afzallik berdik. 
 Shunday qilib, xatolar oldini olish mumkin.
"""


# Bu usullar yordamida Python'da xatolar bilan samarali ishlash imkonini beruvchi
# strategiyalarni ishlab chiqish mumkin.
















































































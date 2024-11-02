# For sikli mavzusi bo’yicha vazifalar

# 1. Elektron Pochta Manzillarini Tekshirish:
# Email manzillar ro'yxati berilgan:
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for sikli va string metodlari yordamida har bir email manzilida "@" belgisi
# bor-yo'qligini tekshiring: Agar bo'lmasa, "Noto'g'ri email: email_manzi" deb
# chiqaring.

def check_email(arr):
    """Email tarkibida @ borligini tekshirish"""
    if len(arr) > 0:
        for item in arr:
            if item.find("@") != -1:
                print(f"This {item} email address saved")
            elif item.find("@") == -1:
                print(f"This {item} email address is invalid")

# check_email(pochtalar)


# 2. Parol Kuchini Tekshirish:
# ○ Foydalanuvchilarning parollar ro'yxati berilgan (masalan,
password = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# ○ for sikli va shart operatorlari yordamida har bir parolni tekshiring:
# ■ Agar uzunligi 8 dan kam bo'lsa, "Juda qisqa"
# ■ Agar raqam yoki maxsus belgilar bo'lmasa, "Kuchsiz parol"
# ■ Aks holda, "Kuchli parol"

def check_password(arr):
    """User parollarini tekshiradigan funksiya"""
    if len(arr) > 0:
        for password in arr:
            if len(password) >= 8 and password.isascii() == True:
                print(f"Strong password: {password}")
            else: print(f"Invalid password: {password}")
    return "Check completed"
# check_password(password)

# 3. Ob-havo Ma'lumotlarini Tahlil Qilish:
# ○ Bir hafta davomida kundalik haroratlar ro'yxati berilgan (masalan,
temp = [20,22, 19, 24, 25, 23, 21]
# ○ for sikli yordamida o'rtacha haroratni hisoblang va har bir kun uchun
# agar harorat 22 dan yuqori bo'lsa, "Iliq kun", aks holda "Salqin
# kun" deb chiqaring.

def check_temp(arr):
    """haroratga qarab ob-havoni tahlil qiladigan funksiya"""
    k = len(arr)
    if arr[0]:
        T = 0
        for c in arr:
            T += c
        t = T / k
        print(f"Haftalik o'rtacha harorat selsiy shkalasi bo'yicha {t}°C ga teng")

        for i in arr:
            if i >= 22:
                print(f"Bugun havo harorati {i}°C, iliq kun")
            else: print(f"Bugungi havo harorati {i}°C, havo salqin")

# check_temp(temp)

# 4. Restoran Buyurtmalari:
# ● Mavjud taomlar ro'yxati berilgan (masalan,
meals_menu = ["Osh", "Shashlik", "Manti", "Lag’mon" ]
# ● Foydalanuvchidan buyurtma kiritishni so'rang.
# ● for sikli yordamida foydalanuvchi kiritgan buyurtma mavjud taomlarga mos
# keladimi-yo'qligini tekshiring:
# ○ Agar mos kelsa, "Buyurtmangiz qabul qilindi" deb chiqaring.
# ○ Aks holda, "Kechirasiz, bunday taom yo'q" deb chiqaring.
def check_menu(arr, order):
    """User kiritgan ma'lumot bo'yicha arrayni for yordamida tekshirish"""
    if order.lower() in [meal.lower() for meal in arr]:
        return "Buyurtmangiz qabul qilindi"
    else:
        return "Kechirasiz, bunday yo'q"

# order = input("Qanday taom buyurasiz: ")
# if order:
#     print(check_menu(meals_menu, order))
# else:
#     print("Iltimos buyurtmangizni ayting: ")




# 5. Anketa Tahlili:
# ● Foydalanuvchilarning yoshlari ro'yxati berilgan (masalan,
pupils_ages = [16, 21, 17, 30, 25]
# ● for sikli yordamida har bir foydalanuvchining yoshini tekshiring:
# ○ Agar yosh 18 dan kichik bo'lsa, "Yosh chegarasiga yetmagan"
# deb chiqaring.
# ○ Aks holda, "Xush kelibsiz" deb chiqaring.

def check_pupil_age(arr):
    """Foydalanuvchu yoshini tekshiruvchi funksiya"""
    for age in arr:
        if age < 18:
            print(f"Siz {age} yoshda ekansiz, yosh chegarasiga yetmagansiz")
        else:
            print(f"Siz {age} yoshda ekansiz, voyaga yetgansiz, Xush kelibsiz")

# if pupils_ages:
#     check_pupil_age(pupils_ages)
# else:
#     print("Malumotlar topilmadi")


# 6. Mobil Ilova Bildirishnomalari: Bildirishnomalar sarlavhalari ro'yxati berilgan
xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for sikli yordamida agar sarlavha "Batareya past" bo'lsa, "Telefoningizni
# quvvatlang" deb print chiqaring.
def message(arr):
    """Messages for mobile phone"""
    txt = "Batareya past"
    if txt in [t for t in arr]:
        print("Telefoningizni quvvatlang")

# message(xabarlar)


# 7. Fayllarni guruhlash:
fayllar = [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# musiqalar=[ ] va rasmlar=[ ] nomli listlar yarating. Fayllar ustida sikl aylantirib “.jpg”
# larni rasmlar listiga, “.mp3” larni musiqalar listiga qo’shing. Yordam: find() string
# metodi va append() list metodidan foydalaning.

def sorted_file(arr):
    """Fayllarni kengaytmasiga qarab tartiblovchi funksiya"""
    musics = []
    images = []
    music = ".jpg"
    img = ".mp3"

    for item in arr:
        if item.endswith(music):
            musics.append(item)
        if item.endswith(img):
            images.append(item)
    return (images, musics)

# print(sorted_file(fayllar))


numbers = list(range(10))
# print(numbers)

# for i in numbers:
#     pass

# str1 = "Salom"
# for s in str1:
#     print(s)
# else: print("Finished")

# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print("\r")

# rows = 5
# for i in range(1, rows + 1):
#     print("* " * i)

# rows = 5
# for i in range(rows + 1, 0, -1):
#     for k in range(0, i - 1):
#         print("*", end=" ")
#     print(" ")

# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

def star_style(n):
    """Bu funksiya * ni kapalak stilida chop etadi"""
    for i in range(n):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n - i - 1) + '*' * (i + 1)
        )
    for i in range(n - 2, -1, -1):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n -i - 1) + '*' * (i + 1)
        )

# star_style(5)

# my_string = input('Enter your string: ')
# my_char = input('Enter your character: ')
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# new_string = ''
# for i in my_string:
#     if i in vowels:
#         new_string += my_char
#     else:
#         new_string += i
# print(new_string)

def style_diamond(n):
    for i in range(1, 2 * n):
        spaces = abs(n - i)
        stars = 2 * (n - spaces) - 1
        print(' ' * spaces + '*' * stars)
# style_diamond(5)

def char(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(65 + k), end=" ")
            k += 1
        print()

# char(5)

def numeric(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()

# numeric(5)












































































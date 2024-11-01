#
# # Amaliyot
# “if, elif, else” shart operatorlari mavzusi bo’yicha vazifalar
# 1. Ob-havo Tavsifi: Foydalanuvchidan ob-havo haroratini inputda so'rang.
# Agar harorat 0 dan past bo'lsa, "Sovuq" deb print chiqaring.
# Agar 0 dan 20 gacha bo'lsa, "Salqin".
# Agar 21 dan 30 gacha bo'lsa, "Iliq".
# Agar 31 dan yuqori bo'lsa, "Issiq" deb chiqaring.

def temp(c):
    """ Bu funksiya user kiritgan qiymat bo'yicha ob-havoni pragnoz qiladi"""
    if c < 0:
      return  "Havo sovuq"
    elif c > 0 and c < 20:
      return "Havo Salqin"
    elif c > 21 and c < 30:
      return "Havo iliq"
    elif c > 30:
      return "Havo issiq"

# c = input("Ixtiyoriy raqam kiriting: ")
# if c.isalpha() != True and c != "":
#     print(temp(int(c)))
# else:
#     print("Kechirasiz, to'g'ri ma'lumot kiritilmadi")


# 2. Internet-do'kon Chegirmasi: Foydalanuvchidan xarid summasini so'rang. Agar summa
# 50,000 so'mdan kam bo'lsa, chegirma yo'q. Agar 50,000 dan 100,000 so'mgacha bo'lsa,
# 5% chegirma. Agar 100,000 so'mdan yuqori bo'lsa, 10% chegirma hisoblang va yakuniy
# narxni chiqaring.

def discount_sale(c):
    """ Haridor qancha savdo qilganiga qarab chegirma hisoblovchi funksiya"""
    if c < 50000:
        return f"Sizdan jami {c} so'm bo'ldi. Haridingiz uchun raxmat!"
    elif c > 50000 and c < 100000:
        d = c/100 * 5
        x = c - d
        return f"Hurmatli mijoz sizga {d} so'm miqdorida chegirmamiz bor. Sizdan jami {x} so'm bo'ldi"
    elif c > 100000:
        d = c / 100 * 10
        x = c - d
        return f"Hurmatli mijoz sizga {d} so'm miqdorida chegirmamiz bor. Sizdan jami {x} so'm bo'ldi"

# n = input("Necha pullik harid qildingiz: ")
# if n.isalpha() == False and n != None:
#     a = int(n)
#     print(discount_sale(a))
# else:
#     print("Aniqroq ma'lumot bersangiz iltimos!")

# 3. Tizimga Kirish: Foydalanuvchidan login va parolni so'rang. Agar login "admin" va parol
# "12345" bo'lsa, "Xush kelibsiz, admin!" deb chiqaring. Agar login yoki parol noto'g'ri bo'lsa,
# "Login yoki parol xato" deb chiqaring.

def login(login, password):
    """Login va parolni tekshiruvchi funksiya"""
    if login == "admin" and password == "12345":
        return "Hush kelibsiz Admin"

    return "Login yoki parol xato!"

# user_login = input("Loginingizni kiriting: ")
# password = input("Parolingizni kiriting: ")
# if user_login == "" or password == "":
#     print("Iltimos Bo'limlarni barchasini to'ldiring!")
# else:
#     print(login(user_login, password))




# 4. Film Yosh Cheklovi: Foydalanuvchidan yoshini so'rang. Agar yosh 13 dan kichik bo'lsa,
# "Sizga ushbu film tavsiya etilmaydi" deb chiqaring. Agar 13 dan 17 gacha bo'lsa, "Siz filmni
# ota-onangiz bilan ko'rishingiz mumkin". Agar 18 va undan katta bo'lsa, "Siz filmni tomosha
# qilishingiz mumkin" deb chiqaring.

def view_cinema(age):
    """Yoshiga qarab, Tomoshabinni nazorat qiluvchi funksiya"""
    if age < 13:
        return "Sizga bu film tavsiya qilinmaydi"
    elif age >= 13 and age <= 17:
        return "Siz bu filmni ota-ona nazoratida tomosha qilishingiz mumkin"
    return "Film Tomosha qilishingiz mumkin"

# age = input("Yoshingiz nechida: ")
# if age.isalpha() == False and age != "":
#     x = int(age)
#     print(view_cinema(x))
# else:
#     print("Yoshingizni to'g'ri kiriting: ")

# 5. Restoran Menyusi: Foydalanuvchiga menyudan taom tanlash imkoniyatini bering: 1 -
# "Osh", 2 - "Mastava", 3 - "Shashlik". Tanlovga qarab taomning narxi va tayyorlanish vaqtini
# chiqaring.

taom = {
    "osh":[25000, 10],
    "mastava":[25000, 10],
    "shashlik":[15000, 20],
}
def order_meal(order, taom):
    if order in taom:
        result = taom[order]
        return f"{order} {result[0]} so'm, {result[1]} daqiqada tayyor bo'ladi"
    elif order not in taom:
        return "Kechirasiz bizda bu taom yo'q edi!"

def welcome():
    print("Biror nima buyurasizmi, Bugungi menyuimizda! ")
    for key in taom.keys():
        print(f"{key}, ", end="")

    order = input("bor! siz nima buyurtma qilmoqchisiz!>>> ")

    if order != "":
        order_meal(order, taom)

    taklif = input("Yana biror nima buyurasizmi, Ha/Yo'q >>>  ").lower()

    if taklif == "ha":
        welcome()
    elif taklif == "yo'q" or taklif != "ha":
        return order_meal(order, taom)

# print(welcome())




# 6. Email Tekshiruvi: Foydalanuvchidan email manzilini inputda kiritishni so'rang. Agar
# emailda "@" belgisi va "." nuqtasi bo'lmasa, "Noto'g'ri email manzili" deb chiqaring. Aks
# holda, "Email qabul qilindi" deb chiqaring.
# Yordam: find() string metodidan foydalaning. Masalan if matn.find(“belgi”) == -1 bo’lsa
# demak belgi matnda topilmagan bo’ladi.

def email_address(email):
    """Emailni tekshiruvchi funksiya"""
    if email.endswith("@gmail.com"):
        return "Email successfuly"
    else:
        return "Biz faqat @gmail.com kengaytmali emailni quvvatlaymiz, iltimos! shartlarga rioya qiling"

# email = input("Emailni to'ldiring:>>> ")
# if email != "":
#     print(email_address(email))
# else:
#     print("Email manzilingizni kiriting.")

# 7. Talaba Baholash Tizimi: Foydalanuvchidan olgan ballini so'rang (0 dan 100 gacha).
# Quyidagi mezonlarga ko'ra bahoni print qiling:
# ● 86 dan 100 gacha: 5 baho
# ● 70 dan 85 gacha: 4 baho
# ● 55 dan 69 gacha: 3 baho
# ● 55 dan past: 2 baho

def baho(b):
    """Talabaning bahosini aniqlash funksiyasi"""
    if b < 55:
        return "2 baho"
    elif b > 55 and b <= 69:
        return "3 baho"
    elif b > 69 and b <= 85:
        return "4 baho"
    elif b >= 86 and b <= 100:
        return "5 baho"

# b = input("To'plagan balingizni kiriting: ")
# if b != '' and b.isalpha() != True:
#     x = int(b)
#     print(baho(x))
# else:
#     print("Kerakli ma'lumotni kiriting!")


# 8. Bankomat Pul Yechish: Foydalanuvchidan kartasidagi summani va yechmoqchi
# bo'lgan summani so'rang. Ya’ni 2 ta input bo’ladi. Agar kartadagi puli yechiladigan puldan
# kam bo'lsa, "Hisobda yetarli mablag' mavjud emas" deb print chiqaring. Agar yechiladigan
# summa 5 000 so'mdan kam bo'lsa, "Minimal yechish summasi 5 000 so'm" deb chiqaring.
# Aks holda, "Pul muvaffaqiyatli yechildi" deb print chiqaring va kartadagi qolgan mablag'ni
# print qiling.

def payme(total, pay):
    """ Karta ma'lumotlari bilan ishlash funksiyasi """
    if pay > total:
        return "Kartada mablag' yetarli emas"
    elif pay < 5000:
        return "Eng kam yechiladigan pul miqdori 5000 so'm"
    else:
        total = total - pay
        return f"Pul muvofaqqiyatli yechildi, kartangizda qolgan pul miqdori: {total}"

# total = input("Kartangizda qancha pul qolgan deb o'ylaysiz: ")
# pay = input("Kartangizdan necha pul yechmoqchisiz: ")

# if total != "" and pay != "" and total.isalpha() == False and pay.isalpha() == False:
#     total = int(total)
#     pay = int(pay)
#     print(payme(total, pay))
# else:
#     print("Malumotlarni kiriting!")

# 9. Ish Jadvalini Tekshirish: Foydalanuvchidan haftaning kunini so'rang (Dushanba,
# Seshanba, ... , Yakshanba). Agar kun "Shanba" yoki "Yakshanba" bo'lsa, "Bugun dam olish
# kuni" deb chiqaring. Aks holda, "Bugun ish kuni" deb chiqaring.

def weeks(week, arr):
    """Hafta kuniga qarab kun tartibini tahlil qiluvchi funksiya"""
    if week == "shanba" or week == "yakshanba":
        return "Bugun dam olish kuni"

    if week not in arr:
        return "Hafta kunlaridan birini kiriting"

    if week in arr and week != "shanba" and week != "yakshanba":
        return "Bugun ish kuni"

arr = set(("yakshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"))

# week = input("Bugun qaysi kun: ").lower()
# if week != "":
#     print(weeks(week, arr))
# else:
#     print("Bugun qaysi kunligini aniq kiriting, iltimos!")


# 10. Mobil Tarif Tanlash: Foydalanuvchidan oyiga qancha internet trafikidan foydalanishini
# so'rang (GB da). Agar trafik 1 GB dan kam bo'lsa, "Sizga 'Mini' tarifi mos keladi" deb
# chiqaring. Agar 1 GB dan 5 GB gacha bo'lsa, "Sizga 'Standard' tarifi mos keladi". Agar 5
# GB dan yuqori bo'lsa, "Sizga 'Unlimited' tarifi mos keladi" deb chiqaring.
#
def tarif(t):
    """Userga oyilik trafik sarfiga qarab, tarif tanlab beruvchi funksiya"""
    k = 1024
    t = t * k
    if t < 1024:
        return "Sizga Mini tarifi mos"
    elif t > 1024 and t <= 5 * k:
        return "Sizga Standart tarifi mos"
    elif t > 5 * k:
        return "Sizga Unlimited tarifi mos"

trafik = input("Bir oylik trafik sarfingiz necha MB: ")

if trafik != "" and int(trafik) > 0 and trafik.isalpha() == False:
    trafik = int(trafik)
    print(tarif(trafik))
else:
    print("Kerakli miqdorni to'g'ri kiriting!")



# a = 150
# b = 170
#
# # print(a) if a > b else print(b)# short handling
# x = 100
# if x > 50:
#     print(f"{x} 50 dan katta")
#     if x > 70:
#         print(f"{x} 70 dan ham katta")
#     else:
#         print(f"{x} soni bizga mos emas")
#
# num = []
# for i in range(2, 20):
#     if i % 2 != 0:
#         continue
#     else: num.append(i)
#
# # print(num)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# capitalize()	satrdagi birinchi belgini Katta harfga aylantiradi
str1 = "python"
# print(str1.capitalize())

#casefold()	satrni kichik harflarga aylantiradi
str2 = "PYTHON"
# print(str2.casefold())

# center()	satrni berilgan qiymat bo'yicha markazga joylashtiradi
str3 = "Python"
# print(str3.center(20, "*"))

# count() Belgilangan qiymat satrda necha marta sodir bo'lishini qaytaradi
str4 = "Nodejs, JS, Reactjs, vuejs, Angularjs"
# print(str4.casefold().count('js'))

# endswith() Agar satr belgilangan qiymat bilan tugasa, true qiymatini qaytaradi
str5 = "I'm learning python"
# print(str5.endswith('python'))
# print(str5.endswith('js'))

# find() - metodi satrdagi qidirilayotgan belgining birinchi paydo bo'lish o'rnini qaytaradi
# agar qiymat topilmasa -1 qaytaradi, agar find() argumentsiz ishlatilsa 0 qaytaradi

str6 = "Welcome to my family, welcome to my friends"
# print(str6.casefold().find('welcome'))
# print(str6.find('js'))
# print(str6.find('to', 4, 10))

# index() metodi find() metodi kabi ishlaydi,
# yagona farqi izlanayotgan qiymat topilmasa dastur xato qaytaradi va to'xtab qo'ladi

str7 = "Nodejs, reactjs, js"
# print(str7.index('js'))
# print(str7.index('py'))
# print(str7.index('react', 2, 15))

# isalnum()Agar barcha belgilar alfavit-raqamli bo'lsa,
# bu usul alifbo harfi (az) va raqamlarni (0-9) bildirsa, "True" qiymatini qaytaradi.

str8 = "python24"
# print(str8.isalnum())


# isalpha() Agar barcha belgilar alifbo harflari (az) bo'lsa, usul "True" ni qaytaradi .
# Alfavit harflari bo'lmagan belgilarga misol: (bo'shliq)!#%&? va hokazo.

str9 = "python"
# print(str9.isalpha())

# isascii()Agar barcha belgilar ascii belgilar (az) bo'lsa,
# usul True qiymatini qaytaradi .
# ascii jadvalida katta harflar 65-index raqamdan 90-indexgacha,
# kichik harflar 97-indexdan 122-indexgacha ingliz alifbosi tartibida keladi

str10 = "PythonABC789"
# print(str10.isascii())


# isdigit(), agar barcha belgilar raqam bo'lsa,
# True, aks holda False qiymatini qaytaradi.
str11 = "2024"
# print(str11.isdigit())


#  isidentifier(), agar satr haqiqiy identifikator bo'lsa,
#  True qiymatini qaytaradi, aks holda False.
# Agar satrda faqat alfanumerik harflar (az) va (0-9) yoki
# pastki chiziq (_) bo'lsa, u haqiqiy identifikator hisoblanadi.
# Yaroqli identifikator raqam bilan boshlanmasligi yoki bo‘sh joyni o‘z ichiga olmaydi.

str12 = "_id"
# print(str12.isidentifier())

# islower(), agar barcha belgilar kichik harfda bo'lsa,
# True qiymatini qaytaradi, aks holda False.
# Raqamlar, belgilar va bo'shliqlar belgilanmaydi, faqat alifbo belgilar.

str13 = "Python Language"
# print(str13.islower())
# print(str13.casefold().islower())

# isnumeric(), agar barcha belgilar raqamli bo'lsa (0-9) True,
# aks holda False qiymatini qaytaradi.
# ² va ¾ kabi ko'rsatkichlar ham raqamli qiymatlar hisoblanadi.
# "-1"va "1.5"raqamli qiymatlar EMAS, chunki satrdagi

str14 = "20242025"
# print(str14.isnumeric())

# isspace()Agar satrdagi barcha belgilar bo'sh joy bo'lsa,
# usul "True", aks holda "False" ni qaytaradi .

str15 = "    "
str15_1 = "  .py"
# print(str15.isspace())
# print(str15_1.isspace())


# istitle()Agar matndagi barcha so'zlar katta harf bilan boshlansa,
# VA so'zning qolgan qismi kichik harflar bo'lsa, usul "True" qiymatini qaytaradi,
# aks holda "False" .
# Belgilar va raqamlar e'tiborga olinmaydi.

str16 = "Python Developer"
str16_1 = "Py js"
# print(str16.istitle())
# print(str16_1.istitle())

# isupper(), agar barcha belgilar bosh harfda bo'lsa,
# True, aks holda False qiymatini qaytaradi.
# Raqamlar, belgilar va bo'shliqlar belgilanmaydi, faqat alifbo belgilar.

str17 = "PYTHON DEV"
# print(str17.isupper())

# join()barcha elementlarni iteratsiyada oladi va ularni bitta satrga birlashtiradi.
# Ajratuvchi sifatida qator ko'rsatilishi kerak.

str18_tuple = ('JS', 'Nodejs', 'Python')
# print(', '.join(str18_tuple))

# lower()barcha belgilar kichik harf bo'lgan qatorni qaytaradi.
# Belgilar va raqamlar e'tiborga olinmaydi.

str19 = "PYTHON"
# print(str19.lower())

# maketrans() satrdagi istalgan belgini ko'rsatilgan belgiga xaritalaydi
str20 = "JS Nodejs Py"
x = str20.maketrans('J', "P") # ascii jadvalidagi harning indexni ko'rsatadi
# print(str20.translate(x))

# replace() belgilangan iborani boshqa belgilangan ibora bilan almashtiradi.

str21 = "Nodejs Reactjs JS JS JS JS JS"
a = str21.count('JS') # JS necha marta qatnashgani qiymati
# print(str21.replace('JS', 'Javascript', a))

# upper()barcha belgilar katta harf bilan yozilgan qatorni qaytaradi.
str22 = "python"
# print(str22.upper())

# split()qatorni ro'yxatga ajratadi.
# Siz ajratuvchini belgilashingiz mumkin, standart ajratuvchi har qanday bo'shliqdir.

str23 = "Python, JS, Reactjs"
# print(str23.split(","))

# strip() oldingi va keyingi bo'shliqlarni olib tashlaydi.
# Satrning boshidagi yetakchi, oxiridagi ma’noni bildiradi.
# Qaysi belgilarni olib tashlashni belgilashingiz mumkin, agar bo'lmasa,
# barcha bo'shliqlar o'chiriladi.

str24 = "  Python  "
n = len(str24)
# print(n)
m = len(str24.strip())
# print(m)

# len() metodi satr uzunligini qaytaradi
str25 = "Python"
# print(len(str25))

# swapcase() Kichik harflarni katta va katta harflarni kichik harflar bilan belgilang

str26 = "pthon NODEJS REACTJS"
# print(str26.swapcase())

# startswith(), agar satr belgilangan qiymatdan boshlansa,
# True qiymatini qaytaradi, aks holda False.
# bo'shliqlar va turli belgilar hisobga olinadi

str27 = "py js react"
# print(str27.startswith("py"))

# zfill()belgilangan uzunlikka yetguncha satr boshida nol (0) qo'shadi.
# Agar len parametrining qiymati satr uzunligidan kichik bo'lsa,
# hech qanday to'ldirish amalga oshirilmaydi.

str28 = "python"
# print(str28.zfill(5))
# print(str28.zfill(10))

# lstrip() - satrning chap tomonidagi bo'shliqni o'chiradi
str29 = "  Py  "
# print(str29.lstrip())

# rstrip() - satrning o'ng tarafidagi bo'shliqni olib tashlaydi
str30 = "  Py  "
# print(str30.rstrip())

# rsplit() satrning o'ng tarafidan boshlab ro'yxatga ajratadi
str31 = "py, js, php"
d = str31.rsplit(', ', 1)
# print(d)

# rfind() satrning o'ng tarafidan boshlab ro'yxatga ajratadi
str32 = "py, js, php"
# print(str32.rfind('p'))

str33 = "py, js, nodejs"
# print(str33.rfind('n', -8, -1))

str34 = "python javascript"
# print(str34.rindex('j', -12, -1))

# rjust()to'ldirish belgisi sifatida belgilangan belgidan (bo'sh joy sukut bo'yicha) foydalanib,
# satrni to'g'ri tekislaydi.

str35 = "python"
# print(str35.rjust(15))















































































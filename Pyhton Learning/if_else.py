# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:38:54 2024

@author: Sherzodbek
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
change_cars = []

for x in cars:
    if x == 'gm' and x in cars:
        change_cars.append(x.upper())
    else :
        change_cars.append(x.title())
print(change_cars)




for x in cars:
    if x != 'gm':
        change_cars.append(x.title())
    else :
        change_cars.append(x.upper())
      
print(change_cars)



user = input("Loginingizni kiriting: ")

if user.lower() == "admin":
    print(f"Xush kelibsiz {user}, foydalanuvchilar ro'yxatini ko'rishni istaysizmi ?")
else:
    print(f"Saytimizga xush kelibsiz {user}")



son_1 = int(input('Ixtiyoriy son kiriting: '))
son_2 = int(input('Ixtiyoriy son kiriting: '))

if son_1 == son_2:
    print('Sonlar teng')
else:
    print('Sonlar teng emas')

son_3 = int(input('Ixtiyoriy son kiriting: '))
if son_3 < 0:
    print('Kiritilgan son manfiy')
elif son_3 == 0:
    print('Son 0 ga teng')
else:
    print('Son musbat, uning kvadrat ildizi', son_3**(1/2))




# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
#  agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.


son = int(input("Iltimos, juft son kiriting: "))

if son % 2 == 0:
    print("raxmat")
else:
    print("bu juft son emas")


# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

age = int(input("Xush kelibsiz, yoshingiz nechida: "))

if age < 4 or age > 60:
    print("Hurmatli mehmon, muzeyga kirish siz uchun bepul")
elif age > 4 and age < 18:
    print("Hurmatli mehmon, muzeyga kirish narxlari siz uchun: 10000 so'm")
else :
    print("Hurmatli mehmon, muzeyga kirish siz uchun 20000 so'm")


# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring


number_one = int(input("son kiriting: "))
number_two = int(input("yana bitta son kiriting: "))

if number_one == number_two:
    print("sonlar teng")
elif number_one > number_two:
    print(f"{number_one} katta {number_two} dan")
else:
    print(f"{number_one} kichik {number_two} dan")


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri 
# ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

products = list(("Non", "choy", "Kabob", "Palov", "BeshBarmoq", "Norin", "Shorva", "Mastava", "Somsa", "salat" ))

box = []

for taom in range(len(products)):
    if taom == "yetadi, raxmat":
        break
    elif taom not in products:
        print("Kechirasiz bu buyurtmangiz bizda yo'q")
    else:
        box.append(taom)


print(f"Sizning buyurtmalaringiz: {box}")

not_yet = []

for taom in range(len(products)):
    taom = input("Nima buyurtma qilasiz: ")
    if taom == "yetadi, raxmat":
        break
    elif taom not in products:
        print("Kechirasiz bu buyurtmangiz bizda yo'q")
        not_yet.append(taom)
    else:
        box.append(taom)


print(f"Sizning buyurtmalaringiz: {box}")
if len(not_yet) == 0:
    print(f"Siz so'ragan barcha mahsulotlar {products} do'konimizda bor")
else:
    print(f"Siz so'ragan bu mahsulotlar {not_yet} do'konimizda yo'q")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni 
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa,
# "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users_logins = ["Ali", "devPro","PythonDev"]

for n in range(len(users_logins)):
   users_logins[n] = users_logins[n].lower()
   
for i in range(len(users_logins)):
    user_login = input("Login kiriting: ")
    if user_login in users_logins:
        print("Boshqa login kiriting")
    else:
        print(f"Xush kelibsiz hurmatli {user_login}")
        break

# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan
# qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

num = int(input("Butun son kiriting: "))

res = []
for i in range(2, 11):
    if i % num != 0:
        continue
    else:
        res.append(i)
print(res)



























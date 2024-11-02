# while tsikli bilan biz shart to'g'ri bo'lsa,
# bir qator bayonotlarni bajarishimiz mumkin.

# WHILE sikli mavzusi bo’yicha vazifalar

# 1. Svetafor: Foydalanuvchidan inputda svetavor qaysi rangda deb so’rang. qizil,
# sariq yoki yashil deb yozmoagunicha, bu xato rang deb qayta so’rayvering. Agar shu
# ranglardan birini tanlasa “rahmat, to’g’ri keladi” degan print chiqazing.

def traffic_light():
    """Svetafor rangi nazorati funksiyasi"""
    colors = ["yashil", "sariq", "qizil"]
    while True:
        print("Svetafor qaysi rangda! ")
        color = input(">>> ")
        if color.lower() in [color.lower() for color in colors]:
            return "Raxmat, to'g'ri keladi"

# print(traffic_light())


"""
  Tasodifiy Sonni Topish O'yini: Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son
  o'ylaydi. Foydalanuvchidan ushbu sonni topishni so'rang. Foydalanuvchi to'g'ri sonni
  topguncha davom etadi. Har bir noto'g'ri urinishdan so'ng, "Noto'g'ri, qayta urinib
  ko'ring" deb chiqaring. To'g'ri topilganda, "Tabriklaymiz, siz topdingiz!" deb chiqaring.
  Ko'rsatma: random. dan foydalanib tasodifiy son yarating va while sikli yordamida
  foydalanuvchi kiritmalarini tekshiring
"""

import random


def find_number(n):
    number = random.randint(0, 11)
    i = 0
    while True:
        n = int(input("Sonni toping: "))
        i += 1
        if n > number:
            print("Noto'g'ri, qayta urinib ko'ring")
        elif n < number:
            print("Noto'g'ri, qayta urinib ko'ring")
        else:
            print(f"Tabriklaymiz, siz {i} ta urinishda topdingiz!")
            break


# n = int(input("Sonni toping: "))
# find_number(n)

"""
  Vazifa: Foydalanuvchidan do'stlarining ismlarini kiritishni so'rang.
  Foydalanuvchi "stop" deb yozmaguncha, yangi ismlar qo'shilaveradi. Oxirida
  barcha do'stlarining ismlari ro'yxatini chiqaring.
  ● Ko'rsatma: While sikli va list metodlaridan foydalanib, ro'yxatni shakllantiring.
"""


def my_friends():
    """Do'stlar ro'yxatini tuzish"""
    friends = []
    while True:
        name = input("Do'stingizni ismini kiriting: ").lower()
        if name != 'stop' and name != '':
            friends.append(name.title())
        elif name == 'stop':
            break
        elif name == "":
            print("Iltimos, ismni kiriting")
    return friends


# print(my_friends())


"""
  Valyuta Ayirboshlash Kalkulyatori: Foydalanuvchiga valyuta ayirboshlash
  imkoniyatini bering. U so'mni dollarga almashtirishi mumkin. Valyuta kurslarini
  oldindan belgilang (masalan, 1 USD = 12,600 so'm). Foydalanuvchi summani
  kiritadi, dastur esa hisob-kitobni chiqaradi. Foydalanuvchi "exit" deb yozmaguncha
  dastur davom etadi.exit deb yozsa dastur to’xtaydi
"""


def exchange_rate():
    """Foydalanuvchi kiritgan summani dollarga almashtirish"""
    while True:
        money = int(input("Summani kiriting: ").lower())
        if money == 'exit':
            break
        elif money != '':
            res = round((money / 12600), 3)
            print(f"Sizning {money} so'm pulingiz {res} $ dollar bo'ladi")
        else:
            print("Iltimos, summani kiriting")


# exchange_rate()

# 1. While siklidan foydalanib print qiling:
# 1
# 22
# 333
# 4444
# 55555

def piramid():
    n = 1
    while n <= 5:
        print(str(n) * n)
        n += 1


# piramid()

# 2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
# input: 555   output: 15
# input: 8125   output: 16

def number_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


# n = int(input("Sonni kiriting: "))
# if n:
#   print(number_sum(n))


# 3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing
def toq_sonlar():
    numbers = list(range(1, 101, 2))
    print(numbers)
    sum = 0
    while numbers:
        sum += numbers.pop()

    return sum


# print(toq_sonlar())


# 3. While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing

# 4. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
# Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
# foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
# Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
# foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
# taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
# qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.


# Tasodifiy raqam yaratish

def random_number():
    # Tasodifiy raqam yaratish
    target = random.randint(1, 100)
    print("1 dan 100 gacha bo'lgan raqamni topishga harakat qiling!")

    # Binary Search chegaralarini belgilash
    low = 1
    high = 100

    while True:
        # Foydalanuvchidan taxmin kiritishni so'rash
        try:
            user_guess = int(input("Raqamni kiriting: "))
        except ValueError:
            print("Iltimos, raqam kiriting!")
            continue

        if user_guess < low or user_guess > high:
            print(f"Raqam {low} va {high} oralig'ida bo'lishi kerak.")
            continue

        # Binary Search algoritmi bilan foydalanuvchi taxminini tekshirish
        if user_guess < target:
            print("Juda past!")
            low = user_guess + 1  # Past chegarani yangilash
        elif user_guess > target:
            print("Juda baland!")
            high = user_guess - 1  # Yuqori chegarani yangilash
        else:
            print("To'g'ri topdingiz!")
            break


random_number()






































































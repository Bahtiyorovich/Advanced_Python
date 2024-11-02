# "user_data" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (first_name, last_name, age).
# Input orqalik ism, familiya va yoshni kiritamiz.
# va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
# "user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini
#
#   Ism: Alisher
#   Familiya: Olimov
#   Yosh: 27
#
# ko'rinishiga print qilib bersin.
from audioop import reverse


def user_data(**data):
    """User ma'lumotlarini chop etuvchi funksiya"""
    for key, value in data.items():
        print(f"{key}:{value}")

# user_data(Ism = "Alisher", Familya = "Olimov", Yosh = 27)


# "find_max" funksiyasini elon qilasizlar.
# Funksiyani 3 ta parametri bor (a, b, c).
# Input orqalik 3 ta son kiritamiz.
# va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
# "find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
# topib print qiladi.
#
#   Eng katta son - A = 10
#   yoki
#   Eng katta son - A va B = 10
#   yoki
#   Eng katta son - A va B va C = 10

def find_max(a, b, c):
    """Sonlarning eng kattasini va teng sonlar borligini aniqlovchi funksiya"""

    if a == b == c:
        return f"Uchta son ham teng"


    if a >= b and a >= c:
        if a == b or a == c:
            return f"Eng katta son - {a}"
        else:
            return f"Eng katta son - {a}"
    elif b >= a and b >= c:
        if b == a or b == c:
            return f"Eng katta son - {b}."
        else:
            return f"Eng katta son - {b}"
    else:
        if c == a or c == b:
            return f"Eng katta son - {c}"
        else:
            return f"Eng katta son - {c}"


# print(find_max(7, 6, 5))
# print(find_max(7, 7, 7))
# print(find_max(4, 11, 11))


"""
find_letter_count" funksiyasini elon qilasizlar.
Funksiyani 2 ta parametri bor (word, letter).
Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
"find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
"word" da "letter" nechi martda qatnashganini print qilsin.

  "Programing" so'zida "r" dan 2 ta.

"""

def find_letter_count(word, letter):
    """Berilgan so'zda necha marta letter argumenti qatnashganini aniqlovchi funksiya"""
    n = word.count(letter)

    return f"{word} so'zida {letter} harfi {n} marta qatnashgan"

# word = input("Pythonga oid ixtiyoriy so'z kiriting: ")
# letter = input("Yuqorida kiritilgan so'zda siz hozir kiritadigan harf nechtaligini aniqlaymiz, Iltimos harf kiriting >>> ")
# if word != "" and letter != "":
#     print(find_letter_count(word, letter))
# else:
#     print("Iltimos ma'lumotlarni to'liq kiriting!")


"""
    "list_sum" funksiyasi elon qilasizlar.
    Funksiyani 1 ta pametrni bor (myList).
    "myList" funksiyasini chaqirib unda argumentini berasizlar.
    uni ichida esa myList elementlarini yig'indisini print qilasizlar.
    
      Listning elementlar yig'indisi = 32
"""
def list_sum(arr):
    """List elementlari yig'indisini qaytaruvchi funksiya"""
    sum = 0
    if arr:
        for i in arr:
            sum += i
    return sum

# numbers = [1,2,3,4,5,6,7]
# print(list_sum(numbers))


# daraja(a, b) - bu funksiya a ni b darajasini print qilsin.

def pow(a, b):
    """Kiritilgan argumentlar bo'yicha"""
    return (a ** b)

# print(pow(2, 3))


def pow_numbers(a, *n):
    """Daraja hisoblash"""
    for i in n:
        print(a ** i)

# pow_numbers(2, 2,3,4,5)


# digit_count_and_sum(word) - bu funksiya "word" ni ichidagi
# raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.

def digit_count_and_sum(word):
    """berilgan so'z ichida nechta raqam qatnashgan
    bo'lsa ularni yig'indisini aniqlovchi funksiya"""
    sum = 0
    numbers = []
    if word:
        for i in word:
            if i.isdigit():
                sum += int(i)
                numbers.append(i)
    else:
        return "So'zni kiriting"

    n = len(numbers)
    return f"Berilgan so'zda {n} ta raqam ishlatilgan, ularning yig'indisi {sum} ga teng"

# print(digit_count_and_sum("123python45"))
# print(digit_count_and_sum(""))


# add_right(a, b) - bu funksiya a sonini o'ng tomoniga
# b sonini birlashtirib qoysin va print qilsin.

def add_right(a, b):
    """Ikki raqamni birlashtiruvchi funksiya"""
    result = str(a) + str(b)
    return result

# print(add_right(2, 5))


# add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini
# birlashtirib qoysin va print qilsin.

def add_left(a, b):
    result = str(b) + str(a)
    return result

# print(add_left(5, 7))

# work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga
# ko'paytirib qiymatini o'zgartiradi va listni print qilsin.

def work_with_list(arr):
    """List ma'lumotlarini yangilash va qayta tartiblash"""
    # Asl listni tartiblash
    arr.sort()
    k = len(arr)

    # Qayta ishlash
    for i in range(k - 1, -1, -1):
        x = arr.pop(i) * arr[0]
        arr.append(x)

    arr.sort(reverse=False)
    return arr

#
# arr = [5, 7, 1, 3, 9, 6, 4]
# print(work_with_list(arr))


# 11. big_sales(sales) funksiyasini yarating.
# sales bu
# qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.

dictionary = {
  "yanvar": 12000,
  "mart": 6000,
  "aprel": 15000,
  "sentabr": 9000,
  "dekabr": 10000,
}

def max_sale(sales):
    """Lug'at ichidagi eng katta qiymatni aniqlovchi funksiya"""
    if not sales:
       return "Ma'lumotlar topilmadi"

    max_sale_month = None
    max_sale = None

    for key, value in sales.items():
        if max_sale is None or value > max_sale:
            max_sale = value
            max_sale_month = key
    return f"Eng katta savdo {max_sale_month} oyida {max_sale} so'm bo'lgan"

# print(max_sale(dictionary))

# min_max(numbers, max_num, min_num) max_num numbers ichigagi eng
# katta sonmi yoki yoqmi shuni aniqlang,
# min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang

def min_max(numbers, max_num, min_num):
    """Berilgan max_num va min_num qiymatlari numbers ichida qanday ahamiyatga ega"""

    # Listni tartiblaymiz
    numbers.sort()

    # Maksimum va minimum qiymatlarni aniqlaymiz
    maximum = numbers[-1]
    minimum = numbers[0]

    if max_num == maximum:
        max_result = f"{max_num} eng katta son"
    else:
        max_result = f"{max_num} eng katta son emas"

    if min_num == minimum:
        min_result = f"{min_num} eng kichik son"
    else:
        min_result = f"{min_num} eng kichik son emas"

    return f"{numbers} ichida {max_result}, {min_result}"

# arr = list(range(8))
# print(min_max(numbers=arr, max_num=9, min_num=5))


# expensiveProduct(products) - funksiyadagi products - list.
# Unga shunaqa qiymat beriladi.Eng qimmat telefon nomini print qilib bersin bu funksiya.
products = [
  {
    "name": "Iphone X",
    "price": 600
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  },
]

def expensive_product(products):
    """Berilgan listdagi eng qimmat maxsulot nomini chiqaramiz"""

    max_price = None
    max_product = None

    for product in products:
        if max_price is None or product["price"] > max_price:
            max_price = product['price']
            max_product = product['name']

    return f"Eng qimmat mahsulot: {max_product}, narxi: {max_price} so'm"

# print(expensive_product(products))
































































































































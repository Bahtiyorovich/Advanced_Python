# Vazifa
# Har safar chaqirilganda keyingi tub sonni generatsiya qiladigan generator yarating.

def prime_generator():
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

# primes = prime_generator()
#
# for _ in range(6):
#     print(next(primes))


# Kiritilgan belgilardan  parollar generatsiya qiladigan generator yarating.
import itertools

def password_generator(input_string):
    for pwd in itertools.permutations(input_string):
        yield ''.join(pwd)

# input_string = "abs"
# passwords = password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))


# Cheksiz Fibonachi sonlarini generatsiya qiladigan generator yarating.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci))


# listdagi elementlarni n tadan guruhlanganda barcha mavjud guruhlarni
# generatsiya qiladigan generator yarating.

def group_generator(arr, n):
    for group in itertools.permutations(arr, n):
        yield group

arr = [1,2,3,4]
n = 2
groups = group_generator(arr, n)
for group in groups:
    print(group)





# Hanoi Minorasi o'yini
from logging.config import stopListening


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# n = int(input("Enter the number of disks"))
# TowerOfHanoi(n, 'A', 'C', 'B')

# For tsiklning yaratilishi

# l = [1,2,3,4,5]
# l_iter = iter(l)
#
# while True:
#     try:
#         print(next(l_iter))
#     except StopIteration:
#         break

## **Generator - iterator qaytaruvchi funksiya bo’lib,
# ** **iterator yaratishning oson yo’li hisoblanadi.**

# generator yaratish uchun **return** o’rniga **yield** dan foydalanamiz.


def try_generator(y):
    n = y
    n += 1
    print("Performed addition")
    yield n

    n *= 2
    print("Performed multiplication")
    yield n

# result = try_generator(5)
# print(next(result))
# print(next(result))

# Bu funksiya yield operatoridan foydalanadi, bu esa uni generatorga aylantiradi va
# ketma-ket qiymatlarni yaratish imkoniyatini beradi.
#
# Kodning ishlash jarayoni
# try_generator(5) chaqirilganda result o'zgaruvchisiga generator obyektini qaytaradi,
# lekin funksiyaning o'zi bajarilmaydi.
#
# next(result) birinchi yield operatorigacha bo'lgan kodni bajaradi:
#
# n = y satri orqali n ning boshlang'ich qiymati 5 bo'ladi.
# n += 1 orqali n 6 ga o'zgaradi.
# "Performed addition" chop etiladi.
# yield n orqali 6 qaytariladi va kod bajarilishi to'xtatiladi.
# next(result) ikkinchi marta chaqirilganda, funksiya davom ettiriladi:
#
# n *= 2 orqali n 12 ga teng bo'ladi.
# "Performed multiplication" chop etiladi.
# yield n orqali 12 qaytariladi.
# Chiqish
# Bu kodda next(result) chaqiruvlari natijasida quyidagi chiqish olinadi:
#
# python
# Copy code
# Performed addition
# 6
# Performed multiplication
# 12
# Yuqoridagi print(next(result)) va print(next(result)) satrlari funksiyaning
# har bir yield nuqtasida to'xtatilib, ketma-ket qiymatlarni chiqarib beradi.


















































































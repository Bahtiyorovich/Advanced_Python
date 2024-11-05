# map() birinchi argument sifatida funksiyani,
# ikkinchi argument sifatida esa iterable (masalan, list) oladi va
# har bir elementga berilgan funksiyani qo'llaydi.

# Funksiya yarataylik
def multiply_by_2(x):
    return x * 2

# Ro'yxat
numbers = [1, 2, 3, 4, 5]

# map() funksiyasidan foydalanamiz
result = map(multiply_by_2, numbers)
print(list(result))  # Natija: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  # Natija: [2, 4, 6, 8, 10]


# filter() birinchi argument sifatida funksiyani, ikkinchi argument
# sifatida esa iterable oladi. Funksiya har bir
# elementga qo'llanadi va faqat True qiymat qaytaradigan elementlar saqlanadi.


# Juft sonlarni topuvchi funksiya
def is_even(x):
    return x % 2 == 0

# Ro'yxat
numbers = [1, 2, 3, 4, 5, 6]

# filter() funksiyasidan foydalanamiz
result = filter(is_even, numbers)
print(list(result))  # Natija: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))  # Natija: [2, 4, 6]



# reduce() funksiyasi functools modulidan import qilinadi.
# Bu funksiya birinchi argument sifatida funksiyani,
# ikkinchi argument sifatida iterable oladi va iterable elementlariga
# ketma-ketlikda qo'llanib, bitta yakuniy qiymat qaytaradi.

from functools import reduce

# Barcha elementlarni ko'paytiruvchi funksiya
def multiply(x, y):
    return x * y

# Ro'yxat
numbers = [1, 2, 3, 4, 5]

# reduce() funksiyasidan foydalanamiz
result = reduce(multiply, numbers)
print(result)  # Natija: 120 (1*2*3*4*5)

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Natija: 120


# Qisqacha Xulosa:
# map() — har bir elementga berilgan funksiyani qo'llaydi va yangi iterable qaytaradi.

# filter() — har bir elementga berilgan funksiyani qo'llaydi va
# True qiymat qaytargan elementlardan iborat yangi iterable qaytaradi.

# reduce() — iterable elementlariga ketma-ketlikda funksiyani
# qo'llaydi va yakuniy bitta qiymat qaytaradi.
# Ushbu funksiyalar ma'lumotlarni qayta ishlashda va
# kodni yanada ixcham yozishda juda qulaydir.




































































































# tuple - bu tartiblangan va o'zgarmas to'plam,
# va takroriy qiymatlarga ruxsat beradi
# Tuple elementlari indexlanadi
# Tuple yaratilgandan keyin biz uning elementlarini o'zgartira olmaymiz,
# qo'sha olmaymiz, olib tashlay olmaymiz

this_tuple = ("apple", "banana", "chery", "apple", "banana")
# print(len(this_tuple))

# bitta element bilan tuple yaratmoqchi bo'lsak {,} - elementdan keyin
# qo'yish kerak, aks holda python tupleni tan olmaydi

weeks = ('monday',)
# print(type(weeks))

# tuple har qanday ma'lumot turini olishi mumkin
elements = ('tuple', 2024, True)

new_tuple = tuple(('apple', "macPro"))
# print(type(new_tuple))

# tuple elementlarini ko'rish
my_tuple = ("Honda", "Toyota", "KIA", "BMW M_5 Compitation")
# print(my_tuple[1])
# print(my_tuple[2:])
# print(my_tuple[1:4])
# print(my_tuple[-4:-1])

# Tuple elementlari bilan amallar bajarmoqchi bo'lsangiz,
# avval uni list()ga aylantiring, list() ning barcha metodlarini qo'llash mumkin bo'ladi

(car1, car2, *car3) = my_tuple
# print(car1)
# print(car2)
# print(car3)

# count(); tuple.count(value)
# index(): tuple.index(value), qiymatning birinchi paydo bo'lish o'rnini bildiradi,
# agar topilmasa xato qaytardi


















# set - tartibsiz, o'zgartirish mumkin emas, takrorlanishlarga ruxsat berilmaydi

this_set = {"apple", "banana", True, 1, False, 0, "apple", "chery"}
# print(this_set)

# to'plamni yaratishda set() - metodidan foydalaning

my_set = set(("car", "number"))
# print(my_set)

# To'plamga element qo'shish usuli
this_set.add('Kisonli')
# for i in this_set:
#     print(i, end=" ")

car1 = {"mers"}
car2 = {"bmw m4", "bmw m5"}
car1.update(car2)
car3 = ["Malibu", "Cobalt"]
car1.update(car3)
# print(car1)

# agar to'plam elementlarini olib tashlash kerak bo'lsa

car1.remove('mers')
# print(car1)

car1.discard('Cobalt')
# print(car1)

car1.clear()
# print(car1)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 |set4
# print(myset)

# qo'shimcha ma'lumotlarni shu linkdan topasiz
# https://www.w3schools.com/python/python_sets_methods.asp



































































































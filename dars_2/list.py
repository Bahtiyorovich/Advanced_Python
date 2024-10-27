# list() - ro'yxat : elementlari tartiblangan,
# o'zgartirilishi mumkin, takroriy qiymatlarga ruxsat beradi

# ro'yxatda nechta element borligini aniqlash uchun len() metodidan foydalaning

# ro'yxat turlari har qanday ma'lumotlarga ega bo'lishi mumkin

# yangi ro'yxat yaratishda list() konstruktoridan foydalanish mumkin

arr = list(("apple", "cup", "banana"))
# print(arr)

# list - tartibli, o'zgaruvchan, takroriy azolarga ruxsat bor
# tuple - tartibli, o'zgarmas, takroriy azolarga ruxsat bor
# set - tartibsiz, o'zgarmas va indekslanmagan, takroriy azolarga ruxsat yo'q
# dict - tartibli, o'zgaruvchan, takroriy azolarga ruxsat yo'q

cars = ['malibu', 'Gentra', 'BMW M5']
# cars[0] = "Damas"
# cars[1:2] = ["nexia2", "nexia3"]
# cars[2:] = ["MERS"]

# insert(index, object) - ro'yxatdan hech qanday elementni olib tashlamasdan
# ko'rsatilgan indexga yangi element qo'shish

cars.insert(0, "Cobalt")
# print(cars)

# append() - ro'yxat oxiriga element qo'shish uchun
cars.append("Toyota")
# print(cars)

# extend() - boshqa ro'yxat elementlarini joriy ro'yxatga qo'shish uchun
car1 = ['Malibu']
car2 = ["Gentra"]
car1.extend(car2)
# print(car1)

# har qanday takrorlanadigan ob'ektni qo'shish mumkin
car_list = ["Damas"]
car_tuple = ("Gentra", "Malibu")
# car_list.extend(car_tuple)
# print(car_list)

# remove() - belgilangan elementning ro'yxatda birinchi uchraganini olib tashlaydi

car_list.remove("Damas")
# print(car_list)

# pop(index) - ro'yxatdan belgilangan indexdagi elementni olib tashlaydi,
# agar siz index ko'rsatmasangiz, oxirgi elementni olib tashlaydi

# clear() - ro'yxatni bo'shatadi

car1.clear()
# print(car1)

# ro'yxatni tartiblash
names = ['Halil', 'Guli', 'fozil', 'eldor','Doniyor', 'Botir', 'ali']
# names.sort()
# print(names)

numbers = [1, 9, 8, 10, 7, 6, 5]
numbers.sort()
# print(numbers)
numbers.sort(reverse=True)
# print(numbers)

# Katta-kichik harflarni sezmaydigan qilib tartiblash
# names.sort(key = str.lower)
# print(names)

# reverse() - metodi listni tartibini o'zgartiradi
names.reverse()
print(names)


# ro'yxatni nusxalashning uch usuli
# copy() - metodi
new_names = names.copy()
# list() - metodi
names_list = list(names)
# bo'lim usuli (:)
copy_names = names[:]
# print(copy_names)

# ikki ro'yxatni qo'shishning uch usuli mavjud
list1 = ['samsung', 'xiaomi']
list2 = ['readmi', 'iphone']
# list3 = list1 + list2
# print(list3)

# list2.extend(list1)
# print(list2)

# for x in list2:
#     list1.append(x)
# print(list1)






















































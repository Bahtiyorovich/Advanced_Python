# Ro'yxat - bu tartiblangan va o'zgaruvchan to'plam. Takroriy a'zolarga ruxsat beradi.
# Tuple - bu tartiblangan va o'zgarmas to'plam. Takroriy a'zolarga ruxsat beradi.
# Toʻplam tartibsiz, oʻzgarmas* va indekslanmagan toʻplamdir. Takroriy a'zolar yo'q.
# Lug'at tartibli** va o'zgaruvchan to'plamdir. Takroriy a'zolar yo'q.


this_dict = {
    "Lang":"Python",
    "type":"Dynamic",
    "place_of_use": ["web", "data_since", "machine_learning", "Gameing"]
}

# lug'at yaratish uchun dict() konstruktoridan foydalanish mumkin

my_car = dict(name = "BMW M_5 Compitation", color = "Black_Silver", year = 2022, price = 150000)

# lug'at elementlariga kirish

x = my_car['name']
# print(x)

y = my_car.get("color")
# print(y)

z = my_car.keys()
k = my_car.values()
# print(f"{z}\n {k}")

# items() - metodi lug'at elementlarini kortej sifatida qaytaradi

d = my_car.items()
# print(d)

# Lug'atni yangilash yoki yangi element qo'shish

my_car['color'] = 'black'
# print(my_car.get('color'))

my_car['driver'] = 'Me'
# print(my_car.keys())

my_car.update({"year":2024})
# print(my_car.get('year'))

my_car.update({"mode":"avtomaticaly"})
print(my_car.items())

# Lug'atdan element olib tashlash

# my_car.pop('price')
# print(my_car)
# oxirgi kiritilgan elementni olib tashlaydi
# my_car.popitem()
# my_car.clear() # lug'atni bo'shatadi

# print(my_car)


# Lug'atni loopga solish

# for x in my_car:
#     print(my_car[x]) #faqat qiymatlarini chop etish

# for k in my_car.values():
#     print(k)

# for j in my_car.keys():
#     print(j)

# Lug'atning nusxasini olish

new_car = my_car.copy()
new_car2 = dict(my_car)

# print(new_car)
# print(new_car2)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# yoki

car1 = { "name":"BMW M4", "color":"black"}
car2 = {"name":"BMW M5", "color":"black"}
car3 = {
    "car1":car1,
    "car2":car2
}

for key, value in car3.items():
    print(key)
    for k in value:
        print(value[k])






















































































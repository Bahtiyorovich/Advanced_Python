# if else 9-dars
# butun son berilgan, agar son musbat bo'lsa, 1 ga oshirilsin,
# aks xolda o'zgartirilmasin, natija print qilinsin

# input ma'lumotlarni string formatda qabul qiladi,
# bu matematik amallarni bajarishga halaqit qiladi,

# x = input("Ixtiyoriy butun son kiriting: ")
#
# if x.isalpha():
#     print("Iltimos raqam ma'lumot turini kiriting")
# elif not x:
#     print("Iltimos son kiriting")
#
# elif x.isalpha != True and int(x) == 0:
#     print(f"{x} musbat ham emas, manfiy ham emas")
#
# elif int(x) < 0:
#     print(x)
# else:
#     x = int(x) + 1
#     print(x)


# y = input("Ixtiyoriy butun son kiriting: ")
#
# if y.isalpha():
#     print("Iltimos raqam ma'lumot turini kiriting")
# elif not y:
#     print("Iltimos son kiriting")
#
# elif y.isalpha != True and int(y) == 0:
#     print(10)
#
# elif int(y) < 0:
#     print(int(y) - 2)
# else:
#     y = int(y) + 1
#     print(y)



def musbat_son(a, b, c):
    """ bu funksiya uchta son ichida nechtasi musbat ekanligini aniqlash uchun ishlatiladi """
    # pass
    sonlar = [a, b, c]
    manfiy = 0
    musbat = 0

    for i in sonlar:
        if i > 0:
            musbat += 1
        else:
           manfiy += 1

    return f"{manfiy} ta manfiy son, {musbat} ta musbat son"

    # print(f"{count} ta musbat son mavjud")
    # return f"{count} ta musbat son mavjud"

print(musbat_son(4, 7, 10))
# musbat_son(-5, 11, -8)










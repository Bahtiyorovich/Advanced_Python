# n = 18
# if n <= 1:
#     print(f"Boshqa variant bering")
# else:
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             print(f"{n} soni tub son emas")
#             break
#         else:
#             print(f"{n} soni tub son")
#             break




while True:
    info = input("Ixtiyoriy ma'lumot kiriting>>> ")
    if info.isdigit():
        print("Dastur yopildi!... Raxmat")
        break


# Ma'lumot o'rnida qabul qilasizlar!, agar masalada biror shart bajarilmaguncha tsikl(takrorlanish) bajarilishi davomiyligi talab qilinsa," while "operatoridan foydalaning,
# agar ro'yxat yoki to'plam ustida amal bajarish kerak bo'lsa "for" operatoridan foydalaning

nums = []
i = 0
while i <= 10:
    son = int(input(">>>"))
    if son > 0:
        nums.append(son)
    i += 1

print(nums)

nums = []
i = 0
while True:
    son = int(input(">>>"))
    if son > 0:
        nums.append(son)
        if i == 10:
            break
    i += 1

print(nums)

































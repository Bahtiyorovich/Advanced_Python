# SELECTION SORT
# algoritmi
# 1. bo'sh ro'yxat yaratib olamiz
# 2. ro'yxatdan eng katta elementni topib, bo'sh ro'yxatga qo'shamiz
# 3. 2-qadamni takrorlaymi, toki ro'yxat tugamaguncha

# Big_O O(n**2)

def selection_sort(arr):
    sorted_arr = []  # Bo'sh ro'yxat yaratamiz
    k = len(arr)
    while arr:  # Asosiy ro'yxatdagi elementlar tugamaguncha davom etamiz
        # Eng katta elementni va uning indeksini topish uchun boshlang'ich qiymatlarni o'rnatamiz
        max_index = 0

        # Ro'yxatni boshidan oxirigacha aylanamiz
        for i in range(1, k):
            if arr[i] > arr[max_index]:
                max_index = i  # Eng katta elementning indeksini yangilaymiz

        # Eng katta elementni saralangan ro'yxat boshiga qo'shamiz
        sorted_arr.append(arr[max_index])

        # Eng katta elementni `arr` ro'yxatidan olib tashlaymiz
        arr.pop(max_index)

    return sorted_arr


arr = [17, 5, -36, 89, 45, 25, 75, 84, 63, 22, 23, 30]
print(selection_sort(arr))



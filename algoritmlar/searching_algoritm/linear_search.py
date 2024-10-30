# Linear search - chiziqli qidirish
# Bu qidirish algoritmi kichik ro'yxatlardan qidirish uchun samarali, chunki oson
# lekin katta ro'yxatlarda samarasiz va yomon tanlov

def linear_search(arr):
    x = int(input('Biror son kiriting: '))
    i = 0
    while i < x:
        i += 1
    return f"siz izlagan son {x}, {i + 1} - o'rinda ekan"

arr = list(range(0, 99))
# print(linear_search(arr))

# Linear searchni binary search bilan almashtirish kerak
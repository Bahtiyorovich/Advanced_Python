# Binary search
"""
 Bizda N ta elementdan iborat A ro'yxat bor:
 T biz izlayotgan qiymat
 Bizga T ning indeksi kerak

 Bu masalani hal qilish uchun chegara belgilab olamiz:
    1. Pastki chegara L=0, tepa chegara H = N - 1
    2. Tekshirib olamiz L < H danligini, agar shart bajarilmasa qidirishni to'xtatamiz
    3. O'rta qiymatni indeksini topamiz m = (l + h)/2
    4. Agar Am = T bo'lsa m ni qaytaramiz. Dastur to'xtaydi
    5. Agar Am < T bo'lsa, L = m + 1 qilamiz va 3-qadamga qaytamiz
    6. Agar Am > T bo'lsa, H = m - 1 qilamiz va 3-qadamga qaytamiz

"""
def binary_search(arr):
    x = int(input("Biror son kiriting: "))
    k = len(arr) - 1
    i = 0

    while i <= k:
        """o'rta indeksni topamiz"""
        m = (i + k)//2

        # agar o'rta qiymat x ga teng bo'lsa indexni qaytaramiz
        if arr[m] == x:
            return m

        elif arr[m] < x:
            i = m + 1

        else:
            k = m - 1

    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# index = binary_search(arr)
# if index != -1:
#     print(f"Qiymat {arr[index]} indexi: {index} ")
# else:
#     print(f"Qiymat topilmadi")

# Bu kod o'sish tartibida saralangan ro'yxatda ikkilik qidiruv yordamida
# izlanayotgan qiymatni topishga yordam beradi.

# Binary searchda N ta elementdan iborat ro'yxat uchun maximum qidirishlar soni log2(N) ga teng

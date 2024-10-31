# Divide & Conquer - bo'lib tashlab, hukmronlik qil

# Katta muammolarni kichik muammolarga bo'lib hal qiladi bu metod

# Ikki sonning EKUBini aniqlovchi funksiya tuzamiz

def ekub(a, b):
    return a if b == 0 else ekub(b, a % b)

# print(ekub(45, 25))

def three_ekub(a, b, c):
    return ekub(ekub(a, b), c)

# Ekuk
"""
EKUK(a, b) = abs(a, b) // EKUB(a, b)
"""

def ekub_two(a, b):
    return a if b == 0 else ekub(b, a % b)

def ekuk(a, b):
    return abs(a * b) // ekub(a, b)

def three_ekuk(a, b, c):
    return ekuk(ekuk(a,b), c)


# array elementlari yig'indisini rekursiya yordamida hisoblash

def summ_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + summ_arr(arr[1:])
arr = [5, 10, 15]
print(summ_arr(arr))





































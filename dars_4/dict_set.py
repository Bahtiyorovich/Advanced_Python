# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha
# guruhlaydigan str_counter(strs) funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}
def str_counter(strs):
    """element uzunligi bo'yicha tartiblaydigan funksiya"""
    str_dict = {}
    for i in strs:
        x = len(i)
        if x not in str_dict:
            str_dict[x] = [i]
        else:
            str_dict[x].append(i)

    return str_dict

str_list = ['apple', 'banana', 'cherry', 'chevrolet']
#print(str_counter(str_list))
# lug'at ichida bir xil kalitlarga ruxsat berilmagani
# uchun ro'yxatda bir uzunlikdagi bir nechta elementdan faqat bittasini ko'rsatadigan xolatdan qochish
# uchun elementlarni har birini list ichida qabul qiladigan funksiya yozildi


# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan,
# kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan
# elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
#    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}

def merge_list(l1, l2):
    """Ikkita list elementlarini mos ravishda kelit qiymat ko'rinishida qaytaradigan funksiya"""

    merge_dict = {}
    k = len(l1)
    for i in range(0, k):
        merge_dict[l1[i]] = l2[i]

    return merge_dict

# print(merge_list(list_1, list_2))



# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

class MyFriendsNumber:
    def __init__(self):
        self.info = {}

    def all_info(self):
        for key, value in self.info.items():
            return f"{key} ___ {value}"

    def get_number(self, name):
        return self.info.get(name, None)

    def add_number(self, new_name, new_number):
        self.info[new_name] = new_number

    def update_number(self, up_name, up_number):
        self.info[up_name] = up_number

    def delete_number(self, del_name):
        del self.info[del_name]

# friends_contacts = MyFriendsNumber()
# print(friends_contacts.get_number("Ali"))
# friends_contacts.add_number("Ali", 998931789595)
# print(friends_contacts.get_number("Ali"))
# print(friends_contacts.update_number("Ali", 998901770505))
# print(friends_contacts.delete_number("Ali"))
# print(friends_contacts.all_info())

# Bunday masalalarni hal qilishda classlardan yaxshiroq yechim yo'q deb o'yladim



# 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning
# takrorlanish sonini o'z ichiga
# olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.

# Bu masalani collections dagi Counter metodi yordamida qilsa ham bo'ladi
def counter_dict(arr):
    """List ichida takrorlanuvchi qiymatlar sonini aniqlovchi funksiya"""
    count = {}
    k = len(arr)
    for i in arr:
        n = 0
        for j in range(0, k):
            if i == arr[j]:
                n += 1
        count[i] = n

    return count
arr = [2, 1, 1, 1]
# print(counter_dict(arr))


# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}

def max_ball_students(students):
    """Lug'at ichidagi eng katta qiymatli kalitlarni ajratib olish funksiyasi"""
    if len(students) <= 1:
        return f"Kamida ikkita talabaning ma'lumoti qabul qilinadi"

    ball = []
    names = []
    for key, value in students.items():
        ball.append(value)
        names.append(key)

    ball.sort()
    result = []
    for name in names:
        if students[name] == ball[-1]:
            result.append(name)
        if students[name] == ball[-2]:
            result.append(name)

    for i in range(0, len(result)):
        print(f"{result[i]} {ball[-2 + i]} ball bilan {2 - i} - o'rin")

max_ball_students({"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80})










































































































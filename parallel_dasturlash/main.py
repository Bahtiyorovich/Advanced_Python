import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200_00_000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Kutish boshlandi...")
    time.sleep(sec)
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Kutish yakunlandi...")


def cpu_bound(n):
    pid = os.getpid()
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash boshlandi...")
    while n > 0:
        n -= 1
    print(f"{pid} * {current_process().name} * {current_thread().name} --> Hisoblash yakunlandi...")


if __name__ == "__main__":
    start = time.time()
    end = time.time()
    # 1-holat: Single threeding io_bound
    # io_bound(SLEEP)
    # io_bound(SLEEP)

    # 2-holat: multithreeding io_bound
    # t1 = Thread(target=io_bound, args=(SLEEP,))
    # t1 = Thread(target=io_bound, args=(SLEEP,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 3-holat; singlethreed cpu_bound
    # cpu_bound(COUNT)
    # cpu_bound(COUNT)

    # 4-holat: multithreeding cpu_bound
    # t1 = Thread(target=cpu_bound, args=(COUNT,))
    # t2 = Thread(target=cpu_bound, args=(COUNT,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # 5-holat: multiprocessing cpu_bound
    # p1 = Process(target=cpu_bound, args=(COUNT,))
    # p2 = Process(target=cpu_bound, args=(COUNT,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # 6-holat: multiprocessing io_bound
    # i1 = Process(target=io_bound, args=(SLEEP,))
    # i2 = Process(target=io_bound, args=(SLEEP,))
    # i1.start()
    # i2.start()
    # i1.join()
    # i2.join()

    # print(f"Ketgan vaqt; {end - start}")

# Xulosa:
# 1- io_bound - threeding
# 2- cpu_bound - mucurrent_thread()
"""
Optimallashtirish uchun Tavsiyalar
CPUga yuk bo‘lgan vazifalar: Multiprocessingni hisoblashda talab qilinadigan ishlar uchun ishlating, 
chunki bu bir nechta yadrolarga ishlash imkonini beradi va umumiy bajarish vaqtini qisqartiradi.

Kutishga asoslangan vazifalar: Threadingni io_bound kabi vazifalar uchun ishlating, 
chunki bu multiprocessingdan kamroq xotira talab qiladi va asosan kutishga asoslangan vazifalarni samarali bajaradi.
"""

# Real vaqtni ko'rsatuvchi soat dsturi
while True:
    hozirgi_vaqt = time.strftime("%H:%M:%S") #  orqali hozirgi vaqtni soat, daqiqa va sekundlarda olamiz.
    print(f"\rHozirgi vaqt: {hozirgi_vaqt}", end="") # bilan har bir yangi vaqt ma'lumotini eskisini o'chirib, yangisini bir qatorga chop etamiz.
    time.sleep(1) # yordamida dastur har bir yangilanish orasida 1 soniya kutadi, shunda sekundlar real vaqt rejimida o'zgarib turadi.


# Python’da GIL (Global Interpreter Lock) — bu Python’ning ba’zi ishlash xususiyatlarini tartibga soluvchi mexanizmdir.
# Bu asosan CPython interpretatori bilan ishlaydi va
# bir vaqtning o‘zida faqat bitta treakni bajarishga ruxsat beruvchi
# global blokirovka yoki qulf hisoblanadi.


# GIL qanday ishlaydi?
# GIL Python’ning ichida boshqa treaklar bajarilayotgan bo‘lsa ham,
# faqat bitta treakning interpreter kodini ishlatishiga ruxsat beradi. Bu quyidagicha ishlaydi:
#
# Treak yaratish va GIL qo‘lga olish: Har bir Python treagi ishlashni boshlaganda
#  avval GILni qo‘lga olishga harakat qiladi. GILni olishni uddalasa,
#  ushbu treak Python kodini bajarishni boshlaydi.
#
# GILni boshqa treakka berish: Python’ning interpretatori treakning bir qismini bajarib,
#  keyin GILni boshqa treakka uzatadi. Bu uzatish odatda
#  har bir 100 ta Python bayti kodi (bytecode) bajarilgandan keyin yoki
#  treak kutish holatiga o‘tganidan keyin amalga oshadi.
#
# Treaddagi GILni bo‘shatish: GILni bo‘shatish — bu boshqa treaklarning ham
# kod bajarish imkoniyatiga ega bo‘lishini ta’minlash uchun amalga oshiriladi.
#
# GILning afzalliklari va kamchiliklari
# Afzalliklari:

# Xavfsizlikni oshiradi: GIL Python ichida ko‘p treakli kod bajarilganda xotira boshqaruvini
#  soddalashtiradi va xotira xavfsizligini oshiradi.
# Interpreterni optimallashtirishni osonlashtiradi: GIL yordamida
# Python interpretatori har xil optimallashtirishlarni tezroq amalga oshirishi mumkin.
# Ko‘p vazifalarni oson boshqarish: GIL’ni boshqarish orqali Python’da
# ko‘p vazifa bilan ishlashni sodda va boshqariladigan qiladi.

# Kamchiliklari:

# CPUga yuk bo‘lgan treaklarda sekinlik: GIL Python’da bir vaqtning o‘zida faqat
# bitta treak bajarilishiga ruxsat beradi, shuning uchun ko‘p yadroli protsessorlarda bu
# hisoblashni sezilarli darajada sekinlashtiradi.
# Ko‘p yadroli ishlashni to‘liq qo‘llab-quvvatlamaydi:
#  GIL sababli ko‘p yadroli protsessorlardan to‘liq foydalana olmaydi.
# Ko‘p treakli dasturlar samaradorligini pasaytiradi:
#  GIL ko‘p treakli dasturlarni sekinlashtirishi mumkin,
#  chunki har bir treak bir-birini kutishga majbur bo‘ladi.
# GILni aylanib o‘tish usullari
# GIL faqat Python kodiga taalluqli, boshqa tillardagi kodlarga esa taalluqli emas.
# Python’da quyidagi usullar bilan GIL’ni aylanib o‘tish mumkin:
#
# Multiprocessing modulidan foydalanish: Bu modul har bir jarayon uchun alohida interpreter ishga tushiradi,
# bu esa ko‘p yadroli protsessorlarda GIL’ni aylanib o‘tishga yordam beradi.
#  Har bir jarayon o‘ziga xos GIL’ga ega bo‘lib, bir-biriga bog‘liq emas.
#
# C yoki Cython bilan integratsiya: GILni talab qilmaydigan C yoki Cython kodlarini
#  ishlatish orqali yuqori samaradorlikka erishish mumkin.
#
# Asinxron dasturlash (asyncio): GIL’dan foydalanmasdan,
# asinxron treaklashni boshqarish uchun asyncio modulidan foydalanish mumkin.
# Bu modullar ko‘pincha I/Oga asoslangan vazifalar uchun ishlatiladi va GIL’dan
#  foydalanmagan holda samarali ishlaydi.
#
# Xulosa
# GIL Python’ning ichki tuzilishi xavfsizligi va ishlash optimallashtirilishini
# ta’minlash uchun foydali bo‘lsa-da, bu ko‘p yadroli ishlashni
# to‘liq qo‘llab-quvvatlamaslik kabi kamchiliklarga ega.
# CPUga yuk bo‘lgan vazifalarni bajarish uchun Python’da
# multiprocessing yoki Cython kabi usullarni qo‘llash samarali yechim bo‘lishi mumkin.
#

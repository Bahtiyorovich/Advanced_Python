# Global Scope - o’zgaruvchi funksiyadan tashqarida yaratilganda
# u o’sha fayldagi barcha funksiyalar uchun acessable bo’ladi.

# Local Scope - o’zgaruvchi funksiya ichida e’lon qilinganda,
# u faqat o’sha funksiya uchun acessable bo’ladi.
a = 4
def f1():
	global a
	a = 5
	print(a) # local -> 5

# print(a) #global -> 4

# Nonlocal Scope - funksiya ichida yaratilgan o’zgaruvchi,
# funksiya ichidagi boshqa funksiyalar(inner functions) uchun ham acessable bo’ladi.


# Ichki funksiya nonlocal o’zgaruvchiga murojaat qila oladi, lekin o’zgartira olmaydi.
# Agar o’zgartirmoqchi bo’lsa, **nonlocal** so’zidan foydalanadi.

def f1():
	a = 4
	def f2(): #inner function
		nonlocal a
		a += 2
	print(a)  # -> 6



def f(x):
    def g(y):
        return y
    return g
z = 5
b = 1

h=f(z)
natija = h(b)
print(natija )  # Output is 1

# yoki
natija = f(z)(b)
print(natija )  # Output is 1

def f(x):
    def g(y):
        def h(z):
            return z
        return h
    return g
k = 5
b = 2
c = 1
f(k)(b)(c)  # Output is 1

# CLOSURE - tashqi funksiyaning nonlocal o’zgaruvchilarini
# ishlata olish imkoniyatiga ega ichki funksyadir.

# Composer

def composer(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h

km_to_m = lambda z: z*1000
m_to_sm = lambda y: y*100

km_to_sm = composer(km_to_m, m_to_sm)
print(km_to_sm(12))































































































































































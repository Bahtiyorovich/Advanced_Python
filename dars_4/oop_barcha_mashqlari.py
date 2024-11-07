# Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
# output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.

class Oson1:
    a = 7
    @classmethod
    def output_a(cls):
        print(cls.a)
# Oson1.output_a()


# Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
# summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.
class Oson2:
    a = 7
    b = 11

    @classmethod
    def summa(cls):
        result = cls.a + cls.b
        print(f"{result}")
# Oson2.summa()

# Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
# plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.

class Oson3:
    a = 11

    @classmethod
    def plus_minus(cls):
        if cls.a > 0:
            return f"{cls.a} musbat son"
        else:
            return f"{cls.a} manfiy son"

# print(Oson3.plus_minus())

# Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
# odd_even() - bu funksiya klassdagi "a" ni to'g yoki juft ekanligini print qilib bersin.

class Oson4:
    a = 12

    @classmethod
    def odd_even(cls):
        if cls.a % 2 == 0:
            return f"{cls.a} juft son"
        else:
            return f"{cls.a} toq son"
# print(Oson4.odd_even())

# Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
# daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.

class Oson5:
    a = 2
    b = 3

    @classmethod
    def pow(cls):
        return f"{cls.a ** cls.b}"

# print(Oson5.pow())

# 6. "MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
# add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
# remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.

class MyClass6:
    words = []

    @classmethod
    def add_word(cls, word):
        if word and isinstance(word, str):
            cls.words.append(word)
            print(f'"{word}" ro\'yxatga qo\'shildi.')
        else:
            print(f'Ma\'lumot xato')
    @classmethod
    def remove_word(cls, word):
        if word in cls.words:
            cls.words.remove(word)
            print(f'"{word}" so\'zi ro\'yxatdan o\'chirildi')
        else:
            print("Ma'lumot topilmadi")

    @classmethod
    def get_words(cls):
        return cls.words

# MyClass6.add_word("Python")
# MyClass6.get_words()
# MyClass6.remove_word("Python")


# 7. "MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
# add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
# bor bolsa xech narsa qilmasin.
# update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
# yoq bolsa xech narsa qilmasin.

class MyClass7:
    myDict = {}

    @classmethod
    def get_mydict(cls):
        return cls.myDict

    @classmethod
    def add_elem(cls, key, val):
        if key and val:
            cls.myDict.setdefault(key, val)

    @classmethod
    def update_elem(cls, key, val):
        if key and val and key in cls.myDict.keys():
            cls.myDict[key] = val

# print(MyClass7.get_mydict())
# MyClass7.add_elem("python", "OOP")
# print(MyClass7.get_mydict())
# MyClass7.update_elem("python", "Decorators")
# print(MyClass7.get_mydict())

# 8. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
# compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi
# "new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin.

class MyClass8:
    def __init__(self, numbers):
        self.total = sum(numbers)

    def compare_list(self, new_list):
        second_list = sum(new_list)
        return max(self.total, second_list)

# myClass8 = MyClass8(list(range(10)))
# print(myClass8.compare_list(list(range(6))))


# 9. "MyClass9" nomli klass elon qililar. Bu klassdan "list1" va "list2" list o'zgaruvchilari bor.
# list1_max() - bu funksiya klassdagi "list1" dan maximumni topib return qilsin.
# list2_max() - bu funksiya klassdagi "list2" dan maximumni topib return qilsin.
# sum_of_two_max() - bu funksiya klassdagi list1_max() va list2_max() foydalanib ikkita maximumni topib yig'indisini print qilsin.

class MyClass9:
    def __init__(self, list_first, list_second):
        self.list_one = list_first
        self.list_two = list_second
    # Eng optimal yechim taklif qilaman, bu usul max() funksiyasini bir marta argument sifatida ishlatadi
        self.list_one_max_value = max(self.list_one)
        self.list_two_max_value = max(self.list_two)

    def sum_of_two_max_value(self):
        return self.list_one_max_value + self.list_two_max_value


    # masalani shartiga moslab kod yozilsa bu katta hajmdagi
    # listlar uchun kodning ishlash tezligini pasaytirib yuboradi
    # buning sababi max() funksiyasi uchun O(n) tezlikda ishlashidir

    # def list_one_max(self):
    #     return max(self.list_one)
    #
    # def list_two_max(self):
    #     return max(self.list_two)

    # def sum_of_two_max_value(self):
    #     res1 = self.list_one_max()
    #     res2 = self.list_two_max()
    #
    #     return res1 + res2

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# myClass9 = MyClass9(arr1, arr2)
# print(myClass9.sum_of_two_max_value())


# 10. "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
# divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
# va funksiya oxirida bolinadigonlarni listini return qilsin.

class MyClass10:
    def __init__(self, numbers):
        self.numbers = numbers
        self.new_list = []

    def divide(self, d):
        if not self.numbers:
            return f"{self.numbers}, Ma'lumotlar mavjud emas"

        for i in self.numbers:
                if i % d == 0:
                    self.new_list.append(i)

        return self.new_list

# myClass10 = MyClass10(list(range(2, 30)))
# print(myClass10.divide(5))

# OOP2 vazifalari
# 1-masala yechimi

class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def get_info(self):
        return f"Texnika: {self.brand} brendi ostida, Modeli: {self.model}, Texnika turi: {self.type}"

class Notebooks(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        return f"Texnika: Brendi: {self.brand},\n Modeli: {self.model},\n Turi: {self.type},\n Video Cartsi: {self.video_card},\n RAM: {self.ram},\n Display o'lchami: {self.display}"

class Television(Notebooks):
    def __init__(self, size, display):
        super().__init__(display)
        self.size = size

    def more_info(self):
        return f"{self.get_info()}, {self.size}, {self.display}"

class Smartphones(Television):
    def __init__(self, size, sim_count):
        super().__init__(size)
        self.sim_count = sim_count

    def more_info(self):
        return f"{self.more_info()} Sim karta: {self.sim_count}"

texnika = Texnika("artel", "mx", "Phone")
notebook = Notebooks()
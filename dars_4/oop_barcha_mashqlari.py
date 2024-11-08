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

class Television(Texnika):
    def __init__(self,brand, model, type, size, display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def more_info(self):
        return f"{self.get_info()}, {self.size}, {self.display}"

class Smartphones(Texnika):
    def __init__(self,brand, model, type, size, sim_count):
        super().__init__(brand, model, type)
        self.sim_count = sim_count
        self.size = size

    def more_info(self):
        return f"{self.get_info()} Sim karta: {self.sim_count}"

notebook = Notebooks("Dell", "XPS 13", "Notebook", "Intel Iris", "16GB", "13.4 inch")
television = Television("Samsung", "QLED", "Television", "55 inch", "4K")
smartphone = Smartphones("Apple", "iPhone 14", "Smartphone", "6.1 inch", 2)

# Ma'lumotlarni chiqaramiz
# print(notebook.more_info())
# print(television.more_info())
# print(smartphone.more_info())


# 2-masala

class Transport:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def get_info(self):
        print(f"Transport >> {self.brand} brendi ostida, Modeli: {self.model}, turi: {self.type}")

class ElectroCar(Transport):
    def __init__(self, brand, model, type, battery_life, chargin_time):
        super().__init__(brand, model, type)
        self.battery_life = battery_life
        self.chargin_time = chargin_time

    def more_info(self):
        print(f"{self.get_info()}"
              f"Batareya yaroqlilik muddati: {self.battery_life}, bir marta to'liq zaryadlash vaqti: {self.chargin_time}")

class SportCar(Transport):
    def __init__(self, brand, model, type, motor, color):
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.motor} motori bilan jixozlangan, {self.color} rangida")

class Truck(Transport):
    def __init__(self, brand, model, type, motor, height, long, weight):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.motor}, {self.height}, {self.long}, {self.weight}")

# tesla = ElectroCar("Tesla", "Model S", "Electric Car", "402 miles", "8 hours")
# bmw_m5 = SportCar("BMW", "M5 Competition", "Sports Car", "4.4L V8", "Black")
# truck = Truck("Volvo", "FH16", "Truck", "540 HP", "4 meters", "7 meters", "12 tons")
#
# # Ma'lumotlarni chiqaramiz
# tesla.more_info()
# bmw_m5.more_info()
# truck.more_info()



# 3-masala
class University:
    def __init__(self, university):
        self.university = university

    def get_info(self):
        print(f"{self.university}")

class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.name = first_name
        self.surname = last_name
        self.age = age

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.name}, {self.surname}, {self.age}")

class Student(University):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university)
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.group = group

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.name}, {self.surname}, {self.age}, {self.group}")

class Teacher(University):
    def __init__(self, university, first_name, last_name, position, subject):
        super().__init__(university)
        self.name = first_name
        self.surname = last_name
        self.position = position
        self.subject = subject

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.name}, {self.surname}, {self.position}, {self.subject}")

class OtherStaff(University):
    def __init__(self, university, first_name, last_name, position):
        super().__init__(university)
        self.name = first_name
        self.surname = last_name
        self.position = position

    def more_info(self):
        print(f"{self.get_info()}"
              f"{self.name}, {self.surname}, {self.position}")

# staff = Staff("Namdu", "Ali", "Valiyev", 26)
# student = Student("Namdu", "John", "Smith", 21, "201")
# teacher = Teacher("Namdu", "Shox", "Temur", "mutahasis", "Fizik")
# other_staff = OtherStaff("Namdu", "Bobur", "Mansurov", "professor")
#
# staff.more_info()
# student.more_info()
# teacher.more_info()
# other_staff.more_info()


# 4-masala

class Object(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name

    def object_info(self):
        print(f"{self.get_info()}, {self.name}")

class Computer(Object):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info(self):
        print(f"{self.get_info()}, {self.name}, {self.soni}, {self.tizimi}, {self.holati}")

class Mebel(Computer):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name, soni, tizimi, holati)

    def furniture(self):
        print(f"{self.object_more_info()}")

object = Object("Namdu", "Fizika Laboratoriyasi")
hp = Computer("Namdu", "hp", 20, "Microsoft", "new")
furniture = Mebel('Namdu', "special chair", 10, "", "new")

object.object_info()
hp.object_more_info()
furniture.object_more_info()


# OOP 3 - topshiriq
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Depozit: {amount} so'm qo'shildi. Joriy balans: {self.balance} so'm."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Pul yechildi: {amount} so'm. Joriy balans: {self.balance} so'm."
        else:
            return "Balans yetarli emas."

    def check_balance(self):
        return f"Joriy balans: {self.balance} so'm."


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width


class StudentMe:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def print_summary(self):
        average = self.calculate_average()
        return f"Ism: {self.name}, Yosh: {self.age}, O'rtacha baho: {average}"


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.current_page = 1

    def open(self, page):
        self.current_page = page
        return f"Kitob {page}-sahifada ochildi."

    def turn_page(self):
        self.current_page += 1
        return f"Sahifa ochildi: {self.current_page}."

    def restart(self):
        self.current_page = 1
        return "Kitob boshidan ochildi."


class Dog:
    total_dogs = 0

    def __init__(self):
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

class Computer:
    total_computers = 0
    computers_list = []

    def __init__(self, model):
        self.model = model
        Computer.add_computer(self)

    @classmethod
    def add_computer(cls, computer):
        cls.computers_list.append(computer)
        cls.total_computers += 1


class Employee:
    total_employees = 0
    employees_list = []

    def __init__(self, name):
        self.name = name
        Employee.hire_employee(self)

    @classmethod
    def hire_employee(cls, employee):
        cls.employees_list.append(employee)
        cls.total_employees += 1

class Television:
    average_screen_size = 0
    total_screen_size = 0
    total_televisions = 0

    def __init__(self, screen_size):
        self.screen_size = screen_size
        Television.update_average_screen_size(screen_size)

    @classmethod
    def update_average_screen_size(cls, screen_size):
        cls.total_televisions += 1
        cls.total_screen_size += screen_size
        cls.average_screen_size = cls.total_screen_size / cls.total_televisions


class Course:
    total_courses = 0
    courses_list = []

    def __init__(self, course_name):
        self.course_name = course_name
        Course.add_course(self)

    @classmethod
    def add_course(cls, course):
        cls.courses_list.append(course)
        cls.total_courses += 1


class Math:
    @staticmethod
    def multiply(a, b):
        return a * b


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32


class Distance:
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934


class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


class Time:
    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return (minutes, remaining_seconds)
































































































































































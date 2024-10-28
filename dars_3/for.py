numbers = list(range(10))
# print(numbers)

# for i in numbers:
#     pass

# str1 = "Salom"
# for s in str1:
#     print(s)
# else: print("Finished")

# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print("\r")

# rows = 5
# for i in range(1, rows + 1):
#     print("* " * i)

# rows = 5
# for i in range(rows + 1, 0, -1):
#     for k in range(0, i - 1):
#         print("*", end=" ")
#     print(" ")

# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")

def star_style(n):
    """Bu funksiya * ni kapalak stilida chop etadi"""
    for i in range(n):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n - i - 1) + '*' * (i + 1)
        )
    for i in range(n - 2, -1, -1):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n -i - 1) + '*' * (i + 1)
        )

# star_style(5)

# my_string = input('Enter your string: ')
# my_char = input('Enter your character: ')
#
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# new_string = ''
# for i in my_string:
#     if i in vowels:
#         new_string += my_char
#     else:
#         new_string += i
# print(new_string)

def style_diamond(n):
    for i in range(1, 2 * n):
        spaces = abs(n - i)
        stars = 2 * (n - spaces) - 1
        print(' ' * spaces + '*' * stars)
# style_diamond(5)

def char(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(65 + k), end=" ")
            k += 1
        print()

# char(5)

def numeric(n):
    k = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(k, end=" ")
            k += 1
        print()

numeric(5)












































































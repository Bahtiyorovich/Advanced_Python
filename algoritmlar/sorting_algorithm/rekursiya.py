# REKURSIYA

def count(n):
    print(n)
    if n > 1:
      count(n - 1)

# count(10)

# n!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
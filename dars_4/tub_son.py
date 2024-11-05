n = 18
if n <= 1:
    print(f"Boshqa variant bering")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} soni tub son emas")
            break
        else:
            print(f"{n} soni tub son")
            break



